#kpbochenek@gmail.com
def find_message(text):
    return "".join(filter(lambda x: 'A' <= x <= 'Z', text))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

    print("Earn cool rewards by using the 'Check' button!")
