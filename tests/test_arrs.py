from utils.arrs import get, my_slice
from utils.dicts import get_val
import pytest


class TestArrs:
    @pytest.mark.parametrize(
            'array, ind, default, value',
            [
                ([1, 2, 3], 1, 'test', 2),
                ([], 0, 'test', 'test'),
                ([1, 2, 3], 4, 'test', 'test')
            ]
    )
    def test_get(self, array, ind, default, value):
        assert get(array, ind, default) == value

    @pytest.mark.parametrize(
        'array, start_point, end_point, res_slice',
        [
            ([1, 2, 3, 4], 1, 3, [2, 3]),
            ([1, 2, 3], 1, None, [2, 3]),
            ([1, 2, 3, 4], None, 3, [1, 2, 3]),
            ([1, 2, 3], None, None, [1, 2, 3]),
            ([1, 2, 3], -4, None, [1, 2, 3]),
            ([1, 2, 3], None, 6, [1, 2, 3]),
            ([], None, 6, [])
        ]
    )
    def test_my_slice(self, array, start_point, end_point, res_slice):
        assert my_slice(array, start_point, end_point) == res_slice


class TestDicts:
    @pytest.mark.parametrize(
        'collection, key, default, value',
        [
            ({'a': 1, 'b': 2, 'c': 3}, 'c', 'git', 3),
            ({'a': 1, 'b': 2, 'c': 3}, None, 'git', 'git'),
            ({'a': 1, 'b': 2, 'c': 3}, 'd', 'git', 'git')
        ]
    )
    def test_get_val(self, collection, key, default, value):
        assert get_val(collection, key, default) == value
