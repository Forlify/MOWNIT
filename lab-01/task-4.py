import numpy as np
import matplotlib.pyplot as plt

print('################################################### STARTED')

################################# a
print('################################################### a')


def logistic(r, x):
    return r * x * (1 - x)


def bifurcation_diagram(x_0, skip, iterations, minimal_r=0, maximal_r=4):
    R = []
    X = []
    r_range = np.linspace(minimal_r, maximal_r, int(1 / 0.0001))

    for r in r_range:
        x = x_0
        for i in range(iterations + skip):
            if i >= skip:
                R.append(r)
                X.append(x)

            x = logistic(r, x)

    plt.plot(R, X, ls='', marker=',')
    plt.ylim(0, 1)
    plt.xlim(minimal_r, maximal_r)
    plt.xlabel('wartosci r')
    plt.ylabel('wartosci x')
    plt.show()


# bifurcation_diagram(0.10, 100, 500)
# bifurcation_diagram(0.25, 100, 500)
# bifurcation_diagram(0.50, 100, 500)
#
# bifurcation_diagram(0.10, 100, 500, minimal_r=1)
# bifurcation_diagram(0.25, 100, 500, minimal_r=2)
# bifurcation_diagram(0.50, 100, 500, minimal_r=3)

################################# b
print('################################################### b')


def trajectories(double, float, r_double, r_float):
    doubles = []
    floats = []
    indexes = []

    for index in range(0, 51):
        double = logistic(r_double, double);
        float = logistic(r_float, float);

        indexes.append(index)
        doubles.append(double)
        floats.append(float)

    plt.plot(indexes, doubles, label='double')
    plt.plot(indexes, floats, label='float')
    plt.title(' trajektorie obliczone z użyciem pojedynczej i podwójnej precyzji ')
    plt.ylabel('wartosc x')
    plt.xlabel('iteracje')
    plt.legend()
    plt.show()


# trajectories(0.1, np.float32(0.1), 3.8, np.float32(3.8))
# trajectories(0.25, np.float32(0.25), 3.8, np.float32(3.8))
# trajectories(0.50, np.float32(0.50), 3.8, np.float32(3.8))

################################# c
print('################################################### c')


def count_iterations(x, r, iterations_threshold):
    epsilon = 1e-7
    iteration = 0

    while x > epsilon:
        if iterations_threshold < iteration:
            return 0
        x = logistic(r, x)
        iteration += 1

    return iteration


def plot_all_iterations():
    x = np.float32(0.001)

    xs = []
    iterations = []

    for i in range(1, 1000):
        print(i)
        xs.append(x * i)
        iterations.append(count_iterations(x * i, np.float32(4), 1e7))

    plt.plot(xs, iterations, '.', label='float')
    plt.title('ilosc iteracji')
    plt.ylabel('ilosc iteracji')
    plt.xlabel('wartosc x')
    plt.legend()
    plt.show()


# plot_all_iterations()

print('################################################### END')
