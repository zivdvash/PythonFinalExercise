import math


def factorial(n: float):
    if (n == 1):
        return 1

    return n * factorial(n - 1)



def main():
    print(factorial(5))


if __name__ == "__main__":
    main()
