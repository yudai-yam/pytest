from operations import sum_a_and_b

def test_sum():
    result = sum_a_and_b(1,2)

    assert result == 3, "something is wrong"