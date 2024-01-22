import pytest
from calculator import evaluate_expression


@pytest.mark.parametrize(
    'input_n, expected',
    [
        ('5+5', 10),
        ('3*3', 9),
        ('5-2', 3),
        ('555##', 6),
        ('--3!', 6),
        ('3+-3^2', 12),
        ('52!/83^(4@5+65)-12&(7-3--8.5)', -12),
        ('(83^3)&0@(52.7221%10)@2-(42^3!)&0@2-(87##!+30)', -749.319),
        ('3+~-3', 6),
        ('~-3! ', 6),
        ('1234##', 1),
        ('(-3-(-(-3)))', -6),
        ('~--(((-(-3-(45612^2.5)+4@6)---615#)$534%12)---803#+18!@12)', -3201186852863999.5),
        ('((((((((~-3!!^~-3!)#/5) ^ 100)#!#) + ~-(5&2$4)!#)%7 / 10 ) ^ 2 * 1000) % 3)! + ~-------((((((((~-3!!^~-3!)#/5) ^ 100)#!#) + ~-(5&2$4)!#)%7 / 10 ) ^ 2 * 1000) %  3)!', 2),
        ('-3!', -6),
        ('2---3! ', -4),
        ('~-3', 3),
        ('3+~-3', 6),
        ('~3^3', -27),
        ('~3^2', 9),
        ('2 +--3!', 8),
        ('(1234.56789#%7^-10)##   @   (12#+~-----2!)', 10),
        ('4@2', 3),
        ('5/3/5', 0.333),
        ('5+3/2+7/3!', 7.667)
    ]
)
def test_evaluate_exp(input_n, expected):
    """
    Test cases for the evaluate_expression function with valid expressions.
    """
    assert evaluate_expression(input_n) == expected


@pytest.mark.parametrize("input_value, expected_exception", [
    ('abc', ValueError),
    ('', ValueError),
    (' ', ValueError),
    ('~--3!', ValueError),
    ('2 - - 3!', ValueError),
    ('()', SyntaxError),
    ('3!^-~(0.5*82&12%5+(51-28)@2)', SyntaxError),
    ('--~--3', SyntaxError),
    ('~--~-3', SyntaxError),
    ('~~3', SyntaxError),
    ('1~-1', SyntaxError),
    ('1/0', ZeroDivisionError),
    ('(4+3(', SyntaxError),
    ('!', SyntaxError),
    ('+', SyntaxError),
    ('-', SyntaxError),
    ('~', SyntaxError),
    ('5~', SyntaxError),
    ('5+~', SyntaxError),
    ('--', SyntaxError),
    ('*--5', SyntaxError),
    ('5-#5', SyntaxError)
])
def test_invalid_input(input_value, expected_exception):
    """
    Test cases for the evaluate_expression function with invalid expressions.
    """

    with pytest.raises(expected_exception):
        evaluate_expression(input_value)
