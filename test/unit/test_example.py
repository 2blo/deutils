from deutils import example_function
import pandas as pd
import pytest


@pytest.mark.parametrize(
    ("input", "output"),
    [
        (
            pd.DataFrame({"a": [1, 2, 3]}),
            pd.DataFrame({"a": [1, 2, 3], "new_column": [0, 1, 2]}),
        ),
        (
            pd.DataFrame({"a": [1, 2, 3, 4]}),
            pd.DataFrame({"a": [1, 2, 3, 4], "new_column": [0, 1, 2, 3]}),
        ),
    ],
)
def test_example_function(input: pd.DataFrame, output: pd.DataFrame):
    assert example_function(input).equals(output)
