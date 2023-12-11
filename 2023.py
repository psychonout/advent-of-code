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
    data = data.split("\n\n")
    maps = {}
    seeds = []

    def map_as_dict(items):
        locations = []
        for line in items.strip().splitlines():
            range_line = [int(element) for element in line.strip().split(" ")]
            range_line[-1] = range_line[-1] - 1
            locations.append(tuple(range_line))
        return locations

    for line in data:
        category, items = line.split(":")
        if category == "seeds":
            seeds = [int(item.strip()) for item in items.strip().split(" ")]
        else:
            maps[category] = map_as_dict(items)

    logger.debug(seeds)
    logger.debug(maps)

    def part_one():
        seed_locations = []

        for seed in seeds:
            floating_seed = seed
            for map_key, map_values in maps.items():
                logger.debug(f"looking {floating_seed} {map_key}")
                for target, source, interval in map_values:
                    if floating_seed > source and floating_seed <= source + interval:
                        offset = floating_seed - source
                        floating_seed = target + offset
                        break

                if "humidity-to-location" in map_key:
                    seed_locations.append(floating_seed)

        return min(seed_locations)

    def part_two():
        seed_locations = []
        seed_pairs = [
            (seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)
        ]

        for seed in seed_pairs:
            current_stage = [seed]
            logger.debug(f"{current_stage}")
            next_stage = []

            for map_key, map_values in maps.items():
                # logger.debug(map_key)
                while current_stage:
                    # using while because floating point works as a queue
                    first_seed, last_seed = current_stage.pop()
                    for location in map_values:
                        target, source, interval = location
                        if last_seed < source or source + interval <= first_seed:
                            # no overlap of ranges
                            continue
                        elif source <= first_seed <= last_seed < source + interval:
                            # the whole range of seeds fits inside the source range
                            offset = first_seed - source
                            next_stage.append(
                                (
                                    target + offset,
                                    target + offset + last_seed - first_seed,
                                )
                            )
                            break
                        elif first_seed < source <= last_seed < source + interval:
                            #  some part of lower seeds don't fit into the source range
                            offset = last_seed - source
                            next_stage.append((target, target + offset))
                            current_stage.append((first_seed, source - 1))
                            break
                        elif source <= first_seed < source + interval <= last_seed:
                            # some of the upper seeds go beyond the source range
                            offset = first_seed - source
                            next_stage.append((target + offset, target + interval))
                            current_stage.append((source + interval, last_seed))
                            break
                        elif first_seed < source <= source + interval <= last_seed:
                            # whole range of source fits inside seed range
                            next_stage.append((target, target + interval))
                            current_stage.append((first_seed, source - 1))
                            current_stage.append((source + interval, last_seed))
                            break
                    else:
                        next_stage.append((first_seed, last_seed))
                current_stage = next_stage
                next_stage = []

            seed_locations.extend(current_stage)

        return min(i[0] for i in seed_locations)

    # return part_one()
    return part_two()


def day_6():
    data = download_input(6, 2023, test=False).splitlines()

    def part_one():
        numbers_of_ways_to_win = []

        times = [int(time.strip()) for time in data[0].split(":")[1].strip().split()]
        distances = [
            int(distance.strip()) for distance in data[1].split(":")[1].strip().split()
        ]

        for index, time in enumerate(times):
            # total time to spare
            # 1 unit of time  to spare increases boat speed by one per the rest of units
            number_of_ways_to_win = 0
            for second in range(time):
                distance = second * (time - second)
                if distance > distances[index]:
                    number_of_ways_to_win += 1
            numbers_of_ways_to_win.append(number_of_ways_to_win)

        result = 1
        for x in numbers_of_ways_to_win:
            result = result * x
        return result

    def part_two():
        time = int(data[0].split(":")[1].replace(" ", ""))
        distance = int(data[1].split(":")[1].replace(" ", ""))
        logger.info(time)
        logger.info(distance)
        # total time to spare
        # 1 unit of time  to spare increases boat speed by one per the rest of units
        number_of_ways_to_win = 0
        for second in range(time):
            # logger.debug(second)
            race_distance = second * (time - second)
            # logger.debug(distance)
            if race_distance > distance:
                number_of_ways_to_win += 1

        return number_of_ways_to_win

    # return part_one()
    return part_two()


