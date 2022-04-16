def select_largest(my_list, beg, end, i):
    if end - beg <= 1:
        return my_list[beg]
    pivot_val = start_partition(my_list, beg, end)
    k = end - pivot_val
    if i < k:
        return select_largest(my_list, pivot_val + 1, end, i)
    elif i > k:
        return select_largest(my_list, beg, pivot_val, i - k)
    return my_list[pivot_val]

def start_partition(my_list, beg, end):
    pivot_val = my_list[beg]
    i = beg + 1
    j = end - 1
    while True:
        while (i <= j and my_list[i] <= pivot_val):
            i = i + 1
            while (i <= j and my_list[j] >= pivot_val):
                j = j - 1
            if i <= j:
                my_list[i], my_list[j] = my_list[j], my_list[i]
            else:
                my_list[beg], my_list[j] = my_list[j], my_list[beg]
                return j
my_list = input('Enter the list of numbers.. ')
my_list = my_list.split()
my_list = [int(x) for x in my_list]
i = int(input('Enter the value for i.. '))
ith_largest = select_largest(my_list, 0, len(my_list), i)
print('The result is {}.'.format(ith_largest))