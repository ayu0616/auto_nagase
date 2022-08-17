from concurrent.futures import ThreadPoolExecutor
import os
import shutil
from TaskItem import TaskItem
from get_tasks import get_tasks, get_token
import requests
import datetime

nagase_token = get_token()
tasks = get_tasks(nagase_token)

headers = {
    "Authorization": f"Bearer {nagase_token}",
}
base_url = "https://production-apprunner-api.toshin-correction.com/sheets/download?"

# payloads: dict[str, list[str]] = {"selected": [], "as_ids": []}
today = datetime.date.today()
today_string = today.strftime("%Y-%m-%d")
dirname = f"/Users/OgawaAyumu/Downloads/{today_string}"
os.mkdir(dirname)

un_scored_task = list(filter(lambda task: not task["uploaded"], tasks))
task_len = len(un_scored_task)
count = 0


def print_progress():
    global count
    count += 1
    print(f"\r{count}/{task_len} : {round((count)/task_len*100, 1)}%", end="")


def download_task(task: TaskItem):
    error_count = 0
    url = f"{base_url}selected[]={task['code']}&as_id[]={task['as_id']}"
    while True:
        res = requests.get(url, headers=headers)
        if res.ok or error_count > 1:
            zip_binary = res.content
            zip_filename = os.path.join(dirname, f"{task['code']}.zip")
            with open(zip_filename, "wb") as f:
                f.write(zip_binary)
            try:
                shutil.unpack_archive(zip_filename, dirname)
            except Exception:
                continue
            finally:
                os.remove(zip_filename)
            break
        error_count += 1
    print_progress()


with ThreadPoolExecutor(max_workers=10) as executer:
    executer.map(download_task, un_scored_task)

# for i, task in enumerate(un_scored_task):
#     error_count = 0
#     url = f"{base_url}selected[]={task['code']}&as_id[]={task['as_id']}"
#     while True:
#         res = requests.get(url, headers=headers)
#         if res.ok or error_count > 1:
#             zip_binary = res.content
#             zip_filename = os.path.join(dirname, f"{task['code']}.zip")
#             with open(zip_filename, "wb") as f:
#                 f.write(zip_binary)
#             shutil.unpack_archive(zip_filename, dirname)
#             os.remove(zip_filename)
#             break
#         error_count += 1
#     print(f"\r{i+1}/{task_len} : {round((i+1)/task_len*100, 1)}%", end="")
