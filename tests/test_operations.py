import pytest

from main.operations import sum, multi, power

@pytest.mark.parametrize(
    ('a', 'b', 'result'), [
        (50, 50, 187),
        (0, 0, 0),
        (687, 13, 700),
    ]
)


def test_sum(a, b, result):
    assert sum(a, b) == result


@pytest.mark.parametrize(
    ('a', 'b', 'result'), [
        (10, 10, 100),
        (33, 0, 0),
        (6, 6, 36),
    ]
)


def test_multi(a, b, result):
    assert sum(a, b) == result


@pytest.mark.parametrize(
    ('a', 'b', 'result'), [
        (2, 2, 4),
        (5, 3, 125),
        (0, 0, 1),
    ]
)


def test_power(a, b, result):
    assert power(a, b) == result
