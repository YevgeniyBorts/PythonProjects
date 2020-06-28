import math


def TrapezoidalQ(n, b, y, z, s):
    # n is Manning's n - table at
    # https://www.engineeringtoolbox.com/mannings-roughness-d_799.html
    # b = Bottom width of channel (ft)
    # y = Depth of channel (ft)
    # z = Side slope of channel (horizontal)
    # s = Directional slope of channel - direction of flow
    A = b * y + z * y * y
    W = b + 2 * y * math.sqrt(1 + z * z)
    R = A / W
    Q = 1.49 / n * A * math.pow(R, 2.0 / 3.0) * math.sqrt(s)
    return Q


def CalculateDepth(q, n, w, z, s):
        error = 1
        accuracy = 0.001
        increment = 0.1
        ys = 0
        while (error > accuracy):
            qa = TrapezoidalQ(n, b, ys, z, s)
            error = q - qa
            if (error > 0):
                ys = ys + increment
            else:
                ys = ys - increment
                increment = increment / 2
                error = -error
        return ys


#3 ft bottom, 2 slope, 1 foot drop every 100ft gives a Q of 25.9, not 25.1

b = 3
z = 2
s = 0.01
y = 1
n = 0.022
q = TrapezoidalQ(n, b, y, z, s);
print("Depth at Q = 25.9: ", CalculateDepth(q, n, b, z, s))
print("Depth at Q = 50: ", CalculateDepth(50, n, b, z, s))