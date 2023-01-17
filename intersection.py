import math as m
def intersection(radius, x_t, y_t, z_t):
    for i in range(len(x_t)):
        # The distance formula is used to check if the point in the trajectory is less than the Earth's radius
        d = m.sqrt(x_t[i]**2 + y_t[i]**2 + z_t[i]**2)
        # The moment this point is found, it will make a new list of coords. up to this iteration
        if d <= radius-100:
            x_t = x_t[:i]
            y_t = y_t[:i]
            z_t = z_t[:i]
            break
    return x_t, y_t, z_t



