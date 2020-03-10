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


plt.plot(np.linspace(-5, 5, 500), approximation(5))
plt.plot(np.linspace(-5, 5, 500), approximation(10))
plt.plot(np.linspace(-5, 5, 500), approximation(15))

real_function = []
for x in np.linspace(-5, 5, 500):
    real_function.append(function(x))

plt.plot(np.linspace(-5, 5, 500), real_function)
plt.show()


#######################################################################################


def calculate_difference(n):
    results = approximation(n, 30)
    x = np.linspace(-5, 5, 30)

    results = list(map(lambda x, y: x - y, results, list(map(function, x))))

    return results


plt.plot(np.linspace(-5, 5, 30), calculate_difference(5))
plt.plot(np.linspace(-5, 5, 30), calculate_difference(10))
plt.plot(np.linspace(-5, 5, 30), calculate_difference(15))
plt.show()


#######################################################################################

def count_chebyshev_x(n, k, a, b):
    return ((1.0 / 2.0) * (a + b)) + ((1.0 / 2.0) * (b - a) * np.cos(((2.0 * k - 1.0) * np.pi) / (2.0 * n)))


def chebyshev_approximation(n, count=500):
    results = []
    x = []
    for i in range(1, n+1):
        x.append(count_chebyshev_x(n, i, -5, 5))

    print(x)
    vander_x = np.vander(x, n , True)
    coefficients = np.linalg.solve(vander_x, list(map(function, x)))

    for x in np.linspace(-5, 5, 500):
        result = 0
        for index, coefficient in enumerate(coefficients):
            result += coefficient * (x ** index)
        results.append(result)

    return results


# plt.plot(chebyshev_approximation(5))
# plt.plot(chebyshev_approximation(10))
plt.plot(np.linspace(-5, 5, 500), chebyshev_approximation(20))
plt.plot(np.linspace(-5, 5, 500), real_function)

plt.show()
