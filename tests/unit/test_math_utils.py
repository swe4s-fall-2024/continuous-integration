import pytest

from math_utils import compute_sqr_root


class TestComputeSqrRoot:
    @staticmethod
    def test_positive_number():
        """
        Test that function returns correct square root when given a positive number
        """
        input_val = 4
        expected_output = 2
        actual_output = compute_sqr_root(input_val=input_val)
        assert actual_output == expected_output

    @staticmethod
    def test_negative_number():
        """
        Test to return error when input is a negative number
        """
        input_val = -1
        with pytest.raises(
            ValueError,
            match="Input should be a positive number. Received a negative number",
        ):
            compute_sqr_root(input_val=input_val)
