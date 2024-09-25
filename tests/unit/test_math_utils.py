from math_utils import add


class TestAdd:
    @staticmethod
    def test_success():
        assert add(1, 2) == 3

    @staticmethod
    def test_fail():
        assert add(1, 2) == 4
