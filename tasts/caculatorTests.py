import pytest
@pytest.mark.parametrize(
    'input_n, expected',
    [
        ('5+5', 10),
        ('3*3', 9),
        ('5-2', 3),
        ('555##', 6),
        ('3+-3^2', )
    ]
)