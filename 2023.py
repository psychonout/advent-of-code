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


def day_3():
    data = download_input(3, 2023).splitlines()

    logger.debug(len(data))

    def log_lines(i):
        try:
            logger.debug(f"line {i-1}: {data[i-1]}")
        except IndexError:
            pass
        logger.debug(f"line {i}: {data[i]}")
        try:
            logger.debug(f"line {i+1}: {data[i+1]}")
        except IndexError:
            pass

    def part_one():
        sum_of_part_numbers = 0
        for i, line in enumerate(data):
            # line = line.replace(".", )
            part_number = ""
            is_part_number = False

            if line[-1].isnumeric():
                log_lines(i)

            for j, char in enumerate(line):
                if char.isnumeric():
                    part_number += char
                    indices_to_check = [
                        (i - 1, j - 1),  # top left
                        (i - 1, j),  # top
                        (i - 1, j + 1),  # top right
                        (i, j - 1),  # left
                        (i, j + 1),  # right
                        (i + 1, j - 1),  # bottom left
                        (i + 1, j),  # bottom
                        (i + 1, j + 1),  # bottom right
                    ]
                    for index in indices_to_check:
                        try:
                            if (
                                data[index[0]][index[1]] != "."
                                and not data[index[0]][index[1]].isnumeric()
                            ):
                                logger.debug(
                                    f"found {data[index[0]][index[1]]} at i{index[0]}:j{index[1]}"
                                )
                                is_part_number = True
                                break
                        except IndexError:
                            pass

                if part_number != "" and (not char.isnumeric() or j == len(line) - 1):
                    if is_part_number:
                        logger.debug(f"part number: {part_number}")
                        sum_of_part_numbers += int(part_number)
                    part_number = ""
                    is_part_number = False

        return sum_of_part_numbers

    def part_two():
        parts_with_star = {}  # {star_coordinates: [part_numbers]}
        for i, line in enumerate(data):
            # line = line.replace(".", )
            part_number = ""
            star_coordinates = None

            if line[-1].isnumeric():
                log_lines(i)

            for j, char in enumerate(line):
                if char.isnumeric():
                    part_number += char
                    indices_to_check = [
                        (i - 1, j - 1),  # top left
                        (i - 1, j),  # top
                        (i - 1, j + 1),  # top right
                        (i, j - 1),  # left
                        (i, j + 1),  # right
                        (i + 1, j - 1),  # bottom left
                        (i + 1, j),  # bottom
                        (i + 1, j + 1),  # bottom right
                    ]
                    for index in indices_to_check:
                        try:
                            if data[index[0]][index[1]] == "*":
                                star_coordinates = f"{index[0]}{index[1]}"
                                if star_coordinates not in parts_with_star:
                                    parts_with_star[star_coordinates] = []
                                break
                        except IndexError:
                            pass

                if part_number != "" and (not char.isnumeric() or j == len(line) - 1):
                    if star_coordinates:
                        logger.debug(f"part number: {part_number}")
                        parts_with_star[star_coordinates].append(int(part_number))
                    part_number = ""
                    star_coordinates = None

        relevant_part_multiplications = []

        for part_numbers in parts_with_star.values():
            if len(part_numbers) == 1:
                continue

            relevant_part_multiplications.append(part_numbers[0] * part_numbers[1])
        return sum(relevant_part_multiplications)

    # return part_one()
    return part_two()


