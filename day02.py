import collections

Location = collections.namedtuple("Location", ["displacement", "depth"])


def parse_instructions(instructions, aim=False):
    displacement = 0
    depth = 0
    for ins in instructions:
        command, value = ins.split(" ")
        if command == "forward":
            displacement += int(value)
        elif command == "down":
            depth += int(value)
        elif command == "up":
            depth -= int(value)
        else:
            raise RuntimeError(f"Invalid command: {command}")

    return Location(displacement, depth)


if __name__ == "__main__":
    with open("inputs/day02_input.txt", "r") as data:
        loc = parse_instructions(data, aim=False)

    print("Without aim")
    print(f"Location: {loc}")
    print(f"Result: {loc.displacement * loc.depth}\n")
