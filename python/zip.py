# case1 : 일반적인 사용
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

for item in zip(genres, plays):
    print(item)

# ('classic', 500)
# ('pop', 600)
# ('classic', 150)
# ('classic', 800)
# ('pop', 2500)

# case2 : list로 변환

pairs = list(zip(genres, plays))

print(pairs)
# [('classic', 500), ('pop', 600), ('classic', 150), ('classic', 800), ('pop', 2500)]

# case3 : dict로 변환

dict1 = dict(zip(genres, plays))

print(dict1)
# {'classic': 800, 'pop': 2500}
# key값이 중복되서 덮어씌워진듯

# case4 : unzip?

genres2, plays2 = zip(*pairs)

print(*pairs)
# ('classic', 500) ('pop', 600) ('classic', 150) ('classic', 800) ('pop', 2500)
print(genres2, plays2)
# ('classic', 'pop', 'classic', 'classic', 'pop') (500, 600, 150, 800, 2500)