# 1) Create a tuple `tuplex` containing different data types (string, boolean, float, integer)
#    and print the tuple.
tulpex=("Hi",23.45,7)
print(tulpex)
# 2) Create another tuple `tuplex` containing only integer values and print it.
tuple_1=(23,1,7,20,14)
print(tuple_1)
# 3) Demonstrate tuple immutability:
#    a) Tuples cannot be modified directly (cannot add/change elements in the same tuple).
#    b) Use the `+` operator to merge tuples and create a new tuple.
#    c) Add a single element (9) using `(9,)` and store the new tuple back in `tuplex`.
#    d) Print the updated tuple.
tuple_2=(1,2,3,4,5)
print(tuple_2)
tuple_2=tuple_2 + (9,)
print(tuple_2)
# 4) Create a tuple `tuple1` and count occurrences of a specific value:
#    a) Use `tuple1.count(50)` to count how many times 50 appears.
#    b) Print the count.
tuple1=(50,53,45,50,50,62)
print(tuple1.count(50))
# 5) Create a tuple `tuplex` with multiple integers to demonstrate slicing.
tuple_3=(2,3,4,5,6,7,8,9)
# 6) Slice a portion of the tuple using indexing:
#    a) Use `tuplex[3:5]` to get elements from index 3 up to index 4 (stop index is excluded).
#    b) Store it in `_slice` and print it.
sliced_tuple3=tuple_3[3:5]
print(sliced_tuple3)
# 7) Slice from the beginning when the start index is not provided:
#    a) Use `tuplex[:6]` to get elements from index 0 up to index 5.
#    b) Store it in `_slice` and print it.
tuple3_slice=tuple_3[:6]
print(tuple3_slice)