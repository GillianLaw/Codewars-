def sort_array(source_array):

    odd = []

    for num in source_array:
        if num % 2 != 0:
            odd.append(num)

    odd.sort()

    odd_index = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd[odd_index]
            odd_index += 1
 
    return source_array

a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(sort_array(a))

