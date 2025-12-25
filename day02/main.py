FILE_NAME = "input.txt"


def parse_file(filename: str) -> list[tuple[int, int]]:
    lst = []
    with open(filename, "r") as f:
        for line in f.readlines():
            ranges = line.split(",")
            for val in ranges:
                firstID = int(val.split("-")[0])
                lastID = int(val.split("-")[1])
                lst.append((firstID, lastID))
    return lst


def part1(ranges: list[tuple[int, int]]) -> int:
    invalid_ids = []
    for values in ranges:
        firstID, lastID = values
        for val in range(firstID, lastID + 1):
            val_str = str(val)
            middle = len(val_str) // 2
            if len(val_str) % 2 != 0:
                continue
            first_part = val_str[:middle]
            second_part = val_str[middle:]
            if first_part == second_part:
                invalid_ids.append(val)
    return sum(invalid_ids)


def part2(ranges: list[tuple[int, int]]) -> int:
    invalid_ids = []
    for values in ranges:
        firstID, lastID = values
        for val in range(firstID, lastID + 1):
            val_str = str(val)
            is_invalid = False
            maxChunks = len(val_str) // 2
            for chunk_size in range(1, maxChunks + 1):
                chunks = [
                    val_str[i : i + chunk_size]
                    for i in range(0, len(val_str), chunk_size)
                ]
                if len(val_str) % chunk_size == 0 and all(
                    chunk == chunks[0] for chunk in chunks
                ):
                    # if the pattern has been found we break
                    is_invalid = True
                    break
            if is_invalid:
                invalid_ids.append(val)
    return sum(invalid_ids)


def main(filename: str) -> int:
    return part2(parse_file(filename))


if __name__ == "__main__":
    print(main(FILE_NAME))
