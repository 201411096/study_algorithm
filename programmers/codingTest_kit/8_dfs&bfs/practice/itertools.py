from itertools import permutations, combinations, product, combinations_with_replacement

sample_array = [1,2,3,4]

# 순열
resultArray = permutations(sample_array)
print('permutations ====================================================================================================')
for array in resultArray:
    print(array)

# 조합
resultArray = combinations(sample_array, 2)
print('combinations ====================================================================================================')
for array in resultArray:
    print(array)

# 중복 순열
resultArray = product(sample_array, repeat=2)
print('product ====================================================================================================')
for array in resultArray:
    print(array)

# 중복 조합
resultArray = combinations_with_replacement(sample_array, 2)
print('combinations_with_replacement ====================================================================================================')
for array in resultArray:
    print(array)