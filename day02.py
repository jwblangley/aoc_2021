import collections

Location = collections.namedtuple("Location", ["displacement", "depth"])


def parse_instructions(instructions):
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
