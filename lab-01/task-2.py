from numpy import float32
import matplotlib.pyplot as plt
import time

print('################################################### STARTED')


def kahan_algorithm(numbers):
    sum = float32(0.0)
    err = float32(0.0)

    for elem in numbers:
        y = elem - err
        temp = sum + y

        err = (temp - sum) - y
        sum = temp
    return sum


def relative_error(result, real_result):
    return abs((result - real_result) / real_result)


def absolute_error(result, real_result):
    return abs(result - real_result)


################################# 1
print('################################################### 1')

number = float32(0.7775563)
numbers = [number] * 10 ** 7

start_time = time.time()
kahan_sum = kahan_algorithm(numbers)
end_time = time.time()

print('1. suma (kahan):', kahan_sum)
print('1. blad wzgledny (kahan):', relative_error(number * (10 ** 7), kahan_sum))
print('1. blad bezwzgledny (kahan):', absolute_error(number * (10 ** 7), kahan_sum))

################################# 2
print('################################################### 2')
print('2. sluzy do odjecia bledu on nastepnej liczby po to aby blad przy dodawaniu byl rekompensowany przez roznice elementu oraz erroru')

################################# 3
print('################################################### 3')
print('3. czas wykonywania rekurencyjnej sumy: ', end_time - start_time)

print('################################################### END')
