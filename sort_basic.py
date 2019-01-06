def bubble(array):
    l = len(array)
    for i in range(l):
        for j in range(l-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def select(array):
    l = len(array)
    for i in range(l):
        min_index = i
        for j in range(i+1, l):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


def insert(array):
    for ind, val in enumerate(array):
        insert_value = array[ind]
        while ind > 0 and array[ind-1] > insert_value:
            array[ind] = array[ind-1]
            ind -= 1
        array[ind] = insert_value
    return array


def shell(array):
    l = len(array)
    gap = int(l/2)
    while gap > 0:
        for i in range(gap, l):
            insert_value = array[i]
            j = i - gap
            while j >= 0 and array[j] > insert_value:
                array[j+gap] = array[j]
                j -= gap
            array[j+gap] = insert_value
        gap = int(gap/2)
    return array


def merge_sort(left, right):
    sorted_array = []
    ll,lr = len(left), len(right)
    index_1, index_2 = 0, 0
    while index_1 < ll and index_2 < lr:
        if left[index_1] < right[index_2]:
            sorted_array.append(left[index_1])
            index_1 += 1
        else:
            sorted_array.append(right[index_2])
            index_2 += 1
    if index_1 < ll:
        sorted_array.extend(left[index_1:])
    if index_2 < lr:
        sorted_array.extend(right[index_2:])
    return sorted_array


def merge(array):
    if len(array) == 1:
        return array
    mid = int(len(array) / 2)
    left = merge(array[:mid])
    right = merge(array[mid:])
    sorted_array = merge_sort(left, right)
    return sorted_array


def quick(array):
    if len(array) <= 1:
        return array
    split_element = array[0]
    left = quick([x for x in array[1:] if x < split_element])
    right = quick([x for x in array[1:] if x > split_element])
    return left + [split_element] + right


def quick2(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    l, r = 1, len(array)-1
    while l <= r:
        while l <= r and array[l] < pivot:
            l += 1
        while l <= r and array[r] >= pivot:
            r -= 1
        if l > r:
            break
        array[l], array[r] = array[r], array[l]
    array[0], array[r] = array[r], array[0]
    left = quick2(array[:r])
    right = quick2(array[r+1:])
    return left + [array[r]] + right


def quick3(array, lower, upper):
    if lower >= upper:
        return
    pivot = array[lower]
    left, right = lower+1, upper
    while left <= right:
        while left <= right and array[left] < pivot:
            left += 1
        while left <= right and array[right] >= pivot:
            right -= 1
        if left > right:
            break
        array[left], array[right] = array[right], array[left]
    array[lower], array[right] = array[right], array[lower]
    quick3(array, lower, right-1)
    quick3(array, right+1, upper)


if __name__ == '__main__':
    unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4, 11, 9, 10, 12, 15, 13]
    quick3(unsorted_list, 0, len(unsorted_list)-1)
    print(unsorted_list)