def day_7():
    data = download_input(7, 2023, test=False).splitlines()

    def card_strength(card: str, use_joker=False) -> int:
        all_cards = "23456789TJQKA"
        if use_joker:
            all_cards = "J" + all_cards.replace("J", "")
        return all_cards.index(card)

    def get_suite(cards: str, use_joker=False) -> int:
        all_cards = "23456789TJQKA"
        possible_suites = []

        for card in all_cards:
            temp = cards
            if use_joker:
                temp = cards.replace("J", card)
            # five of a kind
            if len(set(temp)) == 1:
                possible_suites.append(7)

            # four of a kind or full house
            if len(set(temp)) == 2:
                for symbol in set(temp):
                    if temp.count(symbol) == 4:
                        possible_suites.append(6)
                    if temp.count(symbol) == 3:
                        possible_suites.append(5)

            # three of a kind or two pair
            if len(set(temp)) == 3:
                for symbol in set(temp):
                    if temp.count(symbol) == 3:
                        possible_suites.append(4)
                    if temp.count(symbol) == 2:
                        possible_suites.append(3)

            # one pair
            if len(set(temp)) == 4:
                possible_suites.append(2)

            # high card
            if len(set(temp)) == 5:
                possible_suites.append(1)

        return max(possible_suites)

    def part_one():
        card_scores = []
        for line in data:
            cards, bid = line.split()
            card_suite = get_suite(cards)

            card_strengths = [card_strength(card) for card in cards]

            card_scores.append([card_suite, card_strengths, bid, cards])

        logger.info(pformat(card_scores))

        card_scores = sorted(card_scores, key=lambda x: (x[0], x[1]))
        logger.info(pformat(card_scores))
        scores = []
        for multiplyer, card in enumerate(card_scores):
            scores.append(int(card[2]) * (multiplyer + 1))
        return sum(scores)

    def part_two():
        card_scores = []
        for line in data:
            cards, bid = line.split()
            card_suite = get_suite(cards, use_joker=True)

            card_strengths = [card_strength(card, use_joker=True) for card in cards]

            card_scores.append([card_suite, card_strengths, bid, cards])

        logger.info(pformat(card_scores))

        card_scores = sorted(card_scores, key=lambda x: (x[0], x[1]))
        logger.info(pformat(card_scores))
        scores = []
        for multiplier, card in enumerate(card_scores):
            scores.append(int(card[2]) * (multiplier + 1))
        return sum(scores)

    # return part_one()
    return part_two()


def day_8():
    data = download_input(8, 2023, test=False).splitlines()

    def part_one():
        directions = data[0]
        tunnels = data[2:]

        paths = {}

        for tunnel in tunnels:
            key, values = tunnel.split(" = ")
            left, right = values.split(", ")
            if key in paths:
                logger.info(f"key {key} already in paths")

            paths[key] = [left.replace("(", "").strip(), right.replace(")", "").strip()]

        paths = dict(sorted(paths.items(), key=lambda x: x[0]))

        current_path = "AAA"
        next_path = ""
        count_steps = 0

        while current_path != "ZZZ":
            for direction in directions:
                if current_path == "ZZZ":
                    logger.info("Reached the end")
                    break
                match direction:
                    case "L":
                        next_path = paths[current_path][0]
                        count_steps += 1
                    case "R":
                        next_path = paths[current_path][1]
                        count_steps += 1
                    case _:
                        raise ValueError(f"Unknown direction {direction}")

                logger.info(
                    f"current path: {current_path} direction: {direction} next_path: {next_path}"
                )

                current_path = next_path

        return count_steps

    from typing import Iterator

    def parse_input(lines: list[str]) -> tuple[str, list]:
        instructions = lines[0]
        lines = lines[2:]
        nodes = {}
        for line in lines:
            node_id, neighbors = line.split(" = ")
            neighbors = neighbors[1:-1].split(", ")
            nodes[node_id] = tuple(neighbors)
        return instructions, nodes

    import math

    def lcm(numbers: list[int]) -> int:
        if len(numbers) == 2:
            return numbers[0] * numbers[1] // math.gcd(numbers[0], numbers[1])
        return lcm([numbers[0], lcm(numbers[1:])])

    import itertools

    def find_cycle(instructions: str, nodes: list, start: str) -> int:
        step1 = start
        step2 = start
        input_period = len(instructions)
        instructions1 = itertools.cycle(instructions)
        instructions2 = itertools.cycle(instructions)
        print()
        for i, instruction1 in enumerate(instructions1, start=1):
            step1 = nodes[step1][instruction1 == "R"]
            step2 = nodes[step2][next(instructions2) == "R"]
            if step1 == step2 and i % input_period == (i * 2) % input_period:
                logger.info(f"Found cycle of length {i}")
                return i

    def part_two():
        directions = data[0]
        tunnels = data[2:]

        paths = {}

        for tunnel in tunnels:
            key, values = tunnel.split(" = ")
            left, right = values.split(", ")
            if key in paths:
                logger.info(f"key {key} already in paths")

            paths[key] = [left.replace("(", "").strip(), right.replace(")", "").strip()]

        paths = dict(sorted(paths.items(), key=lambda x: x[0]))

        directions, nodes = parse_input(data)
        logger.info(nodes)
        periods = [find_cycle(directions, nodes, ghost) for ghost in paths]
        return lcm(periods)
        # count_steps = 0
        # time_to_stop = False

        # while not time_to_stop:
        #     for direction in directions:
        #         for node in nodes:
        #             if node[-1] != "Z":
        #                 break
        #         else:
        #             logger.info("Reached the end")
        #             time_to_stop = True
        #             break

        #         count_steps += 1
        #         next_steps = []

        #         for node in nodes:
        #             if direction == "L":
        #                 next_step = paths[node][0]

        #             elif direction == "R":
        #                 next_step = paths[node][1]

        #             next_steps.append(next_step)

        #             # logger.info(
        #             #     f"current: {node} direction: {direction} next_path: {next_step}"
        #             # )

        #         nodes = next_steps

        # return count_steps

    # return part_one()
    return part_two()


