import os
from typing import Generator
from loguru import logger
import requests
from dotenv import load_dotenv

load_dotenv()


def from_file(filename):
    if not os.path.exists(filename):
        return None

    with open(filename, "r", encoding="utf-8") as f:
        logger.debug(f"Returning from file: {filename}")
        return f.read()


def download_input(day: int, year: int, test=False) -> str:
    filename = f"inputs/{year}/input-{day}.txt"
    if test:
        filename += ".test"
    data = from_file(filename)
    if data:
        return data

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": os.environ["AOC_SESSION"]}

    response = requests.get(url, cookies=cookies, timeout=5)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)

    return response.text


def get_input(day: int, year: int) -> Generator[str, None, None]:
    response = download_input(day, year)

    yield from response.strip().split("\n")
