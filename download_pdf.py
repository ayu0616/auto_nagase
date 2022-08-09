from get_tasks import get_tasks, get_token
import requests
import datetime

nagase_token = get_token()
tasks = get_tasks(nagase_token)

payloads: dict[str, list[str]] = {"selected": [], "as_ids": []}
for task in tasks:
    if task["uploaded"]:
        continue
    payloads["selected"].append(task["code"])
    payloads["as_ids"].append(task["as_id"])

url = "https://production-apprunner-api.toshin-correction.com/sheets/download?"
selected_str = "&".join(list(map(lambda x: f"selected[]={x}", payloads["selected"])))
as_id_str = "&".join(list(map(lambda x: f"as_id[]={x}", payloads["as_ids"])))
url = f"{url}{selected_str}&{as_id_str}"

headers = {
    "Authorization": f"Bearer {nagase_token}",
}

res = requests.get(url, headers=headers)
zip_binary = res.content

today = datetime.date.today()
today_string = today.strftime("%Y-%m-%d")
with open(f"/Users/OgawaAyumu/Downloads/{today_string}.zip", "wb") as f:
    f.write(zip_binary)
