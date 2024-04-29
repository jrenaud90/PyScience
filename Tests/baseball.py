def calculate_height(time, velocity, initial_height):
    """Calculates the height of a baseball.

    Assumptions:
    - Does not take into account air resistance or other frictions.
    - Does not allow the baseball to end below ground (height < 0).

    Parameters
    ----------
    time : float, [s]
        Time at which to calculate the height of the baseball.
    velocity : float, [m s-1]
        Velocity of the baseball
    initial_height : float, [m]
        Initial height of the baseball.

    Returns
    -------
    height : float, [m]
        Height of the baseball at provided `time`.
    
    Raises
    ------
    ValueError
        If the calculated height is less than 0 a value error will be raised.
    """
    # Make sure height is positive. Negative height will cause a crash later in the program
    height = velocity * time + initial_height
    if height < 0:
        raise ValueError("Height found to be less than zero which is not permitted.")
    return height
