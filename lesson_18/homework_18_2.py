import requests

BASE_URL = "http://127.0.0.1:8080"

def upload(filename):
    with open(filename, "rb") as f:
        resp = requests.post(f"{BASE_URL}/upload", files={"image": f})
    print("POST:", resp.status_code, resp.json())


def get_url(filename):
    resp = requests.get(f"{BASE_URL}/image/{filename}", headers={"Content-Type": "text"})
    print("GET:", resp.status_code, resp.json())


def delete(filename):
    resp = requests.delete(f"{BASE_URL}/delete/{filename}")
    print("DELETE:", resp.status_code, resp.json())


if __name__ == "__main__":
    filename = "PIA14253~orig.jpg"
    upload(filename)
    get_url(filename)
    delete(filename)
