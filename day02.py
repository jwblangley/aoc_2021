import collections

Location = collections.namedtuple("Location", ["displacement", "depth"])


def parse_instructions(ins):
    displacement = 0
    depth = 0

    return Location(displacement, depth)
