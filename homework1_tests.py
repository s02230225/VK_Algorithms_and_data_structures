import pytest
from homework1 import *

# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 1: Разворот части массива ==========

def test_rotate_array():
    arr = []
    rotate_array(arr, 3)
    assert arr == []

    arr = [1]
    rotate_array(arr, 5)
    assert arr == [1]

    arr = [1, 2, 3, 4, 5]
    rotate_array(arr, 0)
    assert arr == [1, 2, 3, 4, 5]

    arr = [1, 2, 3, 4, 5]
    rotate_array(arr, 5)
    assert arr == [1, 2, 3, 4, 5]

    arr = [1, 2, 3, 4, 5, 6]
    rotate_array(arr, 3)
    assert arr == [4, 5, 6, 1, 2, 3]

    arr = [1, 2, 3, 4, 5, 6, 7]
    rotate_array(arr, 3)
    assert arr == [5, 6, 7, 1, 2, 3, 4]


def test_rotate_array_2():
    arr = []
    rotate_array_2(arr, 3)
    assert arr == []

    arr = [1]
    rotate_array_2(arr, 5)
    assert arr == [1]

    arr = [1, 2, 3, 4, 5]
    rotate_array_2(arr, 0)
    assert arr == [1, 2, 3, 4, 5]

    arr = [1, 2, 3, 4, 5]
    rotate_array_2(arr, 5)
    assert arr == [1, 2, 3, 4, 5]

    arr = [1, 2, 3, 4, 5, 6]
    rotate_array_2(arr, 3)
    assert arr == [4, 5, 6, 1, 2, 3]



# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 2: Слияние двух отсортированных массивов ==========

