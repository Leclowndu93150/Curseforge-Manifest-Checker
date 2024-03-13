import requests
import json

API_KEY = "PUT YOUR API KEY HERE"
endpoint = 'https://api.curseforge.com'
iterations = 0

with open("manifest.json", "r") as manifest_file:
    all_mods = json.load(manifest_file)

open('mod_links.txt', 'w').close()
open('error_log.txt', 'w').close()

mod_urls = open("mod_links.txt", "a")

with open("error_log.txt", "a") as error_file:
    for file_data in all_mods["files"]:
        file_id = file_data["fileID"]
        project_id = file_data["projectID"]
        url = f"{endpoint}/v1/mods/{project_id}/files/{file_id}/download-url"
        try:
            r = requests.get(url, headers={"x-api-key": API_KEY})
            response_data = json.loads(r.text)
            download_url = response_data["data"]
            file_name = download_url.split("/")[-1]
            mod_urls.write(f"Download URL for {file_data}: {download_url}\n")
        except Exception as e:
            error_message = f"Error processing file data: {file_data}\nError message: {str(e)}\n"
            error_file.write(error_message)
        iterations += 1
        print(f"Mods Checked = {iterations}")
print('Done.')