def day_4():
    data = download_input(4, 2023).splitlines()

    def part_one():
        total_points = 0
        for line in data:
            winning_numbers, card_numbers = line.split(" | ")
            winning_numbers = winning_numbers.split(": ")[1].strip()

            winning_numbers = [
                int(number.strip())
                for number in winning_numbers.split(" ")
                if number.strip() != ""
            ]
            card_numbers = [
                int(number.strip())
                for number in card_numbers.split(" ")
                if number.strip() != ""
            ]

            matched_numbers = set(winning_numbers).intersection(set(card_numbers))

            card_points = 0

            for index in range(len(matched_numbers)):
                if index == 0:
                    card_points = 1
                else:
                    card_points *= 2

            total_points += card_points
        logger.info(f"Total points: {total_points}")
        return total_points

    def part_two():
        last_card = data[-1].split(": ")[0]

        scratchcards = {}

        for line in reversed(data):
            winning_numbers, card_numbers = line.split(" | ")
            card, winning_numbers = winning_numbers.split(": ")

            winning_numbers = [
                int(number.strip())
                for number in winning_numbers.split(" ")
                if number.strip() != ""
            ]
            card_numbers = [
                int(number.strip())
                for number in card_numbers.split(" ")
                if number.strip() != ""
            ]
            matched_numbers = set(winning_numbers).intersection(set(card_numbers))
            logger.debug(f"{card} matched {matched_numbers}")

            if card not in scratchcards:
                scratchcards[card] = {
                    "copies": 1,
                    # "winning_numbers": winning_numbers,
                    # "card_numbers": card_numbers,
                    "matched_numbers": matched_numbers,
                }

        ordered_dict_keys = dict(sorted(scratchcards.items())).keys()

        for card in ordered_dict_keys:
            card_number = int(card.replace("   ", " ").replace("  ", " ").split(" ")[1])
            logger.debug(f"{card} has {scratchcards[card]['copies']} copies")
            for order, __ in enumerate(scratchcards[card]["matched_numbers"]):
                card_copy = f"Card {card_number + order+1:>3}"
                if card_copy > last_card:
                    continue
                for _ in range(scratchcards[card]["copies"]):
                    # logger.debug(f"Adding a copy of {card_copy}")
                    scratchcards[card_copy]["copies"] += 1

        # logger.debug(pformat(scratchcards))
        return sum([card["copies"] for card in scratchcards.values()])

    return part_two()
    # return part_one()


def day_5():
    data = download_input(5, 2023)
    # print(repr(data))
    data = data.split("\n\n")
    # print(repr(data))
    # logger.debug(len(data))
    # logger.debug(data)

    def map_as_dict(items):
        locations = []
        for line in items.strip().splitlines():
            # logger.debug(line)
            locations.append([int(element) for element in line.strip().split(" ")])
        return locations

    def part_one():
        maps = {}
        seeds = []
        seed_locations = []

        for line in data:
            category, items = line.split(":")
            if category == "seeds":
                seeds = [int(item.strip()) for item in items.strip().split(" ")]
            else:
                maps[category] = map_as_dict(items)

        for seed in seeds:
            floating_seed = seed
            for map_key, map_values in maps.items():
                # logger.debug(f"{map_key}")
                for location in map_values:
                    item_first, item_second, interval = location

                    # logger.debug(f"looking for {floating_seed} in {item_first}:{item_first+interval}")

                    if (
                        floating_seed >= item_second
                        and floating_seed <= item_second + interval
                    ):
                        logger.debug(
                            f"found {floating_seed} {map_key} {item_first} {item_second} {interval}"
                        )
                        logger.debug(f"{floating_seed} now")
                        offset = floating_seed - item_second
                        logger.debug(f"{offset}")
                        floating_seed = item_first + offset
                        logger.debug(f"{floating_seed} after")

                        if map_key == "humidity-to-location map":
                            seed_locations.append(floating_seed)
                        break

        return min(seed_locations)

    def part_two():
        maps = {}
        seeds = []
        seed_locations = []

        for line in data:
            category, items = line.split(":")
            if category == "seeds":
                items = items.strip().split(" ")
                items = [int(item) for item in items]
                for i in range(0, len(items), 2):
                    seeds.append(
                        (int(items[i] + (items[i + 1] / 2)), int(items[i + 1] / 2))
                    )
            else:
                maps[category] = map_as_dict(items)

        for seed in seeds:
            floating_seeds = [seed[0], seed[0] + seed[1], seed[0] - seed[1]]
            for map_key, map_values in maps.items():
                new_floating_seeds = floating_seeds
                for location in map_values:
                    item_first, item_second, interval = location
                    for index, floating_seed in enumerate(floating_seeds):
                        if (
                            floating_seed >= item_second
                            and floating_seed <= item_second + interval
                        ):
                            logger.debug(
                                f"found {floating_seed} {map_key} {item_first} {item_second} {interval}"
                            )
                            logger.debug(f"{floating_seed} now")
                            offset = floating_seed - item_second
                            logger.debug(f"{offset}")
                            floating_seed = item_first + offset
                            logger.debug(f"{floating_seed} after")
                            if index == 0:
                                new_floating_seeds.append(floating_seed)
                            elif index == 1:
                                new_floating_seeds.append(floating_seed + seed[1])
                            elif index == 2:
                                new_floating_seeds.append(floating_seed - seed[1])

                            if map_key == "humidity-to-location map":
                                seed_locations.append(floating_seed)
                            break
                    floating_seeds = new_floating_seeds

        return min(seed_locations)

    # return part_one()
    return part_two()


def day_6():
    data = download_input(5, 2023).splitlines()

    def part_one():
        pass

    def part_two():
        pass

    return part_one()
    # return part_two()


if __name__ == "__main__":
    logger.warning(day_5())
