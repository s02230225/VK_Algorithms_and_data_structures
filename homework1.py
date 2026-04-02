### 1
def rotate_array(arr, k):
    n = len(arr)
    if n == 0:
        return
    k %= n

    def reverse(i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    # каждый элемент перемещается 2 раза => O(n), дополнительная память не используется


def rotate_array_2(arr, k):
    n = len(arr)
    if n == 0:
        return
    k %= n
    if k == 0:
        return

    count = 0
    start = 0
    while count < n:
        i = start
        prev = arr[start]
        while True:
            j = (i + k) % n
            arr[j], prev = prev, arr[j]
            i = j
            count += 1
            if start == i:
                break
        start += 1
    # каждый элемент перемещается ровно один раз => O(n), дополнительная память не используется


### 2
def merge_sorted_array(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
    # два указателя проходят каждый элемент один раз => O(n+m)


def merge_sorted_array_2(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) or j < len(arr2):
        if i == len(arr1):
            result.append(arr2[j])
            j += 1
        elif j == len(arr2):
            result.append(arr1[i])
            i += 1
        elif arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    return result
    # остатки добавляются внутри цикла, но каждый элемент всё равно один раз => O(n+m)


### 3
def merge_inplace_backwards(arr1, arr2):
    m = 0
    while m < len(arr1) and arr1[m] != 0:
        m += 1
    i = m - 1
    j = len(arr2) - 1
    k = i + j + 1

    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
    # заполнение с конца гарантирует, что данные в arr1 не будут перезаписаны раньше времени


### 4
def sort_binary(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # каждый элемент просматривается один раз => O(n)


def sort_binary_2(arr):
    zeros = 0
    for num in arr:
        if num == 0:
            zeros += 1

    for i in range(len(arr)):
        if i < zeros:
            arr[i] = 0
        else:
            arr[i] = 1
    # два прохода, но всё равно O(n)


def sort_binary_3(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        while i < j and arr[i] == 0:
            i += 1
        while i < j and arr[j] == 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    # каждый элемент перемещается не более одного раза => O(n)


### 5
def sort_3_colors(arr):
    i = 0
    j = 0
    k = len(arr) - 1

    while j <= k:
        if arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] == 1:
            j += 1
        else:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
    # каждый элемент просматривается один раз => O(n)


def sort_3_colors_2(arr):
    counts = [0, 0, 0]
    for num in arr:
        counts[num] += 1

    idx = 0
    for color in range(3):
        for i in range(counts[color]):
            arr[idx] = color
            idx += 1
    # два прохода, но первый это 3 фиксированных цвета => O(n)


### 6
def move_even_to_front(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] % 2 == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # i увеличивается только при встрече чётного, поэтому чётные идут в том порядке, в котором встречаются, тогда
    # порядок чётных сохраняется
    return arr


### 7
def move_zeros(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1
        # когда j > i, мы перезаписываем элементы, которые уже обработаны
        # это безопасно, потому что они либо нули, либо уже скопированы левее

    for j in range(i, len(arr)):
        arr[j] = 0
    # перезапись идёт слева направо, ненулевые элементы сохраняют свой порядок,
    # потому что мы берём их в том же порядке, в котором они встречаются в исходном массиве


def move_zeros_2(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # когда j > i, arr[i] всегда равен 0, потому что все ненулевые уже перемещены левее
    # обмен с нулём не меняет порядок остальных ненулевых элементов,
    # так как каждый ненулевой встаёт на первую свободную позицию слева
