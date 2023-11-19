from pprint import pprint

from common import download_input, from_file, get_input


def day_1():
    data = download_input(1, 2022)

    elf_calories = []

    for elf in data.strip().split("\n\n"):
        calories = [int(item) for item in elf.strip().split("\n") if item != ""]
        elf_calories.append(sum(calories))

    # part one
    # return max(elf_calories)

    # part two
    return sum(sorted(elf_calories)[-3:])


def day_2():
    # A,X - rock
    # B,Y - paper
    # C,Z - scissors
    # X - lose
    # Y - draw
    # Z - win

    # part one
    scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
        "AZ": 0,
        "BX": 0,
        "CY": 0,
        "AX": 3,
        "BY": 3,
        "CZ": 3,
        "AY": 6,
        "BZ": 6,
        "CX": 6,
    }

    # part two

    replacements = {
        "AX": "AZ",
        "AY": "AX",
        "AZ": "AY",
        "BX": "BX",
        "BY": "BY",
        "BZ": "BZ",
        "CX": "CY",
        "CY": "CZ",
        "CZ": "CX",
    }

    total_score = 0

    for line in get_input(2, 2022):
        pair = "".join(line.split(" "))

        # part two
        pair = replacements[pair]

        total_score = total_score + scores[pair[1]] + scores[pair]

    return total_score


def day_3():
    from string import ascii_lowercase, ascii_uppercase

    result = 0

    scores = ascii_lowercase + ascii_uppercase

    # part one
    # for line in get_input(3, 2022):
    #     firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    #     common_char = "".join(set(firstpart).intersection(set(secondpart)))
    #     result += scores.index(common_char) + 1

    # part two
    temp = []

    for index, line in enumerate(get_input(3, 2022)):
        temp.append(line)

        if index > 0 and (index + 1) % 3 == 0:
            common_char = "".join(set.intersection(*map(set, temp)))
            result += scores.index(common_char) + 1
            temp = []

    return result


def day_4():
    def get_range(string: str):
        start, finish = string.split("-")
        return range(int(start), int(finish) + 1)

    results = 0
    for line in get_input(4, 2022):
        first, second = [get_range(item) for item in line.split(",")]
        # part one
        # if not set(first).difference(set(second)) or not set(second).difference(set(first)):
        #     results += 1

        # part two
        if set(first).intersection(set(second)):
            results += 1

    return results


def day_5():
    stack, instructions = download_input(5, 2022).split("\n\n")

    stack_data = {}
    for row_no, row in enumerate(reversed(stack.split("\n"))):
        if row_no == 0:
            for col in row.split("  "):
                if col not in stack_data:
                    stack_data[int(col.strip())] = []
        else:
            for col_no, col in enumerate(range(0, len(row), 4)):
                if row[col : col + 4].strip() != "":
                    stack_data[col_no + 1].append(row[col : col + 4].strip())

    for step in instructions.split("\n"):
        if step == "":
            continue
        boxes, stacks = step.split(" from ")
        boxes = int(boxes.replace("move ", ""))
        off, on = [int(part) for part in stacks.split(" to ")]

        # part one
        # for box in range(boxes):
        #     try:
        #         stack_data[on].append(stack_data[off].pop())
        #     except Exception:
        #         pass

        # part two
        stack_data[on].extend(stack_data[off][-boxes:])
        stack_data[off] = stack_data[off][:-boxes]

    return (
        "".join([stack_data[stack][-1] for stack in stack_data])
        .replace("[", "")
        .replace("]", "")
    )


def day_6():
    for i in range(len(download_input(6, 2022))):
        # part one
        # characters = 4
        # part two
        characters = 14
        chunk = data[i : i + characters]
        if len(chunk) == len(set(chunk)):
            print(f"{i+characters}. {chunk}")
            break


# to refactor
def day_7():
    from collections import defaultdict

    path = []
    sizes = defaultdict(int)
    instructions = get_input(7, 2022)
    for line in instructions:
        words = line.strip().split()
        if words[1] == "cd":
            if words[2] == "..":
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == "ls":
            continue
        else:
            try:
                size = int(words[0])
                for i in range(len(path) + 1):
                    sizes["/".join(path[:i])] += size
            except:
                pass

    ans = 0
    best = 1e9

    print(sizes["/"])
    free_space_needed = 70000000 - 30000000
    need_to_free = sizes["/"] - free_space_needed

    for k, v in sizes.items():
        # part one
        if v <= 100000:
            ans += v
        # part two
        if v >= need_to_free:
            best = min(best, v)

    return best
    # current_path = ""
    # current_dir = ""
    # max_path = 0
    # for line in instructions.split("$ "):
    #     print(max_path)
    #     if len(current_path.split("/")) > max_path:
    #         max_path = len(current_path.split("/"))

    #     if line.startswith("cd .."):
    #         before = current_path
    #         current_path = current_path.split("/")[-1:]
    #         print(before, current_path)
    #         break

    #     elif line.startswith("cd "):
    #         if line.split(" ")[1] != "..":
    #             current_dir = line.replace("cd ", "").strip()
    #             if f"{current_path}/{current_dir}" not in directories:
    #                 current_path = f"{current_path}/{current_dir}"
    #                 directories[current_path] = []

    #     elif line.startswith("ls"):
    #         for file in line.split("\n"):
    #             if file.startswith("dir "):
    #                 directory = file.split(" ")[1].strip("\n")
    #                 if f"{current_path}/{directory}" not in directories:
    #                     current_path = f"{current_path}/{directory}"
    #                     directories[current_path] = []
    #             elif not file.startswith("ls"):
    #                 try:
    #                     file_size = int(file.split(" ")[0])
    #                 except Exception as e:
    #                     print(line, "\n", file)
    #                     continue
    #                 directories[current_path].append(file_size)
    # pprint(directories)


