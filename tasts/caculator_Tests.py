import pytest
from calculator import evaluate_expression


@pytest.mark.parametrize(
    'input_n, expected',
    [
        ('5+5', 10),
        ('3*3', 9),
        ('5-2', 3),
        ('555##', 6),
        ('3+-3^2', 12),
        ('1234##', 1),
        ('(-3-(-(-3)))', -6),
        ('~-3', 3),
        ('3+~-3', 6),
        ('~3^3', -27),
        ('~3^2', 9),
        ('4@2', 3),
        ('5+3/2+7/3!', 7.667)
    ]
)
def test_evaluate_exp(input_n, expected):
    assert evaluate_expression(input_n) == expected


@pytest.mark.parametrize("input_value, expected_exception", [
    ('abc', ValueError),
    ('', ValueError),
    (' ', ValueError),
    ('()', SyntaxError),
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
    with pytest.raises(expected_exception):
        evaluate_expression(input_value)
