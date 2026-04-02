from homework3 import *


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 1: Найти корень числа ==========

def test_sqrt_int():
    assert sqrt_int(0) == 0
    assert sqrt_int(1) == 1
    assert sqrt_int(2) == 1
    assert sqrt_int(3) == 1
    assert sqrt_int(4) == 2
    assert sqrt_int(8) == 2
    assert sqrt_int(9) == 3
    assert sqrt_int(15) == 3
    assert sqrt_int(16) == 4
    assert sqrt_int(17) == 4
    assert sqrt_int(25) == 5
    assert sqrt_int(26) == 5
    assert sqrt_int(100) == 10


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 2: Два ксерокса ==========

def test_min_copy_time():
    assert min_copy_time(0, 1, 1) == 0
    assert min_copy_time(1, 1, 1) == 1
    assert min_copy_time(5, 1, 2) == 4
    assert min_copy_time(4, 1, 2) == 3
    assert min_copy_time(1, 3, 4) == 3
    assert min_copy_time(10, 2, 3) == 14
    assert min_copy_time(100, 1, 100) == 100


def test_min_copy_time_math():
    assert min_copy_time_math(0, 1, 1) == 0
    assert min_copy_time_math(1, 1, 1) == 1
    assert min_copy_time_math(5, 1, 2) == 4
    assert min_copy_time_math(4, 1, 2) == 3
    assert min_copy_time_math(1, 3, 4) == 3
    assert min_copy_time_math(10, 2, 3) == 14
    assert min_copy_time_math(100, 1, 100) == 100


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 3: Накормить животных ==========

def test_feed_animals():
    assert feed_animals([1, 2, 3], [1, 1, 2]) == 2
    assert feed_animals([2, 2, 3], [1, 2, 3, 4]) == 3
    assert feed_animals([], [1, 2]) == 0
    assert feed_animals([5, 5, 5], [1, 2, 3]) == 0
    assert feed_animals([1, 2, 3], [3, 2, 1]) == 3
    assert feed_animals([1, 1, 1, 1], [1, 1]) == 2
    assert feed_animals([10, 20, 30], [5, 15, 25, 35]) == 3


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 4: Найти разницу между строками ==========

def test_find_added_char():
    assert find_added_char("abcd", "abcde") == "e"
    assert find_added_char("", "a") == "a"
    assert find_added_char("a", "aa") == "a"
    assert find_added_char("abc", "cbaa") == "a"
    assert find_added_char("xyz", "zyxx") == "x"
    assert find_added_char("hello", "helloo") == "o"
    assert find_added_char("abcde", "edcbaf") == "f"


def test_find_added_char_sum():
    assert find_added_char_sum("abcd", "abcde") == "e"
    assert find_added_char_sum("", "a") == "a"
    assert find_added_char_sum("a", "aa") == "a"
    assert find_added_char_sum("abc", "cbaa") == "a"
    assert find_added_char_sum("xyz", "zyxx") == "x"
    assert find_added_char_sum("hello", "helloo") == "o"
    assert find_added_char_sum("abcde", "edcbaf") == "f"


def test_find_added_char_count():
    assert find_added_char_count("abcd", "abcde") == "e"
    assert find_added_char_count("", "a") == "a"
    assert find_added_char_count("a", "aa") == "a"
    assert find_added_char_count("abc", "cbaa") == "a"
    assert find_added_char_count("xyz", "zyxx") == "x"
    assert find_added_char_count("hello", "helloo") == "o"
    assert find_added_char_count("abcde", "edcbaf") == "f"


def test_find_added_char_array():
    assert find_added_char_array("abcd", "abcde") == "e"
    assert find_added_char_array("", "a") == "a"
    assert find_added_char_array("a", "aa") == "a"
    assert find_added_char_array("abc", "cbaa") == "a"
    assert find_added_char_array("xyz", "zyxx") == "x"
    assert find_added_char_array("hello", "helloo") == "o"
    assert find_added_char_array("abcde", "edcbaf") == "f"


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 5: Сумма двух элементов ==========

def test_two_sum_hash():
    assert two_sum_hash([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_hash([3, 2, 4], 6) == [1, 2]
    assert two_sum_hash([3, 3], 6) == [0, 1]
    assert two_sum_hash([1, 2, 3], 7) == []
    assert two_sum_hash([], 5) == []
    assert two_sum_hash([5], 5) == []
    assert two_sum_hash([-1, -2, -3, -4, -5], -8) == [2, 4]
    assert two_sum_hash([0, 4, 3, 0], 0) == [0, 3]
