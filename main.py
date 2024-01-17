from calculator import evaluate_expression
from stringManipulation import manipulateString


def start():
    print('Enter expression (type "exit" to quit):')
    exp = input()

    while exp != 'exit':
        try:
            result = manipulateString(exp)
            print(evaluate_expression(result))
        except ValueError as e:
            print(f"Value Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        print('Enter another expression (or "exit" to quit):')
        exp = input()


def main():
    start()


if __name__ == "__main__":
    main()
