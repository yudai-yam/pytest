import pandas as pd
from pandas.testing import assert_frame_equal
from pandas_example import double_dataframe


def test_double_dataframe():
    input_df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

    result_df = double_dataframe(input_df)

    expected_df = pd.DataFrame({'a': [2, 4, 6], 'b': [8, 10, 12]})
    assert_frame_equal(result_df, expected_df, check_dtype=False)