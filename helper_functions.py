def degrees_check(degrees:float) -> float:
    while degrees > 180.0:
        degrees -= 360.0

    while degrees < -180.0:
        degrees += 360.0

    return degrees