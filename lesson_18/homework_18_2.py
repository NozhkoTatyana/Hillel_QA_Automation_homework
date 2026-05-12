import requests



BASE_URL = "http://127.0.0.1:8080"


def upload(filename):
    with open(filename, "rb") as f:
        resp = requests.post(f"{BASE_URL}/upload", files={"image": f})
    print("POST:", resp.status_code, resp.json())


def get_url_and_image(filename, content_type):
    headers = {
        "Content-Type": content_type
    }

    resp = requests.get(f"{BASE_URL}/image/{filename}",headers=headers)

    if resp.status_code == 200 and content_type == "text":
        print("GET:", resp.status_code, resp.json())

    elif resp.status_code == 200 and content_type == "image":
        with open("downloaded.jpg", "wb") as f:
            f.write(resp.content)
        print("GET IMG:", resp.status_code, "Image saved")


def delete(filename):
    resp = requests.delete(f"{BASE_URL}/delete/{filename}")
    print("DELETE:", resp.status_code, resp)


if __name__ == "__main__":
    filename = "PIA14253~orig.jpg"

    upload(filename)
    get_url_and_image(filename, "text")
    get_url_and_image(filename, "image")
    delete(filename)

