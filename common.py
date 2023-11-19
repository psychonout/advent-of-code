import os
from typing import Generator

import requests


def from_file(filename):
    if not os.path.exists(filename):
        return None

    with open(filename, "r") as f:
        print(f"Returning from file: {filename}")
        return f.read()


def download_input(day: int, year: int) -> str:
    filename = f"inputs/{year}/input-{day}.txt"
    if from_file(filename):
        return from_file(filename)

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = "53616c7465645f5ff2a38047bd2c4bb69793cce92fc9a9e1bdf78140b998c0dc7d19b62335cf60e5524c910ea173f85a9868ce66e9b26d741a9eaf169873561e"
    cookies = {"session": session}

    response = requests.get(url, cookies=cookies)

    with open(filename, "w") as f:
        f.write(response.text)

    return response.text


def get_input(day: int, year: int) -> Generator[str, None, None]:
    response = download_input(day, year)

    yield from response.strip().split("\n")
