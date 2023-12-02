from operator import index
from pprint import pprint

from common import download_input, from_file, get_input


def day_1():
    data = download_input(1, 2023).splitlines()

    def part_one():
        encoding_keys = []
        for line in data:
            first_digit = ""
            second_digit = ""
            for char in line:
                if char.isdigit():
                    if not first_digit:
                        first_digit = char
                    else:
                        second_digit = char

            if not second_digit:
                second_digit = first_digit

            encoding_keys.append(int(first_digit + second_digit))

            return sum(encoding_keys)

    def part_two():
        digits = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        encoding_keys = []

        for line in data:
            print(line)
            min_occurance = len(line)
            max_occurance = 0
            first_digit = ""
            second_digit = ""
            for digit in digits.keys():
                try:
                    line.index(str(digit))
                    min_occurance = min(min_occurance, line.index(digit))
                    max_occurance = max(max_occurance, line.rindex(digit))
                    first_digit = digit
                    second_digit = digit
                except ValueError:
                    continue
            print(first_digit)
            print(second_digit)
            print(int(f"{digits[first_digit]}{digits[second_digit]}"))
            break

    return part_two()


if __name__ == "__main__":
    print(day_1())
