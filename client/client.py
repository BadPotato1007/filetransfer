from flask import Flask, request, send_from_directory
import requests
import os

app = Flask(__name__)
DOWNLOAD_DIR = os.getcwd()

@app.route('/download', methods=['GET'])
def download():
    file_name = request.args.get('file')
    if file_name:
        url = f"http://localhost:8000/{file_name}"
        local_filename = os.path.join(DOWNLOAD_DIR, file_name)
        download_file(url, local_filename)
        return f"Downloading {file_name}", 200
    return "No file specified", 400

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded {local_filename}")

if __name__ == "__main__":
    app.run(port=8001)
