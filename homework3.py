import math


### 1
def sqrt_int(x):
    if x == 0 or x == 1:
        return x
    low, high = 1, x // 2
    while low <= high:
        mid = (low + high) // 2
        sq = mid * mid
        if sq == x:
            return mid
        elif sq < x:
            low = mid + 1
        else:
            high = mid - 1
    return high
    # границы: low=0, high=x (т.к. корень <= x)
    # каждый шаг сужает диапазон вдвое => O(log x)


def min_copy_time(N, x, y):
    if N == 0:
        return 0
    low, high = 0, N * min(x, y)
    while low < high:
        mid = (low + high) // 2
        if mid // x + mid // y >= N - 1:
            high = mid
        else:
            low = mid + 1
    return low + min(x, y)


def min_copy_time_math(N, x, y):
    if N == 0:
        return 0
    if N == 1:
        return min(x, y)
    t = math.ceil(((N - 1) * x * y) / (x + y))
    while t // x + t // y < N - 1:
        t += 1
    return t + min(x, y)
    # t/x + t/y >= N-1  =>  t >= (N-1) * x * y / (x + y)
    # корректировка нужна из-за целочисленности t//x и t//y


### 3
def feed_animals(animals, portions):
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

    animals = quick_sort(animals)
    portions = quick_sort(portions)

    i = j = 0
    fed = 0
    while i < len(animals) and j < len(portions):
        if portions[j] >= animals[i]:
            fed += 1
            i += 1
            j += 1
        else:
            j += 1
    return fed
    # жадная стратегия: кормим наименьшей порцией наименее требовательное животное
    # сортировка O(n log n), проход O(n)


### 4
def find_added_char(a, b):
    xor = 0
    for ch in a + b:
        xor ^= ord(ch)
    return chr(xor)
    # XOR всех символов: одинаковые символы дают 0, остаётся лишний
    # O(n) времени, O(1) памяти


def find_added_char_sum(a, b):
    sum_a = 0
    for ch in a:
        sum_a += ord(ch)

    sum_b = 0
    for ch in b:
        sum_b += ord(ch)

    return chr(sum_b - sum_a)
    # аналогично прошлому, но через прсото сумму
    # O(n) времени, O(1) памяти


def find_added_char_count(a, b):
    count = {}
    for ch in b:
        count[ch] = count.get(ch, 0) + 1
    for ch in a:
        count[ch] -= 1
        if count[ch] == 0:
            del count[ch]
    return list(count.keys())[0]
    # через хеш-таблицу O(n) времени, O(k) памяти


def find_added_char_array(a, b):
    count = [0] * 256
    for ch in b:
        count[ord(ch)] += 1
    for ch in a:
        count[ord(ch)] -= 1
    for i in range(256):
        if count[i] > 0:
            return chr(i)
    return ""
    # через массив на 256 (пусть мы в ASCII, там букв ять) символов O(n) времени, O(1) памяти


### 5
def two_sum_hash(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
    # хеш-таблица хранит уже просмотренные числа
    # для каждого числа проверяем, есть ли нужное дополнение
    # O(n) времени, O(n) памяти
