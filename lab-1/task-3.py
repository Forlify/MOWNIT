from numpy import float32
import matplotlib.pyplot as plt
import time

print('################################################### STARTED')


def dzeta_forward(result, n, s):
    for k in range(1, n):
        result += 1 / (k ** s)
    return result


def dzeta_backward(result, n, s):
    for k in range(n, 0, -1):
        result += 1 / (k ** s)
    return result


def eta_forward(result, n, s):
    for k in range(1, n):
        result += ((-1) ** (k - 1)) / (k ** s)
    return result


def eta_backward(result, n, s):
    for k in range(n, 0, -1):
        result += ((-1) ** (k - 1)) / (k ** s)

    return result


################################# 1
print('################################################### 1')
float_points = [float32(2.0), float32(3.6667), float32(5.0), float32(7.2), float32(10.0)]
double_points = [2.0, 3.6667, 5.0, 7.2, 10.0]
iterations = [50, 100, 200, 500, 1000]


def dzeta():
    for s in range(0, 5):
        for n in iterations:
            print('point:', float_points[s],
                  ' n:', n, ' dzeta:',
                  dzeta_forward(float32(0.0), n, float_points[s]),
                  dzeta_forward(0.0, n, double_points[s]),
                  dzeta_backward(float32(0.0), n, float_points[s]),
                  dzeta_backward(0.0, n, double_points[s]))
        print()


dzeta()

# Metoda sumowania w przód polega na dodawaniu wyrazow o rosnacych indeksach do dotychczasowej sumy.
# Przez tow przypadku dzety dodajemy do stosunkowo duzej liczby bardzo male wartosci i to jest powodem
# utraty precyzji. W przypadku sumowania wstecz sytuacja wyglada zupelnie inaczej, dodajemy przy kazdej iteracji
# do dotychczasowej sumy wartosc wieksza - co za tym idzie wynik jest obarczony mniejszym bledem.
################################# 2

print('################################################### 2')


def eta():
    for s in range(0, 5):
        for n in iterations:
            print('point:', float_points[s],
                  ' n:', n, ' dzeta:',
                  eta_forward(float32(0.0), n, float_points[s]),
                  eta_forward(0.0, n, double_points[s]),
                  eta_backward(float32(0.0), n, float_points[s]),
                  eta_backward(0.0, n, double_points[s]))
        print()

eta()

print('################################################### END')

