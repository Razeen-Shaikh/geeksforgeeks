def print_fun(string1, string2):
    """
    Concatenates two input strings and prints the result.

    Args:
        string1: The first input string.
        string2: The second input string.
    """
    print(string1+string2)


def main():
    testcases = int(input())

    while testcases > 0:
        string1 = input()
        string2 = input()
        print_fun(string1, string2)
        testcases -= 1


if __name__ == '__main__':
    main()
