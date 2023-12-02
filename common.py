import os
from typing import Generator

import requests


def from_file(filename):
    if not os.path.exists(filename):
        return None

    with open(filename, "r", encoding="utf-8") as f:
        print(f"Returning from file: {filename}")
        return f.read()


def download_input(day: int, year: int) -> str:
    filename = f"inputs/{year}/input-{day}.txt"
    data = from_file(filename)
    if data:
        return data

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = "53616c7465645f5f62c4f773983f52e5d476eb24d9ea4e7fca4937da5f35b65b1044619e60e68cceae97e4cf142e024bae6aba793fe6823bee60a6aa18de5c52"
    cookies = {"session": session}

    response = requests.get(url, cookies=cookies)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)

    return response.text


def get_input(day: int, year: int) -> Generator[str, None, None]:
    response = download_input(day, year)

    yield from response.strip().split("\n")
