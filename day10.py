parantheses = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
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
