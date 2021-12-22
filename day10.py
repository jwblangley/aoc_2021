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
    None: 0,
}


def is_corrupt_parenthesis(string):
    stack = []
    for c in string:
        if c in parantheses.keys():
            stack.append(c)
        if c in parantheses.values():
            if len(stack) == 0 or c != parantheses[stack.pop()]:
                return c
    return None


if __name__ == "__main__":
    with open("inputs/day10_input.txt", "r") as data:
        total_score = sum(score_map[is_corrupt_parenthesis(line)] for line in data)

    print(f"Total score: {total_score}")
