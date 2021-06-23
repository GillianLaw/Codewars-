def up_array(arr):

    for num in arr:
        numbs = [1234567890]
        if num not in numbs:
            return None
        else:
            string_ints = [str(int) for int in arr]

            str_of_ints = "".join(string_ints)
            print(str_of_ints)
            new_array = int(str_of_ints) + 1
            print(new_array)
            digits = [int(x) for x in str(new_array)]
            print(digits)

            

print(up_array([1, 2]))
