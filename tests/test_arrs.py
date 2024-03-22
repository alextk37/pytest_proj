from utils.arrs import get, my_slice
from utils.dicts import get_val
import pytest


class TestArrs:
    @pytest.fixture
    def get_array(self):
        return [1, 2, 3]

    @pytest.mark.parametrize(
            'ind, default, value',
            [
                (1, 'test', 2),
                (4, 'test', 'test')
            ]
    )
    def test_get(self, get_array, ind, default, value):
        assert get(get_array, ind, default) == value
        assert get([], 4, 'test') == 'test'

    @pytest.mark.parametrize(
        'start_point, end_point, res_slice',
        [
            (1, 3, [2, 3]),
            (1, None, [2, 3]),
            (None, 3, [1, 2, 3]),
            (None, None, [1, 2, 3]),
            (-4, None, [1, 2, 3]),
            (None, 6, [1, 2, 3]),
        ]
    )
    def test_my_slice(self, get_array, start_point, end_point, res_slice):
        assert my_slice(get_array, start_point, end_point) == res_slice
        assert my_slice([], None) == []


class TestDicts:
    @pytest.fixture
    def collections(self):
        return {'a': 1, 'b': 2, 'c': 3}

    @pytest.mark.parametrize(
        'key, default, value',
        [
            ('c', 'git', 3),
            (None, 'git', 'git'),
            ('d', 'git', 'git')
        ]
    )
    def test_get_val(self, collections, key, default, value):
        assert get_val(collections, key, default) == value
