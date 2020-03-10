import numpy as np
import matplotlib.pyplot as plt
import time


#######################################################################################


def function(x):
    return 1.0 / (1.0 + x ** 2.0)


def approximation(n, count=500):
    results = []
    x = np.linspace(-5, 5, n + 1)
    vander_x = np.vander(x, n + 1, True)
    coefficients = np.linalg.solve(vander_x, list(map(function, x)))

    for x in np.linspace(-5, 5, count):
        result = 0
        for index, coefficient in enumerate(coefficients):
            result += coefficient * (x ** index)
        results.append(result)

    return results


plt.plot(approximation(5))
# plt.plot(approximation(10))
# plt.plot(approximation(15))

real_function = []
for x in np.linspace(-5, 5, 500):
    real_function.append(function(x))

plt.plot(real_function)
plt.show()


#######################################################################################


def calculate_difference(n):
    results = approximation(n, 30)
    x = np.linspace(-5, 5, 30)

    results = list(map(lambda x, y: x - y, results, list(map(function, x))))

    plt.plot(results)
    plt.show()


calculate_difference(5)
calculate_difference(10)
calculate_difference(15)

#######################################################################################


def chebyshev_approximation(n, count=500):
    results = []
    x = np.linspace(-5, 5, n + 1)
    vander_x = np.vander(x, n + 1, True)
    coefficients = np.linalg.solve(vander_x, list(map(function, x)))

    for x in np.linspace(-5, 5, count):
        result = 0
        for index, coefficient in enumerate(coefficients):
            result += coefficient * (x ** index)
        results.append(result)

    return results