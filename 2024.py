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
        return all(
            lst[i] <= lst[i + 1] and 1 <= lst[i + 1] - lst[i] <= 3
            for i in range(len(lst) - 1)
        )

    def is_descending(lst):
        return all(
            lst[i] >= lst[i + 1] and 1 <= lst[i] - lst[i + 1] <= 3
            for i in range(len(lst) - 1)
        )

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
                    temp_lst[j] <= temp_lst[j + 1]
                    and 1 <= temp_lst[j + 1] - temp_lst[j] <= 3
                    for j in range(len(temp_lst) - 1)
                ):
                    return True
            return False

        def is_descending(lst):
            for i in range(len(lst)):
                temp_lst = lst[:i] + lst[i + 1 :]
                if all(
                    temp_lst[j] >= temp_lst[j + 1]
                    and 1 <= temp_lst[j] - temp_lst[j + 1] <= 3
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


if __name__ == "__main__":
    day_3()
