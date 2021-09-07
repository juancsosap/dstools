from dstools.metrics import *

import pytest

class TestGetMetrics:
    def test_get_metrics(self):
        model = None
        X = {'X1':['a', 'b', 'c'], 'X2':['A', 'A', 'B']}
        Z = {'Z':[0, 1, 0]}
        with pytest.raises(ValueError):
            get_metrics(model, X, Z)

