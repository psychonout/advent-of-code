import functools
import re
from pprint import pprint

from common import download_input, get_input


def day_1():
    floor = 0
    for position, character in enumerate(get_input(day=1, year=2015)):
        if character == "(":
            floor += 1
        elif character == ")":
            floor -= 1
        # part two
        if floor == -1:
            return position
    return floor


def day_2():
    def paper_for_gift(l: int, w: int, h: int):
        return min(l * w, w * h, h * l) + (2 * l * w) + (2 * w * h) + (2 * h * l)

    def ribbon_for_gift(l: int, w: int, h: int):
        return min(2 * (l + w), 2 * (w + h), 2 * (h + l)) + w * h * l

    paper_area = 0
    # part two
    ribbon_length = 0

    for line in get_input(day=2, year=2015):
        l, w, h = [int(dim) for dim in line.split("x")]

        paper_area += paper_for_gift(l, w, h)
        ribbon_length += ribbon_for_gift(l, w, h)

    return paper_area, ribbon_length


def day_3():
    def result_key(coords):
        return f"{coords[0]}, {coords[1]}"

    # part one is having only one santa going over all inputs
    santa_coordinates = [[0, 0], [0, 0]]

    results = {}

    for index, symbol in enumerate(get_input(day=3, year=2015)):
        santa_positions = [
            result_key(santa_coordinates[0]),
            result_key(santa_coordinates[1]),
        ]

        for position in santa_positions:
            if position not in results:
                results["position"] = 1
            else:
                results[position] += 1

        current_santa = index % 2

        if symbol == "^":
            santa_coordinates[current_santa][1] += 1
        elif symbol == ">":
            santa_coordinates[current_santa][0] += 1
        elif symbol == "v":
            santa_coordinates[current_santa][1] -= 1
        elif symbol == "<":
            santa_coordinates[current_santa][0] -= 1

    return len(results)


def day_4():
    import hashlib

    input_str = "bgvyzdsv"
    result = ""
    number = 0

    # part one
    # while not result.startswith("00000"):
    # part two
    while not result.startswith("000000"):
        number += 1
        data = f"{input_str}{number}"
        result = hashlib.md5(data.encode()).hexdigest()

    return result, number


def day_5():
    from string import ascii_lowercase as letters

    def part1():
        rule_1 = ["a", "e", "i", "o", "u"]
        rule_2 = [f"{letter}{letter}" for letter in letters]
        rule_3 = ["ab", "cd", "pq", "xy"]

        nice_strings = []

        for line in get_input(day=5, year=2015):
            if (
                sum([line.count(letter) for letter in rule_1]) >= 3
                and len([match for match in rule_2 if match in line]) >= 1
                and len([match for match in rule_3 if match not in line]) == 4
            ):
                nice_strings.append(line)

        return len(nice_strings)

    def part2():
        nice_strings = []
        for line in get_input(day=5, year=2015):
            first_rule = False

            for first_pair in range(len(line) - 1):
                if first_rule:
                    break
                for second_pair in range(first_pair + 2, len(line) - 1):
                    if first_rule:
                        break
                    if (
                        line[first_pair : first_pair + 2]
                        == line[second_pair : second_pair + 2]
                    ):
                        first_rule = True
            else:
                continue

            for third_pair in range(len(line) - 2):
                chunk = line[third_pair : third_pair + 3]
                if chunk[0] == chunk[-1] and chunk[0] != chunk[1]:
                    print(f"Found a nice string: {line}")
                    nice_strings.append(line)
                    break

        return nice_strings

    return len(part2())


def day_6():
    matrix = [[0 for col in range(1000)] for row in range(1000)]

    # print(matrix)
    # print(len(matrix))
    # print(len(matrix[0]))

    for index, line in enumerate(get_input(day=6, year=2015)):
        line_data = line.replace("toggle", "toggle toggle").split(" ")
        if not line_data:
            continue
        action = " ".join(line_data[0:2])
        start_coords = line_data[2].split(",")
        stop_coords = line_data[-1].split(",")

        for row in range(int(start_coords[0]), int(stop_coords[0]) + 1):
            for col in range(int(start_coords[1]), int(stop_coords[1]) + 1):
                # part one
                # if action == "turn on":
                #     matrix[row][col] = 1
                # elif action == "turn off":
                #     matrix[row][col] = 0
                # elif action == "toggle toggle":
                #     matrix[row][col] = (matrix[row][col] + 1) % 2
                # part two
                if action == "turn on":
                    matrix[row][col] += 1
                elif action == "turn off" and matrix[row][col] != 0:
                    matrix[row][col] -= 1
                elif action == "toggle toggle":
                    matrix[row][col] += 2

    result = 0

    for row in matrix:
        for col in row:
            result += col

    return result


