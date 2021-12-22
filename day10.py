parantheses = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

score_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
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
    with open("inputs/day10_input.txt", "r") as data:
        total_score = sum(
            score_map[is_valid_parantheses(line)]
            for line in data
            if not isinstance(is_valid_parantheses(line), list)
        )

    print(f"Total score: {total_score}")
