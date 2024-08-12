from copy import copy

import numpy as np
import pytest

from diffpy.srmise.dataclusters import DataClusters


def test_clear():
    # Initialize DataClusters with input parameters
    actual = DataClusters(x=np.array([1, 2, 3]), y=np.array([3, 2, 1]), res=4)
    expected = DataClusters(x=np.array([]), y=np.array([]), res=0)
    # Perform the clear operation
    actual.clear()
    assert actual == expected


def test___eq__():
    actual = DataClusters(np.array([1, 2, 3]), np.array([3, 2, 1]), 0)
    expected = DataClusters(np.array([1, 2, 3]), np.array([3, 2, 1]), 0)
    assert expected == actual
    attributes = vars(actual)
    for attr_key, attr_val in attributes.items():
        reset = copy(attr_val)
        assert expected == actual
        if attr_val is not None:
            attributes.update({attr_key: attr_val + 1})
        else:
            attributes.update({attr_key: 1})
        try:
            assert not expected == actual
        except AssertionError:
            print(f"not-equal test failed on {attr_key}")
            assert not expected == actual
        attributes.update({attr_key: reset})


# For reset clusters test, we have two test cases:
# Precondition: DataClusters object should be a valid object.
# Case (1): x and y are non-empty with positive res, reset_clusters would reset clusters to largest y arg
# Case (2): x and y are empty with zero res, reset_clusters would reset clusters to an empty numpy arr
@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            # case (1)
            {
                "input_x": np.array([1, 2, 3]),
                "input_y": np.array([3, 2, 1]),
                "input_res": 4,
            },
            DataClusters(np.array([1, 2, 3]), np.array([3, 2, 1]), 4),
        ),
        (
            # case (2)
            {
                "input_x": np.array([]),
                "input_y": np.array([]),
                "input_res": 0,
            },
            DataClusters(np.array([]), np.array([]), 0),
        ),
    ],
)
def test_reset_clusters(inputs, expected):
    actual = DataClusters(x=inputs["input_x"], y=inputs["input_y"], res=inputs["input_res"])
    assert actual == expected
