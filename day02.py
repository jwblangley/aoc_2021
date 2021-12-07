import collections

Location = collections.namedtuple("Location", ["displacement", "depth"])


def parse_instructions(instructions, aiming=False):
    displacement = 0
    depth = 0
    aim = 0
    for ins in instructions:
        command, value = ins.split(" ")
        if command == "forward":
            if aiming:
                depth += aim * int(value)
            displacement += int(value)
        elif command == "down":
            if aiming:
                aim += int(value)
            else:
                depth += int(value)
        elif command == "up":
            if aiming:
                aim -= int(value)
            else:
                depth -= int(value)
        else:
            raise RuntimeError(f"Invalid command: {command}")

    return Location(displacement, depth)


if __name__ == "__main__":
    with open("inputs/day02_input.txt", "r") as data:
        loc = parse_instructions(data, aiming=False)

    print("Without aim")
    print(f"Location: {loc}")
    print(f"Result: {loc.displacement * loc.depth}\n")

    with open("inputs/day02_input.txt", "r") as data:
        loc = parse_instructions(data, aiming=True)

    print("With aim")
    print(f"Location: {loc}")
    print(f"Result: {loc.displacement * loc.depth}\n")