def day_9():
    data = download_input(9, 2023, test=False).splitlines()

    def get_difference(a: int, b: int) -> int:
        return a - b

    def part_one():
        score = 0
        for sequence in data:
            sequence = [int(sq) for sq in sequence.split(" ")]
            logger.error(sequence)
            sequence_resolved = False

            next_sequence = []
            sequences = [sequence]

            while not sequence_resolved:
                for i in range(len(sequence) - 1):
                    next_sequence.append(get_difference(sequence[i + 1], sequence[i]))

                sequence = next_sequence
                next_sequence = []
                sequences.append(sequence)

                logger.warning(sequence)

                if len(set(sequence)) == 1 and sequence[0] == 0:
                    sequence_resolved = True
                    value_to_add = sequence[-1]
                    logger.info(f"Value to add: {value_to_add}")
                    logger.info(f"Sequences before: {sequences}")
                    for j in range(len(sequences) - 1, -1, -1):
                        if value_to_add == 0:
                            sequences[j].append(sequences[j][-1])
                        else:
                            sequences[j].append(sequences[j][-1] + value_to_add)
                        value_to_add = sequences[j][-1]
                        if j == 0:
                            score += value_to_add
                    logger.success(f"Sequences after: {sequences}")
        return score

    def part_two():
        score = 0
        for sequence in data:
            sequence = [int(sq) for sq in sequence.split(" ")]
            logger.error(sequence)
            sequence_resolved = False

            next_sequence = []
            sequences = [sequence]

            while not sequence_resolved:
                for i in range(len(sequence) - 1):
                    next_sequence.append(get_difference(sequence[i + 1], sequence[i]))

                sequence = next_sequence
                next_sequence = []
                sequences.append(sequence)

                logger.warning(sequence)

                if len(set(sequence)) == 1 and sequence[0] == 0:
                    sequence_resolved = True
                    value_to_add = sequence[0] * -1
                    logger.info(f"Value to add: {value_to_add}")
                    logger.info(f"Sequences before: {sequences}")
                    for j in range(len(sequences) - 1, -1, -1):
                        if value_to_add == 0:
                            sequences[j].insert(0, sequences[j][0])
                        else:
                            sequences[j].insert(0, sequences[j][0] + value_to_add)
                        value_to_add = sequences[j][0] * -1
                        if j == 0:
                            score += value_to_add * -1
                    logger.success(f"Sequences after: {sequences}")
        return score

    return part_two()


def day_10():
    data = download_input(10, 2023, test=True).splitlines()

    class TileException(Exception):
        pass

    class Tile:
        def __init__(self, x: int, y: int, map: list[list[str]]) -> None:
            self.x = x
            self.y = y
            self.tile = list[x][y]
            self.direction = ""  # "up", "down", "left", "right"
            self.distance = 0

        def next_cell_at(self) -> tuple[int, int]:
            match self.tile:
                case "|":
                    if self.direction == "up":
                        return self.x, self.y - 1
                    if self.direction == "down":
                        return self.x, self.y + 1

                    raise TileException
                case "-":
                    if self.direction == "left":
                        return self.x - 1, self.y
                    if self.direction == "right":
                        return self.x + 1, self.y
                    raise TileException
                case "L":
                    if self.direction == "left":
                        return self.x, self.y + 1
                    if self.direction == "right":
                        return self.x + 1, self.y
                case "J":
                    if self.direction == "up":
                        return self.x, self.y - 1
                    if self.direction == "down":
                        return self.x - 1, self.y
                case "7":
                    if self.direction == "left":
                        return self.x, self.y + 1
                    if self.direction == "down":
                        return self.x - 1, self.y
                case "F":
                    if self.direction == "up":
                        return self.x + 1, self.y
                    if self.direction == "down":
                        return self.x, self.y + 1

        @classmethod
        def get_tile_at(cls, x: int, y: int, map: list[list[str]]) -> str:
            return map[x][y]

    def map_as_tiles():
        array = [list(line.strip()) for line in data.strip().splitlines()]
        tiles = []
        for i, row in enumerate(array):
            for j, value in enumerate(row):
                tiles.append(Tile(i, j, array)) 
        return tiles

    def part_one():
        pass

    def part_two():
        pass

    return part_one()
    # return part_two()


if __name__ == "__main__":
    logger.warning(day_9())
