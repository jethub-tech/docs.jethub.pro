import json
import shutil
import time
import zipfile
from pathlib import Path

import click
import requests


API_PATH = "insert_api_path"
CLIENT_TOKEN = "insert_your_private_token"


def create_task(
    path: str,
    sast_python_skiptest: str,
    sast_python_exclude_path: str,
    data_leaks_exclude_path: str,
    global_exclude_path: str,
) -> str:
    """
    Sends a request to the API to create the task.

    Args:
        path (str): The path to the userdata.

    Returns:
        task_id (str): The task identifier inside the API db.

    Raises:
        Exception: If the specified path does not exist.
        Exception: If the API request fails.
    """

    # Check if the specified path exists
    if not Path(path).exists():
        raise Exception("The specified path does not exist")

    # Create the transfer archive
    transfer = "archive.zip"
    if Path(path).is_file():
        # Create archive from 1 file
        zipfile.ZipFile("archive.zip", "w", zipfile.ZIP_DEFLATED).write(path, Path(path))
    else:
        # Create archive from directory
        transfer = shutil.make_archive("archive", "zip", path)

    # Prepare the request data
    file = {"userdata": ("clientarchive.zip", open(transfer, "rb"), "application/zip")}

    # Send the API request
    r = requests.post(
        API_PATH + "/tasks/create_task",
        files=file,
        headers={"Authorization": f"Bearer {CLIENT_TOKEN}"},
        timeout=30,
        data={
            "sast_python_skiptest": sast_python_skiptest,
            "sast_python_exclude_path": sast_python_exclude_path,
            "data_leaks_exclude_path": data_leaks_exclude_path,
            "global_exclude_path": global_exclude_path,
        },
    )

    Path("archive.zip").unlink()

    # Check the API response
    if r.status_code == 200:
        return r.json()["task_id"]

    else:
        # Raise an exception with the error message from the API
        raise Exception(r.json()["msg"])


def wait_results(taskid: str) -> dict:
    """
    Wait for task results from the API.

    This function continuously polls the API for task results until it
    receives a response containing the "data" key or reaches a maximum number of attempts.

    Args:
        taskid (str): Task identifier inside the API database.

    Returns:
        dict: Report.

    Raises:
        Exception: If the function fails to receive a response from the analyzer after 10 attempts.
    """

    # Initialize variables
    data = {}  # API response
    counter = 0  # Number of attempts

    # Continuously poll the API until a response is received or the maximum number of attempts is reached
    while "data" not in data and counter < 10:
        # Send a GET request to the API
        r = requests.get(
            API_PATH + f"/tasks/get_task?task_id={taskid}",
            headers={"Authorization": f"Bearer {CLIENT_TOKEN}"},
            timeout=30,
        )

        # Update the data variable with the JSON response
        data = r.json()

        # Wait for 3 seconds before sending the next request
        time.sleep(3)

        # Increment the counter
        counter += 1

    # Raise an exception if the function fails to receive a response from the analyzer after 10 attempts
    if counter == 10 and "data" not in data:
        raise Exception("Failed to get a response from the analyzer")

    # Return the SAST report
    return data


def write_results(data: dict, out_file: str):
    with open(out_file, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


@click.command(context_settings={"ignore_unknown_options": True})
@click.option("--path", help="Path for transfer to sast", required=True, type=str)
@click.option("--out_file", help="Output file name", default="jethub_report.json", type=str)
@click.option("--sast-python-skiptest", help="Skiptest for sast", type=str)
@click.option("--sast-python-exclude-path", help="Exclude path for sast", type=str)
@click.option("--data-leaks-exclude-path", help="Exclude path for data leaks", type=str)
@click.option("--global-exclude-path", help="Exclude path for global", type=str)
def main(
    path: str,
    out_file: str,
    sast_python_skiptest: str,
    sast_python_exclude_path: str,
    data_leaks_exclude_path: str,
    global_exclude_path: str,
) -> None:
    """
    The main function that creates a new task, waits for the result, and writes the result to a file.
    """

    # Create a new task
    taskid = create_task(
        path, sast_python_skiptest, sast_python_exclude_path, data_leaks_exclude_path, global_exclude_path
    )

    # Wait for the result of the task
    data = wait_results(taskid)

    # Write the result to a file
    write_results(data, out_file)


if __name__ == "__main__":
    main()
