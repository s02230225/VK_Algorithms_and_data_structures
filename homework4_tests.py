import pytest
from homework4 import *
from collections import deque


# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==========

def tree_to_level_order(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    # удаляем завершающие None
    while res and res[-1] is None:
        res.pop()
    return res


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 1 ==========

def test_build_tree():
    arr = [1, 2, 3, None, 4, 5, None]
    root1 = build_tree_from_level_order(arr)
    root2 = build_tree_recursive(arr)

    assert tree_to_level_order(root1) == [1, 2, 3, None, 4, 5]
    assert tree_to_level_order(root2) == [1, 2, 3, None, 4, 5]

    assert build_tree_from_level_order([]) is None
    assert build_tree_recursive([]) is None
    assert build_tree_from_level_order([1]) is not None


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 2 ==========

def test_is_symmetric():
    arr = [1, 2, 2, 3, 4, 4, 3]
    root = build_tree_from_level_order(arr)
    assert is_symmetric_recursive(root) == True
    assert is_symmetric_iterative(root) == True

    arr2 = [1, 2, 2, None, 3, None, 3]
    root2 = build_tree_from_level_order(arr2)
    assert is_symmetric_recursive(root2) == False
    assert is_symmetric_iterative(root2) == False

    assert is_symmetric_recursive(None) == True
    assert is_symmetric_iterative(None) == True


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 3 ==========

def test_min_depth():
    arr = [3, 9, 20, None, None, 15, 7]
    root = build_tree_from_level_order(arr)
    assert min_depth_bfs(root) == 2
    assert min_depth_dfs(root) == 2

    root2 = build_tree_from_level_order([1, 2])
    assert min_depth_bfs(root2) == 2
    assert min_depth_dfs(root2) == 2

    assert min_depth_bfs(None) == 0
    assert min_depth_dfs(None) == 0


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 4 ==========

def test_min_max_product_bst():
    arr = [4, 2, 6, 1, 3, 5, 7]
    assert min_max_product_bst(arr) == 1 * 7 == 7
    assert min_max_product_bst_recursive(arr) == 1 * 7 == 7

    assert min_max_product_bst([]) == 0
    assert min_max_product_bst_recursive([]) == 0
    assert min_max_product_bst([42]) == 42 * 42 == 1764
    assert min_max_product_bst_recursive([42]) == 42 * 42 == 1764


# ========== ТЕСТЫ ДЛЯ ЗАДАЧИ 5 ==========

def test_is_same_tree():
    t1 = build_tree_from_level_order([1, 2, 3])
    t2 = build_tree_from_level_order([1, 2, 3])
    t3 = build_tree_from_level_order([1, 2, None])

    assert is_same_tree_recursive(t1, t2) == True
    assert is_same_tree_iterative(t1, t2) == True
    assert is_same_tree_recursive(t1, t3) == False
    assert is_same_tree_iterative(t1, t3) == False
    assert is_same_tree_recursive(None, None) == True
    assert is_same_tree_iterative(None, None) == True
    assert is_same_tree_recursive(None, t1) == False
    assert is_same_tree_iterative(None, t1) == False
