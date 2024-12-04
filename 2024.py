from pprint import pformat

from loguru import logger

from common import download_input, from_file, get_input


def day_1():
    data = download_input(1, 2024).splitlines()

    def left_right_lists():
        left_side = []
        right_side = []
        for item in data:
            left, right = item.split("   ")
            left_side.append(int(left))
            right_side.append(int(right))

        return left_side, right_side

    def part_one():
        left_side, right_side = left_right_lists()

        left_side = sorted(left_side)
        right_side = sorted(right_side)

        return sum([abs(left_side[i] - right_side[i]) for i in range(len(left_side))])

    def part_two():
        left_side, right_side = left_right_lists()

        similarity_score = 0

        for number in left_side:
            similarity_score += number * right_side.count(number)

        return similarity_score

    logger.success(part_two())


def day_2():
    data = download_input(2, 2024).splitlines()

    def is_ascending(lst):
        return all(lst[i] <= lst[i + 1] and 1 <= lst[i + 1] - lst[i] <= 3 for i in range(len(lst) - 1))

    def is_descending(lst):
        return all(lst[i] >= lst[i + 1] and 1 <= lst[i] - lst[i + 1] <= 3 for i in range(len(lst) - 1))

    def part_one():
        safe_reports = 0

        for report in data:
            report = [int(number) for number in report.split(" ")]

            if is_ascending(report) or is_descending(report):
                safe_reports += 1

        return safe_reports

    def part_two():
        def is_ascending(lst):
            for i in range(len(lst)):
                temp_lst = lst[:i] + lst[i + 1 :]
                if all(
                    temp_lst[j] <= temp_lst[j + 1] and 1 <= temp_lst[j + 1] - temp_lst[j] <= 3
                    for j in range(len(temp_lst) - 1)
                ):
                    return True
            return False

        def is_descending(lst):
            for i in range(len(lst)):
                temp_lst = lst[:i] + lst[i + 1 :]
                if all(
                    temp_lst[j] >= temp_lst[j + 1] and 1 <= temp_lst[j] - temp_lst[j + 1] <= 3
                    for j in range(len(temp_lst) - 1)
                ):
                    return True
            return False

    logger.success(part_one())


def day_3():
    data = download_input(3, 2024)

    def part_one():
        lines = ["mul" + item for item in data.split("mul")]

        answer = 0

        enabled = True

        for line in lines:
            try:
                number_1, number_2 = line.split("mul(")[1].split(")")[0].split(",")
                number_1 = int(number_1)
                number_2 = int(number_2)
                if enabled:
                    answer += number_1 * number_2

            except Exception:
                pass

            if "do()" in line:
                enabled = True
            if "don't()" in line:
                enabled = False

        return answer

    def part_two():
        pass

    logger.success(part_one())


def day_4():
    data = download_input(4, 2024)

    def find_word(grid, word):
        rows = grid.splitlines()
        num_rows = len(rows)
        num_cols = len(rows[0]) if num_rows > 0 else 0
        word_len = len(word)
        count = 0

        def search_direction(x, y, dx, dy):
            for i in range(word_len):
                if not (0 <= x < num_cols and 0 <= y < num_rows) or rows[y][x] != word[i]:
                    return False
                x += dx
                y += dy
            return True

        for y in range(num_rows):
            for x in range(num_cols):
                if search_direction(x, y, 1, 0):  # Horizontal right
                    count += 1
                if search_direction(x, y, -1, 0):  # Horizontal left
                    count += 1
                if search_direction(x, y, 0, 1):  # Vertical down
                    count += 1
                if search_direction(x, y, 0, -1):  # Vertical up
                    count += 1
                if search_direction(x, y, 1, 1):  # Diagonal down-right
                    count += 1
                if search_direction(x, y, -1, -1):  # Diagonal up-left
                    count += 1
                if search_direction(x, y, 1, -1):  # Diagonal up-right
                    count += 1
                if search_direction(x, y, -1, 1):  # Diagonal down-left
                    count += 1

        return count

    def part_one():
        return find_word(data, "XMAS")

    def find_x_shape(grid):
        rows = grid.splitlines()
        num_rows = len(rows)
        num_cols = len(rows[0]) if num_rows > 0 else 0
        count = 0

        def search_x_shape(x, y):
            if x - 1 < 0 or x + 1 >= num_rows or y - 1 < 0 or y + 1 >= num_cols:
                logger.error(f"Out of bounds {x - 1} {x + 1} {y - 1} {y + 1}")
                return False

            top_left = rows[x - 1][y - 1]
            top_right = rows[x - 1][y + 1]
            bottom_left = rows[x + 1][y - 1]
            bottom_right = rows[x + 1][y + 1]

            letters = [top_left, top_right, bottom_left, bottom_right]

            if letters.count("M") == 2 and letters.count("S") == 2:
                pass
            else:
                return False

            return (
                (top_left == "M" and top_right == "M")
                or (top_right == "M" and bottom_right == "M")
                or (bottom_right == "M" and bottom_left == "M")
                or (bottom_left == "M" and top_left == "M")
            )

        for x in range(num_rows):
            for y in range(num_cols):
                if rows[x][y] == "A":
                    logger.debug(f"Found A at {x}, {y}")
                    if search_x_shape(x, y):
                        count += 1

        return count

    def part_two():
        return find_x_shape(data)

    logger.success(part_two())


if __name__ == "__main__":
    day_4()
