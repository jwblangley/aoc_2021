class Cave:
    def __init__(self, uid):
        self.uid = uid
        self.neighbours = []

    def is_big_cave(self):
        return self.uid.isupper()

    def connect(self, other):
        self.neighbours.append(other)
        other.neighbours.append(self)


def count_paths_to_end(start_cave, path=None, end_cave_uid="end"):
    # N.B: Does not detect infinite loops
    if path is None:
        path = list()

    if start_cave.uid == end_cave_uid:
        return 1

    if not start_cave.is_big_cave() and start_cave.uid in path:
        return 0

    return sum(
        count_paths_to_end(nb, path=[*path, start_cave.uid], end_cave_uid=end_cave_uid)
        for nb in start_cave.neighbours
    )