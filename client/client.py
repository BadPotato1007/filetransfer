import requests

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded {local_filename}")

if __name__ == "__main__":
    server_ip = "localhost" 
    port = 8000
    file_name = "file_to_send.txt"
    url = f"http://{server_ip}:{port}/{file_name}"
    download_file(url, file_name)
