### 1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
    # каждый узел посещается один раз, ссылки меняются за O(1) => O(n)


### 2
def middle_node(head):
    if not head:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    # когда быстрый достигает конца, медленный оказывается в середине => O(n)


def middle_node_2(head):
    if not head:
        return None
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next

    curr = head
    for _ in range(count // 2):
        curr = curr.next
    return curr
    # два прохода, но тоже O(n)


### 3
def remove_elements(head, val):
    dummy = ListNode(0, head)
    prev = dummy
    curr = head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next
    # каждый узел посещается один раз => O(n)


def remove_elements_2(head, val):
    while head and head.val == val:
        head = head.next

    if not head:
        return head

    curr = head
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
    # тоже O(n)


### 4
def is_subsequence(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
    # если дошли до конца s, значит все символы найдены в том же порядке
    # каждый символ t просматривается один раз => O(len(t))


### 5
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return True
        elif current < target:
            left += 1
        else:
            right -= 1
    return False
    # каждый шаг сужает диапазон поиска, максимум n шагов => O(n)


def two_sum_binary(nums, target):
    for i in range(len(nums)):
        need = target - nums[i]
        left, right = i + 1, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == need:
                return True
            elif nums[mid] < need:
                left = mid + 1
            else:
                right = mid - 1
    return False
    # O(n log n)


### 6
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
    # каждый символ сравнивается один раз => O(n)


### 7
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
    # каждый элемент просматривается один раз, перезапись поверх дубликатов => O(n)


def remove_duplicates_2(nums):
    if not nums:
        return 0
    i = 0
    j = 1
    while j < len(nums):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1
    # тоже O(n)


### 8
def merge_two_lists(list1, list2):
    dummy = ListNode(0)
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 or list2
    return dummy.next
    # каждый узел посещается один раз, меняются только ссылки => O(n+m), O(1) памяти
