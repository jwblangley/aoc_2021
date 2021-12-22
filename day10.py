from functools import reduce

parantheses = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

corrupt_score_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

autocomplete_score_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def is_valid_parantheses(string):
    stack = []
    for c in string:
        if c in parantheses.keys():
            stack.append(parantheses[c])
        if c in parantheses.values():
            if len(stack) == 0 or c != stack.pop():
                return c
    return stack


if __name__ == "__main__":
    # PART 1
    with open("inputs/day10_input.txt", "r") as data:
        total_score = sum(
            corrupt_score_map[is_valid_parantheses(line)]
            for line in data
            if not isinstance(is_valid_parantheses(line), list)
        )

    print(f"Total corruption score: {total_score}")

    # PART 2
    with open("inputs/day10_input.txt", "r") as data:
        scores = [
            reduce(
                lambda prev, curr: prev * 5 + autocomplete_score_map[curr],
                reversed(is_valid_parantheses(line)),
                0,
            )
            for line in data
            if isinstance(is_valid_parantheses(line), list)
        ]

    median_score = sorted(scores)[len(scores) // 2]
    print(f"Median autocomplete score: {median_score}")
