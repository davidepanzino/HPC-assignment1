#!/usr/bin/python3

"""Julia set generator without optional PIL-based image drawing"""
import time
import psutil
from functools import wraps

# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

calc_avg = []
z_serial = []

# decorator to time
def timefn_calc(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        calc_avg.append(t2 - t1)    # Task 1.2
        return result
    return measure_time

def timefn_z_serial(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        z_serial.append(t2 - t1)    # Task 1.2
        return result
    return measure_time

# Task 1.2
#@timefn_calc

# Task 1.3-1.4
# @profile
def calc_pure_python(desired_width, max_iterations):
    """Create a list of complex coordinates (zs) and complex parameters (cs),
    build Julia set"""
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    # build a list of coordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed,
    # we use it to simulate a real-world scenario with several inputs to our
    # function
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    # print("Length of x:", len(x))
    # print("Total elements:", len(zs))
    output = calculate_z_serial_purepython(max_iterations, zs, cs)

    # This sum is expected for a 1000^2 grid with 300 iterations
    # It ensures that our code evolves exactly as we'd intended
    assert sum(output) == 33219980

# Task 1.2
# @timefn_z_serial

# Task 1.3-1.4
# @profile
def calculate_z_serial_purepython(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output

if __name__ == "__main__":

    # Task 1.2
    # for x in range(10):
    #     calc_pure_python(desired_width=1000, max_iterations=300)

    # avg_calc = sum(calc_avg)/len(calc_avg)
    # avg_z = sum(z_serial)/len(z_serial)

    # print()
    # print('Average time of calc_pure_python function: ' + str(avg_calc) + ' seconds')
    # print('Standard Deviation of calc_pure_python function: ' + str(statistics.stdev(calc_avg)) + ' seconds')
    # print('Average time of calculate_z_serial_purepython function: ' + str(avg_z) + ' seconds')
    # print('Standard Deviation of calculate_z_serial_purepython function: ' + str(statistics.stdev(z_serial)) + ' seconds')


    # Calculate the Julia set using a pure Python solution with
    # reasonable defaults for a laptop
    calc_pure_python(desired_width=1000, max_iterations=300) 
