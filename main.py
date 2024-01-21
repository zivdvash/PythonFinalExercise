from calculator import evaluate_expression
from validation import validate_exp


def main():
    print('Enter expression (type "exit" to quit):')
    exp = input()

    while exp != 'exit':
        try:
            validate_exp(exp)
            print(evaluate_expression(exp))
        except ValueError as e:
            print(f"Value Error: {e}")
        except OverflowError as e:
            print(f"Overflow Error: {e}")
        except IndexError as e:
            print(f"IndexError Error: {e}")
        except SyntaxError as e:
            print(f"SyntaxError Error: {e}")
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        print('Enter another expression (or "exit" to quit):')
        exp = input()


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print(f"EOF Error")

    except KeyboardInterrupt:
        print(f"Keyboard Interrupt")
