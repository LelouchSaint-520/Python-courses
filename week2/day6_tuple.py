# 取出索引1到索引3的元素 ('b', 'c', 'd')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# 索引:    0    1    2    3    4    5    6    7
subset1 = letters[1:4]
print(f"letters[1:4] -> {subset1}")

# 省略索引，头尾
# 从头开始，取到索引3之前 ('a', 'b', 'c')
subset2 = letters[:3]
print(f"letters[:3] -> {subset2}")
# 从索引4开始，取到末尾 ('e', 'f', 'g', 'h')
subset3 = letters[4:]
print(f"letters[4:] -> {subset3}")
#使用步长
# 从头到尾，每隔一个元素取一个（即所有偶数索引的元素）
every_other = letters[::2]
print(f"letters[::2] -> {every_other}")

#复制与反转
# 完整复制一个列表（创建一个全新的副本）
list_copy = letters[:]
print(f"列表的副本: {list_copy}")

# 使用-1作为步长，可以优雅地反转整个列表
reversed_list = letters[::-1]
print(f"反转后的列表: {reversed_list}")
#切片反转的时候，必须大索引在前，小在后，步进为负数
reversed_slice = letters[5:1:-1]
print(f'reversed_slice is : {reversed_slice}')

# 列表推导式 list comprehension
list_eg1 = [1,2,3,4,5,6,7,8,9,10]
list_lc = [eg**2 for eg in list_eg1 if eg % 2 == 0 ]
print(f'list comprehension of list_eg1 : {list_lc}')