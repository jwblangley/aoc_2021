class Cave:
    def __init__(self, uid):
        self.uid = uid
        self.neighbours = []

    def is_big_cave(self):
        return self.uid.isupper()

    def connect(self, other):
        self.neighbours.append(other)
        other.neighbours.append(self)


def count_paths_to_end(
    start_cave,
    path=None,
    end_cave_uid="end",
    single_small_cave_double_visit=False,
    has_double_visit=False,
):
    # N.B: Does not detect infinite loops
    if path is None:
        path = list()

    if start_cave.uid == end_cave_uid:
        return 1

    if single_small_cave_double_visit:
        if has_double_visit and not start_cave.is_big_cave() and start_cave.uid in path:
            return 0
    else:
        if not start_cave.is_big_cave() and start_cave.uid in path:
            return 0

    if (
        single_small_cave_double_visit
        and not start_cave.is_big_cave()
        and start_cave.uid in path
    ):
        if start_cave.uid == "start":
            return 0
        has_double_visit = True

    return sum(
        count_paths_to_end(
            nb,
            path=[*path, start_cave.uid],
            end_cave_uid=end_cave_uid,
            single_small_cave_double_visit=single_small_cave_double_visit,
            has_double_visit=has_double_visit,
        )
        for nb in start_cave.neighbours
    )


if __name__ == "__main__":
    all_caves = {}

    with open("inputs/day12_input.txt", "r") as data:
        for line in data:
            uid_a, uid_b = line.strip().split("-")

            if uid_a in all_caves.keys():
                cave_a = all_caves[uid_a]
            else:
                cave_a = Cave(uid_a)
                all_caves[uid_a] = cave_a

            if uid_b in all_caves.keys():
                cave_b = all_caves[uid_b]
            else:
                cave_b = Cave(uid_b)
                all_caves[uid_b] = cave_b

            cave_a.connect(cave_b)

    num_routes = count_paths_to_end(all_caves["start"])
    print(f"Number of paths: {num_routes}")

    num_routes = count_paths_to_end(
        all_caves["start"], single_small_cave_double_visit=True
    )
    print(f"Number of paths with single small cave double visit: {num_routes}")
