# Interpolation: Rainfall Calculation

# This program contains three functions: lerp to interpolate, filldata to fill in blanks, and start to run the program.
# LERP function uses a formula requiring minimum value, maximum value, normalization, and the list of data.


# This is the function to perform linear interpolation
def lerp(minv, maxv, n, l):
    minv = int(minv)
    maxv = int(maxv)
    return round(n * (l[maxv] - l[minv]) + l[minv], 2)


# The 0.5 used in filldata may not be accurate, I just put it as a blanket value to save time.
# You may need to tweak the norm values for filldata in order to yield the most accurate results.


# Function to fill missing data in list
def filldata(l):
    l[3] = lerp(2, 5, 0.5, l)
    l[4] = lerp(3, 5, 0.5, l)
    l[6] = lerp(5, 7, 0.5, l)
    l[9] = lerp(8, 10, 0.5, l)
    l[11] = lerp(10, 12, 0.5, l)
    l[13] = lerp(12, 15, 0.5, l)
    l[14] = lerp(13, 15, 0.5, l)
    return l


# Function to run the program
def start():
    # This is the list created with all provided data.
    listpart = [0, 0.4, 0.6, None, None, 1.3, None, 2.1, 2.9, None, 3.4, None, 3.7, None, None, 3.9]

    # Function call to fill missing data in list
    listfull = filldata(listpart)

# Output lists for time and rainfall
    time = []
    [time.append(listfull.index(num)) for num in listfull]
    print("Time: ", time)
    print("Rainfall: ", listfull)

    x = float(0)
    while type(x) == float:
        # User Input
        try:
            x = float(input("Please enter a number between 0 and 15 or press enter to exit: "))
        except ValueError:
            break
        # Maximum
        maxval = round(x)+1

        if (x > 14.5) & (x <= 15):
            maxval = 15
        if x > 15:
            continue
        if x < 0:
            continue

        # Minimum
        minval = maxval-1

        # Normalization
        norm = x-minval

        # Output results
        print("Rainfall at hour", x, "is",  lerp(minval, maxval, norm, listfull))


# Run program
start()
