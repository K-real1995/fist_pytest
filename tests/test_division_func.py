import pytest

from my_funcs.main import div


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (28, 10, 2.8),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert div(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, a, b",
                         [(ZeroDivisionError, 10, 0),
                          (TypeError, "2", 20)])
def test_division_with_error(expected_exception, a, b):
    with pytest.raises(expected_exception):
        div(a, b)