def test_merge_sorted_array():
    assert merge_sorted_array([], []) == []
    assert merge_sorted_array([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_array([1, 2, 3], []) == [1, 2, 3]
    assert merge_sorted_array([1], [2]) == [1, 2]
    assert merge_sorted_array([2], [1]) == [1, 2]
    assert merge_sorted_array([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_array([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_array([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_array([1, 4, 5], [2, 3, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_array([1, 3, 5, 7], [2, 4, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_merge_sorted_array_2():
    assert merge_sorted_array_2([], []) == []
    assert merge_sorted_array_2([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_array_2([1, 2, 3], []) == [1, 2, 3]
    assert merge_sorted_array_2([1], [2]) == [1, 2]
    assert merge_sorted_array_2([2], [1]) == [1, 2]
    assert merge_sorted_array_2([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_array_2([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_array_2([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_array_2([1, 3, 5, 7], [2, 4, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 3: Слияние без доп. аллокаций ==========

def test_merge_inplace_backwards():
    arr1 = [1, 2, 3]
    merge_inplace_backwards(arr1, [])
    assert arr1 == [1, 2, 3]

    arr1 = []
    merge_inplace_backwards(arr1, [])
    assert arr1 == []

    arr1 = [0, 0, 0]
    merge_inplace_backwards(arr1, [1, 2, 3])
    assert arr1 == [1, 2, 3]

    arr1 = [2, 0]
    merge_inplace_backwards(arr1, [1])
    assert arr1 == [1, 2]

    arr1 = [1, 0]
    merge_inplace_backwards(arr1, [2])
    assert arr1 == [1, 2]

    arr1 = [1, 2, 3, 0, 0, 0]
    merge_inplace_backwards(arr1, [4, 5, 6])
    assert arr1 == [1, 2, 3, 4, 5, 6]

    arr1 = [4, 5, 6, 0, 0, 0]
    merge_inplace_backwards(arr1, [1, 2, 3])
    assert arr1 == [1, 2, 3, 4, 5, 6]

    arr1 = [1, 3, 5, 0, 0, 0]
    merge_inplace_backwards(arr1, [2, 4, 6])
    assert arr1 == [1, 2, 3, 4, 5, 6]

    arr1 = [1, 2, 3, 0, 0, 0]
    merge_inplace_backwards(arr1, [2, 5, 6])
    assert arr1 == [1, 2, 2, 3, 5, 6]


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 4: Сортировка массива из 0 и 1 ==========

def test_sort_binary():
    arr = []
    sort_binary(arr)
    assert arr == []

    arr = [0]
    sort_binary(arr)
    assert arr == [0]

    arr = [1]
    sort_binary(arr)
    assert arr == [1]

    arr = [0, 0, 0, 1, 1, 1]
    sort_binary(arr)
    assert arr == [0, 0, 0, 1, 1, 1]

    arr = [1, 1, 1, 0, 0, 0]
    sort_binary(arr)
    assert arr == [0, 0, 0, 1, 1, 1]

    arr = [0, 1, 0, 1, 0, 1]
    sort_binary(arr)
    assert arr == [0, 0, 0, 1, 1, 1]

    arr = [1, 0, 1, 0, 1, 0]
    sort_binary(arr)
    assert arr == [0, 0, 0, 1, 1, 1]


def test_sort_binary_2():
    arr = []
    sort_binary_2(arr)
    assert arr == []

    arr = [0]
    sort_binary_2(arr)
    assert arr == [0]

    arr = [1]
    sort_binary_2(arr)
    assert arr == [1]

    arr = [0, 0, 0, 1, 1, 1]
    sort_binary_2(arr)
    assert arr == [0, 0, 0, 1, 1, 1]

    arr = [1, 1, 1, 0, 0, 0]
    sort_binary_2(arr)
    assert arr == [0, 0, 0, 1, 1, 1]

    arr = [0, 1, 0, 1, 0, 1]
    sort_binary_2(arr)
    assert arr == [0, 0, 0, 1, 1, 1]


def test_sort_binary_3():
    arr = []
    sort_binary_3(arr)
    assert arr == []

    arr = [0]
    sort_binary_3(arr)
    assert arr == [0]

    arr = [1]
    sort_binary_3(arr)
    assert arr == [1]

    arr = [0, 0, 0, 1, 1, 1]
    sort_binary_3(arr)
    assert arr == [0, 0, 0, 1, 1, 1]

    arr = [1, 1, 1, 0, 0, 0]
    sort_binary_3(arr)
    assert arr == [0, 0, 0, 1, 1, 1]

    arr = [0, 1, 0, 1, 0, 1]
    sort_binary_3(arr)
    assert arr == [0, 0, 0, 1, 1, 1]


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 5: Сортировка цветов (0, 1, 2) ==========

def test_sort_3_colors():
    arr = []
    sort_3_colors(arr)
    assert arr == []

    arr = [0]
    sort_3_colors(arr)
    assert arr == [0]

    arr = [1]
    sort_3_colors(arr)
    assert arr == [1]

    arr = [2]
    sort_3_colors(arr)
    assert arr == [2]

    arr = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    sort_3_colors(arr)
    assert arr == [0, 0, 0, 1, 1, 1, 2, 2, 2]

    arr = [2, 2, 2, 1, 1, 1, 0, 0, 0]
    sort_3_colors(arr)
    assert arr == [0, 0, 0, 1, 1, 1, 2, 2, 2]

    arr = [0, 2, 1, 0, 2, 1, 0, 2, 1]
    sort_3_colors(arr)
    assert arr == [0, 0, 0, 1, 1, 1, 2, 2, 2]

    arr = [2, 0, 2, 1, 1, 0]
    sort_3_colors(arr)
    assert arr == [0, 0, 1, 1, 2, 2]


def test_sort_3_colors_2():
    arr = []
    sort_3_colors_2(arr)
    assert arr == []

    arr = [0]
    sort_3_colors_2(arr)
    assert arr == [0]

    arr = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    sort_3_colors_2(arr)
    assert arr == [0, 0, 0, 1, 1, 1, 2, 2, 2]

    arr = [2, 2, 2, 1, 1, 1, 0, 0, 0]
    sort_3_colors_2(arr)
    assert arr == [0, 0, 0, 1, 1, 1, 2, 2, 2]

    arr = [0, 2, 1, 0, 2, 1, 0, 2, 1]
    sort_3_colors_2(arr)
    assert arr == [0, 0, 0, 1, 1, 1, 2, 2, 2]

    arr = [2, 0, 2, 1, 1, 0]
    sort_3_colors_2(arr)
    assert arr == [0, 0, 1, 1, 2, 2]


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 6: Чётные числа вперёд ==========

def test_move_even_to_front():
    arr = []
    move_even_to_front(arr)
    assert arr == []

    arr = [2]
    move_even_to_front(arr)
    assert arr == [2]

    arr = [3]
    move_even_to_front(arr)
    assert arr == [3]

    arr = [2, 4, 6, 1, 3, 5]
    move_even_to_front(arr)
    assert arr[:3] == [2, 4, 6]
    assert sorted(arr[3:]) == [1, 3, 5]

    arr = [1, 3, 5, 2, 4, 6]
    move_even_to_front(arr)
    assert arr[:3] == [2, 4, 6]
    assert sorted(arr[3:]) == [1, 3, 5]

    arr = [1, 2, 3, 4, 5, 6]
    move_even_to_front(arr)
    assert arr[:3] == [2, 4, 6]
    assert sorted(arr[3:]) == [1, 3, 5]

    arr = [3, 2, 4, 1, 11, 8, 9]
    move_even_to_front(arr)
    assert arr[:3] == [2, 4, 8]
    assert sorted(arr[3:]) == [1, 3, 9, 11]

    arr = [2, 4, 6, 8]
    move_even_to_front(arr)
    assert arr == [2, 4, 6, 8]

    arr = [1, 3, 5, 7]
    move_even_to_front(arr)
    assert arr == [1, 3, 5, 7]


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 7: Нули в конец ==========

def test_move_zeros():
    arr = []
    move_zeros(arr)
    assert arr == []

    arr = [0]
    move_zeros(arr)
    assert arr == [0]

    arr = [5]
    move_zeros(arr)
    assert arr == [5]

    arr = [1, 2, 3, 0, 0, 0]
    move_zeros(arr)
    assert arr == [1, 2, 3, 0, 0, 0]

    arr = [0, 0, 0, 1, 2, 3]
    move_zeros(arr)
    assert arr == [1, 2, 3, 0, 0, 0]

    arr = [0, 1, 0, 2, 0, 3]
    move_zeros(arr)
    assert arr == [1, 2, 3, 0, 0, 0]

    arr = [0, 1, 0, 3, 12]
    move_zeros(arr)
    assert arr == [1, 3, 12, 0, 0]

    arr = [1, 2, 3, 4]
    move_zeros(arr)
    assert arr == [1, 2, 3, 4]

    arr = [0, 0, 0, 0]
    move_zeros(arr)
    assert arr == [0, 0, 0, 0]


def test_move_zeros_2():
    arr = []
    move_zeros_2(arr)
    assert arr == []

    arr = [0]
    move_zeros_2(arr)
    assert arr == [0]

    arr = [5]
    move_zeros_2(arr)
    assert arr == [5]

    arr = [1, 2, 3, 0, 0, 0]
    move_zeros_2(arr)
    assert arr == [1, 2, 3, 0, 0, 0]

    arr = [0, 0, 0, 1, 2, 3]
    move_zeros_2(arr)
    assert arr == [1, 2, 3, 0, 0, 0]

    arr = [0, 1, 0, 2, 0, 3]
    move_zeros_2(arr)
    assert arr == [1, 2, 3, 0, 0, 0]

    arr = [0, 1, 0, 3, 12]
    move_zeros_2(arr)
    assert arr == [1, 3, 12, 0, 0]

    arr = [1, 2, 3, 4]
    move_zeros_2(arr)
    assert arr == [1, 2, 3, 4]

    arr = [0, 0, 0, 0]
    move_zeros_2(arr)
    assert arr == [0, 0, 0, 0]