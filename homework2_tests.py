import pytest
from homework2 import *


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 1: Разворот односвязного списка ==========

def list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


def array_to_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def test_reverse_list():
    head = array_to_list([])
    assert list_to_array(reverse_list(head)) == []

    head = array_to_list([1])
    assert list_to_array(reverse_list(head)) == [1]

    head = array_to_list([1, 2])
    assert list_to_array(reverse_list(head)) == [2, 1]

    head = array_to_list([1, 2, 3, 4, 5])
    assert list_to_array(reverse_list(head)) == [5, 4, 3, 2, 1]

    head = array_to_list([1, 2, 3, 4, 5, 6])
    assert list_to_array(reverse_list(head)) == [6, 5, 4, 3, 2, 1]


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 2: Найти середину списка ==========

def test_middle_node():
    head = array_to_list([])
    assert middle_node(head) is None
    assert middle_node_2(head) is None

    head = array_to_list([1])
    assert middle_node(head).val == 1
    assert middle_node_2(head).val == 1

    head = array_to_list([1, 2])
    assert middle_node(head).val == 2
    assert middle_node_2(head).val == 2

    head = array_to_list([1, 2, 3])
    assert middle_node(head).val == 2
    assert middle_node_2(head).val == 2

    head = array_to_list([1, 2, 3, 4])
    assert middle_node(head).val == 3
    assert middle_node_2(head).val == 3

    head = array_to_list([1, 2, 3, 4, 5])
    assert middle_node(head).val == 3
    assert middle_node_2(head).val == 3

    head = array_to_list([1, 2, 3, 4, 5, 6])
    assert middle_node(head).val == 4
    assert middle_node_2(head).val == 4


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 3: Удалить элемент из списка ==========

def test_remove_elements():
    head = array_to_list([])
    assert list_to_array(remove_elements(head, 1)) == []
    assert list_to_array(remove_elements_2(head, 1)) == []

    head = array_to_list([1])
    assert list_to_array(remove_elements(head, 1)) == []
    assert list_to_array(remove_elements_2(head, 1)) == []

    head = array_to_list([1])
    assert list_to_array(remove_elements(head, 2)) == [1]
    assert list_to_array(remove_elements_2(head, 2)) == [1]

    head = array_to_list([1, 2, 3, 2, 4])
    assert list_to_array(remove_elements(head, 2)) == [1, 3, 4]
    assert list_to_array(remove_elements_2(head, 2)) == [1, 3, 4]

    head = array_to_list([7, 7, 7, 7])
    assert list_to_array(remove_elements(head, 7)) == []
    assert list_to_array(remove_elements_2(head, 7)) == []

    head = array_to_list([1, 2, 3, 4, 5])
    assert list_to_array(remove_elements(head, 6)) == [1, 2, 3, 4, 5]
    assert list_to_array(remove_elements_2(head, 6)) == [1, 2, 3, 4, 5]


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 4: Является ли одна строка исходной для другой ==========

def test_is_subsequence():
    assert is_subsequence("", "") == True
    assert is_subsequence("", "abc") == True
    assert is_subsequence("abc", "") == False
    assert is_subsequence("abc", "ahbgdc") == True
    assert is_subsequence("axc", "ahbgdc") == False
    assert is_subsequence("ace", "abcde") == True
    assert is_subsequence("aec", "abcde") == False
    assert is_subsequence("abc", "abc") == True
    assert is_subsequence("abc", "acb") == False


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 5: Метод двух указателей (поиск пары) ==========

def test_two_sum_sorted():
    assert two_sum_sorted([], 5) == False
    assert two_sum_binary([], 5) == False

    assert two_sum_sorted([1], 1) == False
    assert two_sum_binary([1], 1) == False

    assert two_sum_sorted([1, 2], 3) == True
    assert two_sum_binary([1, 2], 3) == True

    assert two_sum_sorted([1, 2, 3, 4, 5], 9) == True
    assert two_sum_binary([1, 2, 3, 4, 5], 9) == True

    assert two_sum_sorted([1, 2, 3, 4, 5], 10) == False
    assert two_sum_binary([1, 2, 3, 4, 5], 10) == False

    assert two_sum_sorted([-5, -3, 0, 2, 4, 7], 1) == True
    assert two_sum_binary([-5, -3, 0, 2, 4, 7], 1) == True

    assert two_sum_sorted([-5, -3, 0, 2, 4, 7], 0) == False
    assert two_sum_binary([-5, -3, 0, 2, 4, 7], 0) == False


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 6: Является ли слово палиндромом ==========

def test_is_palindrome():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("aa") == True
    assert is_palindrome("ab") == False
    assert is_palindrome("aba") == True
    assert is_palindrome("abc") == False
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 7: Метод двух указателей (удаление дубликатов) ==========

def test_remove_duplicates():
    nums = []
    assert remove_duplicates(nums) == 0
    assert remove_duplicates_2(nums) == 0
    assert nums[:0] == []

    nums = [1]
    assert remove_duplicates(nums) == 1
    assert nums[:1] == [1]
    nums = [1]
    assert remove_duplicates_2(nums) == 1
    assert nums[:1] == [1]

    nums = [1, 1, 2]
    assert remove_duplicates(nums) == 2
    assert nums[:2] == [1, 2]
    nums = [1, 1, 2]
    assert remove_duplicates_2(nums) == 2
    assert nums[:2] == [1, 2]

    nums = [1, 2, 3, 4, 5]
    assert remove_duplicates(nums) == 5
    assert nums[:5] == [1, 2, 3, 4, 5]
    nums = [1, 2, 3, 4, 5]
    assert remove_duplicates_2(nums) == 5
    assert nums[:5] == [1, 2, 3, 4, 5]

    nums = [1, 1, 1, 2, 2, 3, 3, 3, 4]
    assert remove_duplicates(nums) == 4
    assert nums[:4] == [1, 2, 3, 4]
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 4]
    assert remove_duplicates_2(nums) == 4
    assert nums[:4] == [1, 2, 3, 4]


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 8: Слияние двух отсортированных списков ==========

def test_merge_two_lists():
    list1 = array_to_list([])
    list2 = array_to_list([])
    assert list_to_array(merge_two_lists(list1, list2)) == []

    list1 = array_to_list([])
    list2 = array_to_list([1, 2, 3])
    assert list_to_array(merge_two_lists(list1, list2)) == [1, 2, 3]

    list1 = array_to_list([1, 2, 3])
    list2 = array_to_list([])
    assert list_to_array(merge_two_lists(list1, list2)) == [1, 2, 3]

    list1 = array_to_list([1])
    list2 = array_to_list([2])
    assert list_to_array(merge_two_lists(list1, list2)) == [1, 2]

    list1 = array_to_list([2])
    list2 = array_to_list([1])
    assert list_to_array(merge_two_lists(list1, list2)) == [1, 2]

    list1 = array_to_list([1, 3, 5])
    list2 = array_to_list([2, 4, 6])
    assert list_to_array(merge_two_lists(list1, list2)) == [1, 2, 3, 4, 5, 6]

    list1 = array_to_list([3, 6, 8])
    list2 = array_to_list([4, 7, 9, 11])
    assert list_to_array(merge_two_lists(list1, list2)) == [3, 4, 6, 7, 8, 9, 11]
