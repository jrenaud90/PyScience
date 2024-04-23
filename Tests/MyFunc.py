def my_function(scale, b):

    if b <= 0:
        # This would be very bad for humanity. Let's assume it will never happen.
        raise ValueError("b should never be <= 0.")

    if scale < 0 and b > 0:
        return b
    elif scale > 0 and b > 0:
        return b - scale
    elif scale == 0:
        return 0
    else:
        return scale
