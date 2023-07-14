import asyncio
from fastapi import APIRouter
from typing import List
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

router = APIRouter()


@router.get("/getPhotos")
async def get_photos(username: str, max_count: int) -> dict:
    return {"urls": await scrape_photos(username, max_count=max_count)}


async def scrape_photos(username: str, max_count: int) -> List[str]:
    options = Options()
    options.add_argument('--proxy-server=socks5://45.93.70.123:8000')
    options.add_argument("--user-data-dir=C:\\Users\\dc-1e\\Desktop\\glam_test_task\\chrome")
    photos = []
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://www.instagram.com/{username}/")
    sleep(5) # Ждем пока загрузится страница
    articles = driver.find_elements("tag name", "article")
    elements_inside_article = articles[0].find_elements("tag name", "a")
    counter = 0
    for article in elements_inside_article:
        counter += 1
        photos.append(article.get_attribute("href"))
        if (counter == max_count):
            break
    
    return photos