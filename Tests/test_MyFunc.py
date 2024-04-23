import pytest

from MyFunc import my_function


# Basic tests to ensure functionality
def test_benchmark_my_function():
    """ Does this function do what you expect it to do? 
    This should be the first test you ever write, proving that your function actually works
    """

    # Any time the scale is negative, I expect it to return the other number
    assert my_function(-1, 10) == 10

    # If scale is positive then I expect it to return the difference between the two.
    assert my_function(5, 10) == 10 - 5

possible_scales = (-100, -10, -1, 0, 1, 10, 100)
possible_b = (-100, -10, -1, 0, 1, 10, 100)


# Run multiple tests at once
@pytest.mark.parametrize("scale", possible_scales)
@pytest.mark.parametrize("b", possible_b)
def test_many_benchmark_my_function(scale, b):

    if scale < 0 and b > 0:
        assert my_function(scale, b) == b
    elif scale == 0:
        # Edge case. Skip during benchmark test
        pytest.skip(reason="Handled in edge case tests")
    elif b <= 0:
        # Edge case. Skip during benchmark test
        pytest.skip(reason="Handled in edge case tests")
    else:
        assert my_function(scale, b) == b - scale


# Now move on to edge cases
@pytest.mark.parametrize("b", possible_b)
def test_edge_case_zero_scale_my_function(b):
    """ Scale should never be zero, but if it is I just expect the function to return 0 regardless of b """
    if b <= 0:
        pytest.skip("Handled by next test.")
    else:
        assert my_function(0, b) == 0

@pytest.mark.parametrize("scale", possible_scales)
def test_edge_case_zero_b_my_function(scale):
    """ b should never be <= zero """

    with pytest.raises(ValueError):
        my_function(scale, 0)
    
    with pytest.raises(ValueError):
        my_function(scale, -10)


# Now move on to tests that should throw an error
def test_strings():
    """ Function only works for ints and floats. Make sure an error is raised if a string is passed. """
    with pytest.raises(TypeError):
        my_function("Hello", 10)
    
    with pytest.raises(TypeError):
        my_function(10, "World")
