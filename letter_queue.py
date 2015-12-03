# kpbochenek@gmail.com

def letter_queue(commands):
    stack = []
    for c in commands:
        if c.startswith("PUSH"):
            stack.append(c[5:])
        elif stack:
            stack = stack[1:]
    print(str(stack))
    return "".join(stack)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(("PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T")) == "DOT", "dot example"
    assert letter_queue(("POP", "POP")) == "", "Pop, Pop, empty"
    assert letter_queue(("PUSH H", "PUSH I")) == "HI", "Hi!"
    assert letter_queue(()) == "", "Nothing"