def day_7():
    b = 1674
    c = 0
    t = c << 1
    v = b >> 1
    f = b >> 5
    d = b >> 2
    e = b >> 3
    g = e | f
    h = e & f
    i = ~h
    j = g & i
    k = d | j
    l = d & j
    m = ~l
    n = k & m
    o = b | n
    p = b & n
    q = ~p
    r = o & q
    s = 1 & r

    addresses = {
        "b": b,
        "c": c,
        "d": d,
        "e": e,
        "f": f,
        "g": g,
        "h": h,
        "i": i,
        "j": j,
        "k": k,
        "l": l,
        "m": m,
        "t": t,
        "v": v,
        "n": n,
        "o": o,
        "p": p,
        "q": q,
        "r": r,
        "s": s,
    }

    used_instructions = [
        "0 -> c",
        "1674 -> b",
        "c LSHIFT 1 -> t",
        "b RSHIFT 1 -> v",
        "b RSHIFT 5 -> f",
        "b RSHIFT 2 -> d",
        "b RSHIFT 3 -> e",
        "e OR f -> g",
        "e AND f -> h",
        "NOT h -> i",
        "g AND i -> j",
        "d OR j -> k",
        "d AND j -> l",
        "k AND m -> n",
        "b OR n -> o",
        "b AND n -> p",
        "NOT l -> m",
        "NOT p -> q",
        "o AND q -> r",
        "1 AND r -> s",
    ]

    instructions = sorted([line for line in get_input(7, 2015)])

    addresses = {}
    iteration = 0

    while instructions:
        iteration += 1
        print(f"{iteration}. Number of instructions: {len(instructions)} Number of addresses: {len(addresses)}")

        used_instructions = []
        for line in instructions:
            ld = line.split(" ")

            # regular assignments + lx -> a
            if len(ld) == 3:
                try:
                    addresses[ld[-1]] = int(ld[0])
                    # part two
                    if ld[-1] == "b":
                        addresses[ld[-1]] = 46065
                    used_instructions.append(line)
                except Exception:
                    if ld[0] in addresses:
                        addresses[ld[-1]] = addresses[ld[0]]
                        used_instructions.append(line)
            # NOT operations
            elif len(ld) == 4:
                if ld[1] in addresses:
                    addresses[ld[-1]] = ~addresses[ld[1]]
                    used_instructions.append(line)
            # all other operations
            elif len(ld) == 5:
                first_int, second_int = None, None
                try:
                    first_int = int(ld[0])
                except Exception:
                    pass

                try:
                    second_int = int(ld[2])
                except Exception:
                    pass

                if ld[1] in ["LSHIFT", "RSHIFT"] and ld[0] in addresses:
                    if ld[1] == "LSHIFT":
                        addresses[ld[-1]] = addresses[ld[0]] << int(ld[2])
                    elif ld[1] == "RSHIFT":
                        addresses[ld[-1]] = addresses[ld[0]] >> int(ld[2])
                    used_instructions.append(line)
                elif ld[1] in ["AND", "OR"] and ld[0] in addresses and ld[2] in addresses:
                    if ld[1] == "AND":
                        addresses[ld[-1]] = addresses[ld[0]] & addresses[ld[2]]
                    elif ld[1] == "OR":
                        addresses[ld[-1]] = addresses[ld[0]] | addresses[ld[2]]
                    used_instructions.append(line)
                elif ld[1] in ["AND", "OR"] and first_int or second_int:
                    if first_int and ld[2] in addresses:
                        if ld[1] == "AND":
                            addresses[ld[-1]] = first_int & addresses[ld[2]]
                        elif ld[1] == "OR":
                            addresses[ld[-1]] = first_int | addresses[ld[2]]
                        used_instructions.append(line)
                    elif second_int and ld[0] in addresses:
                        if ld[1] == "AND":
                            addresses[ld[-1]] = addresses[ld[0]] & second_int
                        elif ld[1] == "OR":
                            addresses[ld[-1]] = addresses[ld[2]] | second_int 
                        used_instructions.append(line)
                else:
                    print(ld)

        pprint(addresses)

        instructions = set(instructions).difference(set(used_instructions))


        # for address in addresses:
        #     if address in ld and line not in used_instructions:
        #         print(line)


def day_8():
    result = 0

    for line in get_input(8, 2015):
        # part one
        # result += len(line) - len(eval(line))
        # part two
        result += line.count('\\') + line.count('"') + 2

    return result


if __name__ == "__main__":
    print(day_8())
