"""DAY1_Part1"""

from pathlib import Path


def check_change(numbers: list[str]) -> bool:
    """Check if the numbers are thing."""
    max_change = 3
    for index, number in enumerate(numbers, start=1):
        if index >= len(numbers):
            break
        change = number - numbers[index]
        if change <= 0 or change > max_change:
            return False

    return True


def check_change_all(numbers: list[int]) -> bool:
    """Check if the numbers are thing."""
    output = check_change(numbers)

    if output:
        return output

    output = any(check_change(numbers[:i] + numbers[i + 1 :]) for i in range(len(numbers)))

    if output:
        return output

    numbers.reverse()

    return any(check_change(numbers[:i] + numbers[i + 1 :]) for i in range(len(numbers)))


def check_report(report: str) -> bool:
    """Check if the report is valid."""
    report = [int(numbers) for numbers in report.split()]

    direction = report[0] - report[1]
    report = report[::-1] if direction < 0 else report

    output = check_change_all(report)
    print(f"{output=}")
    return output


def main() -> None:
    """Main function to read input file and calculate the sum of numbers in each line."""
    input_file = Path("./advent_of_code/2024/day02.txt")
    input_data = input_file.read_text().splitlines()

    output = sum(check_report(report) for report in input_data)
    print(output)


if __name__ == "__main__":
    main()
