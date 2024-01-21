from calculator import evaluate_expression
from validation import validate_exp


def main():
    """
    Main function to interactively evaluate mathematical expressions.

    The user can input expressions until typing 'exit'. The program handles various errors, such as
    ValueError, OverflowError, IndexError, SyntaxError, ZeroDivisionError, and other general exceptions.

    To run the program, execute the script, and input mathematical expressions when prompted.

    Press 'exit' to terminate the program.

    Usage:
    1. Run the script.
    2. Input mathematical expressions.
    3. Type 'exit' to end the program.
    """
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
