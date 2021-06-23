arr = [2, 3, 9]
string_ints = [str(int) for int in arr]
str_of_ints = "".join(string_ints)
print(str_of_ints)
new_array = int(str_of_ints) + 1
print(new_array)
digits = [int(x) for x in str(new_array)]
print(digits)