def day_8():
    import math

    # off youtube
    # als = 0
    # grid = [list(map(int, line)) for line in download_input(8, 2022).splitlines()]
    # pprint(grid)
    # for r in range(len(grid)):
    #     for c in range(len(grid[r])):
    #         k = grid[r][c]
    #         if (
    #             all(grid[r][x] < k for x in range(c))
    #             or all(grid[r][x] < k for x in range(c+1, len(grid[r])))
    #             or all(grid[x][c] < k for x in range(r))
    #             or all(grid[x][c] < k for x in range(r+1, len(grid)))
    #         ):
    #             als += 1
    # return als

    grid = []

    test = from_file("inputs/2022/input-8-test.txt")
    # for i, row in enumerate(test.strip().splitlines()):
    for i, row in enumerate(get_input(8, 2022)):
        grid.append([int(col) for col in row])

    result = 0

    highest_scenic_score = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            current_tree = grid[row][col]
            # if (
            #     all(grid[row][temp] < current_tree for temp in range(col))
            #     or all(
            #         grid[row][temp] < current_tree
            #         for temp in range(col + 1, len(grid[row]))
            #     )
            #     or all(grid[temp][col] < current_tree for temp in range(row))
            #     or all(
            #         grid[temp][col] < current_tree for temp in range(row + 1, len(grid))
            #     )
            # ):
            #     result += 1
            scores = [0, 0, 0, 0]
            for temp in range(col - 1, -1, -1):
                scores[0] += 1
                if grid[row][temp] >= current_tree:
                    break

            for temp in range(col + 1, len(grid[row])):
                scores[1] += 1
                if grid[row][temp] >= current_tree:
                    break

            for temp in range(row - 1, -1, -1):
                scores[2] += 1
                if grid[temp][col] >= current_tree:
                    break

            for temp in range(row + 1, len(grid)):
                scores[3] += 1
                if grid[temp][col] >= current_tree:
                    break

            scenic_score = math.prod(scores)

            print(scores)

            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    return highest_scenic_score


def day_9():
    def adjust(H, T):
        dr = H[0] - T[0]
        dc = H[1] - T[1]

        if abs(dr) <= 1 and abs(dc) <= 1:
            pass

        elif abs(dr) >= 2 and abs(dc) >= 2:
            T = (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1] - 1 if T[1] < H[1] else H[1] + 1)

        elif abs(dr) >= 2:
            T = (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1])

        elif abs(dc) >= 2:
            T = (H[0], H[1] - 1 if T[1] < H[1] else H[1] + 1)

        return T

    H = (0, 0)
    T = [(0, 0) for _ in range(9)]
    DR = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
    DC = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
    P1 = set([T[0]])
    P2 = set([T[8]])

    for line in get_input(9, 2022):
        direction, amount = line.split()
        amount = int(amount)

        for _ in range(amount):
            H = (H[0] + DR[direction], H[1] + DC[direction])
            T[0] = adjust(H, T[0])
            for i in range(1, 9):
                T[i] = adjust(T[i - 1], T[i])
            P1.add(T[0])
            P2.add(T[8])

    print(len(P1))
    print(len(P2))
    return None


def day_10():
    cycle = 0
    X = 1

    screen = ["." for col in range(40*6)]

    def display_screen():
        display = [screen[i:i+39] for i in range(0, len(screen), 40)]
        display = "\n".join(["".join(col) for col in display])

        print(display)

    signals = {
        20: 0,
        60: 0,
        100: 0,
        140: 0,
        180: 0,
        220: 0,
    }


    def increment_cycle(cycle: int, X: int) -> int:
        screen[cycle] = "#" if cycle % 40 in [X, X+1, X-1] else "."

        cycle += 1

        if cycle in signals:
            signals[cycle] = cycle * X

        return cycle



    for line in get_input(10, 2022):
        if line == "noop":
            cycle = increment_cycle(cycle, X)
            continue

        for i in range(2):
            cycle = increment_cycle(cycle, X)
        reg, count = line.split(" ")
        count = int(count)
        X += count

    # part two
    display_screen()

    return sum(signals.values())


def day_11():
    from operator import add, mul, sub, truediv
    class Monkey:
        ops = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": truediv,
        }
        
        def __init__(self, mid: int, start_items: int, operation: str, factor: str | int):
            self.id = mid
            self.start_items = start_items
            self.operation = self.ops[operation]

    for monkey_data in download_input(11, 2022).split("\n\n"):
        print(monkey_data)
        break


def day_13():
    def compare_items(item_1, item_2):
        if type(item_1) != type(item_2):
            if type(item_1) != list:
                return compare_items([item_1], item_2)
            if type(item_2) != list:
                return compare_items(item_1, [item_2])

        print(item_1, len(item_1))
        print(item_2, len(item_2))
        print(item_1 < item_2)
        return item_1 < item_2

    sum_of_indices = 0

    for indice, signal_pair in enumerate(download_input(13, 2022).split("\n\n")):
        first_signal, second_signal = [eval(item) for item in signal_pair.split("\n")]
        print(len(first_signal))
        print(first_signal[0])
        print(len(second_signal))
        print(second_signal[0])

        result = compare_items(first_signal, second_signal)
        if result:
            sum_of_indices += (indice + 1)

    return sum_of_indices

print(day_13())
