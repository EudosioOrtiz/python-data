def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left, key)
    merge_sort(right, key)

    return merge_two_sorted_lists(left,right, arr, key)

def merge_two_sorted_lists(a,b, arr , key):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i][key] <= b[j][key]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1
    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1
    

if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    '''
    for arr in test_cases:
        merge_sort(arr)
        print(arr)
    '''
    merge_sort(elements,'time_hours')
    print(elements)