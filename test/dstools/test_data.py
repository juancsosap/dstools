from dstools.data import get_binary_columns

import pytest

class TestGetBinaryColumns:
    def test_with_wrong_data(self):
        data = {'X1':['a', 'b', 'c'], 'X2':['A', 'A', 'B']}
        with pytest.raises(ValueError):
            get_binary_columns(data)

