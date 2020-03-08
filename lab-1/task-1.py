from numpy import float32
import matplotlib.pyplot as plt
import time

################################# 1

# number = float32(0.5312500)
number = float32(0.7775563)
numbers = [number] * 10 ** 7

start_time = time.time()

noraml_sum = float32(0.0)
for i in numbers:
    noraml_sum += i

end_time = time.time()


################################# 2


def relative_error(result, real_result):
    return abs((result - real_result) / real_result)


def absolute_error(result, real_result):
    return abs(result - real_result)


print('################################################### STARTED')
print('################################################### 1')

print('1. czas wykonywania normalnej sumy: ', end_time - start_time)

print('################################################### 2')

print('2. suma: ', noraml_sum)
print('2. blad wzgledny: ', relative_error(5312500, noraml_sum))
print('2. blad bezwzgledny: ', absolute_error(5312500, noraml_sum))


################################# 3

def relative_error_over_time():
    sum = float32(0.0)
    relative_errors = []

    for index in range(0, len(numbers)):
        sum += numbers[index]
        if index % 25000 == 0 and index != 0:
            relative_errors.append(relative_error(0.53125 * index, sum));

    plt.plot(relative_errors)
    plt.show()


relative_error_over_time()


################################# 4 I 5


def recursive_sum_of(list):
    if len(list) == 0:
        return float32(0.0)
    elif len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return list[0] + list[1]
    return recursive_sum_of(list[:int(len(list) / 2)]) + recursive_sum_of(list[int(len(list) / 2):])


start_time = time.time()
recursive_sum = recursive_sum_of(numbers)
end_time = time.time()

print('################################################### 4')
print('4. czas wykonywania rekurencyjnej sumy: ', end_time - start_time)
print('4. rekurencyjna suma: ', recursive_sum)

print('################################################### 5')
print('5. blad wzgledny: ', relative_error(5312500, recursive_sum))
print('5. blad bezwzgledny: ', absolute_error(5312500, recursive_sum))

################################# 7

print('################################################### 7')

recursive_sum = recursive_sum_of(numbers)

print('7. blad wzgledny: ', relative_error(number * (10 ** 7), recursive_sum))

print('################################################### END')
