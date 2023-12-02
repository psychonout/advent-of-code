from pprint import pformat

from loguru import logger

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
            min_occurance = len(line)
            max_occurance = 0
            first_digit = ""
            second_digit = ""
            for digit in digits.keys():
                try:
                    logger.debug(f"{digit} in {line} at {line.index(digit)}")
                    if line.index(digit) < min_occurance:
                        min_occurance = min(min_occurance, line.index(digit))
                        first_digit = digit
                    if line.rindex(digit) >= max_occurance:
                        max_occurance = max(max_occurance, line.rindex(digit))
                        second_digit = digit
                except ValueError:
                    continue
            logger.debug(first_digit)
            logger.debug(second_digit)
            logger.debug(int(f"{digits[first_digit]}{digits[second_digit]}"))
            encoding_keys.append(int(f"{digits[first_digit]}{digits[second_digit]}"))
        return sum(encoding_keys)

    return part_two()


def day_2():
    data = download_input(2, 2023).splitlines()

    def part_one():
        max_red = 12
        max_green = 13
        max_blue = 14
        sum_of_possible_game_ids = 0
        for game in data:
            game_id = int(game.split(":")[0].replace("Game ", ""))
            subsets = game.split(":")[1].split(";")
            max_colors = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for subset in subsets:
                for cube_info in subset.split(","):
                    logger.debug(cube_info.strip())
                    number_of_cubes, color = cube_info.strip().split(" ")
                    if int(number_of_cubes) > max_colors[color]:
                        max_colors[color] = int(number_of_cubes)

            if (
                max_colors["red"] <= max_red
                and max_colors["green"] <= max_green
                and max_colors["blue"] <= max_blue
            ):
                sum_of_possible_game_ids += game_id
        return sum_of_possible_game_ids

    def part_two():
        game_powers = []
        for game in data:
            game_id = int(game.split(":")[0].replace("Game ", ""))
            subsets = game.split(":")[1].split(";")
            max_colors = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for subset in subsets:
                for cube_info in subset.split(","):
                    logger.debug(cube_info.strip())
                    number_of_cubes, color = cube_info.strip().split(" ")
                    if int(number_of_cubes) > max_colors[color]:
                        max_colors[color] = int(number_of_cubes)
            game_power = max_colors["red"] * max_colors["green"] * max_colors["blue"]
            game_powers.append(game_power)

        return sum(game_powers)

    # return part_one()
    return part_two()


if __name__ == "__main__":
    print(day_2())
