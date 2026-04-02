### 0
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


### 1
def build_tree_from_level_order(arr):
    if not arr:
        return None
    root = TreeNode(arr[0]) if arr[0] is not None else None
    if not root:
        return None
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr):
            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1
        if i < len(arr):
            if arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1
    return root


def build_tree_recursive(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = build_tree_recursive(arr, 2 * i + 1)
    root.right = build_tree_recursive(arr, 2 * i + 2)
    return root


### 2
def is_symmetric_recursive(root):
    def mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                mirror(left.left, right.right) and
                mirror(left.right, right.left))
    return mirror(root, root) if root else True


def is_symmetric_iterative(root):
    if not root:
        return True
    queue = [root.left, root.right]
    while queue:
        left = queue.pop(0)
        right = queue.pop(0)
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)
    return True


### 3
from collections import deque

def min_depth_bfs(root):
    if not root:
        return 0
    q = deque([(root, 1)])
    while q:
        node, depth = q.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))
    return 0


def min_depth_dfs(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return 1 + min_depth_dfs(root.right)
    if not root.right:
        return 1 + min_depth_dfs(root.left)
    return 1 + min(min_depth_dfs(root.left), min_depth_dfs(root.right))


### 4
def min_max_product_bst(arr):
    if not arr or arr[0] is None:
        return 0
    i = 0
    while 2 * i + 1 < len(arr) and arr[2 * i + 1] is not None:
        i = 2 * i + 1
    min_val = arr[i]
    i = 0
    while 2 * i + 2 < len(arr) and arr[2 * i + 2] is not None:
        i = 2 * i + 2
    max_val = arr[i]
    return min_val * max_val


def min_max_product_bst_recursive(arr):
    if not arr or arr[0] is None:
        return 0
    def find_extreme(i, go_left):
        if i >= len(arr) or arr[i] is None:
            return None
        next_i = 2 * i + 1 if go_left else 2 * i + 2
        next_val = find_extreme(next_i, go_left)
        return next_val if next_val is not None else arr[i]
    min_val = find_extreme(0, True)
    max_val = find_extreme(0, False)
    return min_val * max_val if min_val is not None and max_val is not None else 0


### 5
def is_same_tree_recursive(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and
            is_same_tree_recursive(p.left, q.left) and
            is_same_tree_recursive(p.right, q.right))


def is_same_tree_iterative(p, q):
    from collections import deque
    queue = deque([(p, q)])
    while queue:
        node1, node2 = queue.popleft()
        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        queue.append((node1.left, node2.left))
        queue.append((node1.right, node2.right))
    return True
