"""
Є відкритий офіційний API NASA Images and Video Library ( https://images-api.nasa.gov ),
який дозволяє виконувати пошук медіа та отримувати список файлів (assets) для кожного знайденого медіа-елемента.

Ваше завдання - за допомогою модуля requests:

Виконати пошук зображень, пов’язаних з ровером Curiosity на Марсі.
З JSON відповіді витягнути nasa_id для знайдених елементів.
Для кожного nasa_id зробити додатковий запит до endpoint-а /asset/{nasa_id}, щоб отримати список URL-ів файлів.
Обрати з цього списку посилання на JPG-зображення (наприклад, перший .jpg або “найкращий” варіант, якщо їх кілька).
Скачати 2 зображення і зберегти локально як:
mars_photo1.jpg
mars_photo2.jpg
Важливо: потрібно виконати мінімум 3 HTTP-запити:

1 запит /search + 2 запити /asset/{nasa_id} (і ще 2 запити на скачування jpg-файлів).

Доступні endpoint-и (Images API)

GET /search?q={q} - пошук медіа
GET /asset/{nasa_id} - список файлів (URL) для вибраного медіа
"""

import requests
import random


BASE_URL = "https://images-api.nasa.gov"

def safe_get(url, params=None):
    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        return resp
    except requests.exceptions.RequestException as e:
        print(f"❌ Помилка запиту: {e}")
        return None

def search_images(query, media_type="image", limit=20):
    url = f"{BASE_URL}/search"
    params = {"q": query, "media_type": media_type, "page_size": limit}
    resp = safe_get(url, params=params)
    if not resp:
        return []
    data = resp.json()
    items = data.get("collection").get("items")
    return [nasa_id["data"][0]["nasa_id"] for nasa_id in items]

def get_asset_urls(nasa_id):
    url = f"{BASE_URL}/asset/{nasa_id}"
    resp = safe_get(url)
    if not resp:
        return []
    data = resp.json()
    return [url_image["href"] for url_image in data.get("collection").get("items")]

def download_image(url, filename):
    resp = safe_get(url)
    if not resp:
        return False
    with open(filename, "wb") as f:
        f.write(resp.content)
    print(f"✅ Збережено {filename}")
    return True


if __name__ == "__main__":
    nasa_ids = search_images("Curiosity rover Mars")
    print("Знайдено nasa_id:", nasa_ids)

    chosen_ids = random.sample(nasa_ids, k=2)
    print("Рендомно обрані nasa_id:", chosen_ids)

    jpg_urls = []
    for nasa_id in chosen_ids:
        urls = get_asset_urls(nasa_id)
        jpg_url = [u for u in urls]
        if jpg_url:
            jpg_urls.append(jpg_url[0])

    for i, url in enumerate(jpg_urls, start=1):
        download_image(url, f"mars_photo{i}.jpg")
