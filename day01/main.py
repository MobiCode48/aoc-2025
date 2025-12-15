import re

LIMIT = 100
FILE_NAME = "input.txt"


def parse_input(input_file: str) -> list[tuple[str, str]]:
    parsed_data: list = []
    with open(input_file) as f:
        for input in f:
            input_trimmed = input.strip("\n")
            match = re.match(r"([A-Za-z]+)(\d+)", input_trimmed)
            result = (match.group(1), match.group(2)) if match else None
            parsed_data.append(result)
    return parsed_data


def main(rotations: list[tuple[str, str]], pointer: int = 50) -> int:
    counter = 0
    for rotation in rotations:
        direction, number = rotation
        value = int(number)
        if direction == "L":
            pointer = (LIMIT + (pointer - value)) % LIMIT
        elif direction == "R":
            pointer = (LIMIT + (pointer + value)) % LIMIT

        if pointer == 0:
            counter += 1

    return counter


if __name__ == "__main__":
    input = parse_input(FILE_NAME)
    print(main(input))
