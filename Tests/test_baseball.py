import pytest

from baseball import calculate_height


# Basic tests to ensure functionality
def test_benchmark_calculate_height():
    """ Does this function do what you expect it to do? 
    This should be the first test you ever write, proving that your function actually works
    """

    # If velocity is zero then the baseball should stay at the initial height no matter the time.
    for time in (-10., 0., 10.):
        assert calculate_height(time=time, velocity=0., initial_height=10.) == 10.
    
    # If time is zero then the baseball should stay at the initial height no matter the velocity.
    for velocity in (-10., 0., 10.):
        assert calculate_height(time=0., velocity=velocity, initial_height=10.) == 10.
    
    # Test some known cases.
    assert calculate_height(time=1., velocity=2., initial_height=5.) == 7. # 1 * 2 + 5
    assert calculate_height(time=5., velocity=2., initial_height=-10.) == 0. # 5 * 2 - 10

possible_velocities = (-100., -10., -1., 0., 1., 10., 100.)
possible_initial_heights = (-100., -10., -1., 0., 1., 10., 100.)
possible_times = (-100., -10., -1., 0., 1., 10., 100.)


# Run multiple tests at once
@pytest.mark.parametrize("velocity", possible_velocities)
@pytest.mark.parametrize("time", possible_times)
@pytest.mark.parametrize("initial_height", possible_initial_heights)
def test_many_vels_times_calculate_height(velocity, time, initial_height):
    """ Test `calculate_height` using many different velocities, initial heights, and times."""

    # We know h = v * t + h_i should never be less than zero. 
    # So v * t >= -h_i is the only valid input. Other inputs should thro an error.
    if velocity * time >= -initial_height:
        # Should not get an error. Let's just check that it produces a positive float.
        # We are hoping our benchmark test will catch if the calculation is incorrect. So this is more to see if the
        # calculation can even be performed.
        height = calculate_height(time, velocity, initial_height)
        assert type(height) == float
        assert height >= 0.
    else:
        # The function should throw an error here. Let's make sure it does.
        with pytest.raises(ValueError):
            calculate_height(time, velocity, initial_height)


# Test interactions with 3rd party packages
def test_astropy_calculate_height():
    """ Test `calculate_height` using AstroPy Units. """

    import astropy.units as u

    velocity = 2.0 * (u.m / u.s)
    initial_height = 10.0 * u.m
    time = 3.0 * u.s

    height = calculate_height(time, velocity, initial_height)
    # Let's make sure the calculation actually worked.
    assert height == 16. * u.m

    # Let's check that the units are correct.
    assert height.unit == u.m

    # Note, `assert type(height) == float` will not work here.
