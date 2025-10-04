#Creat
skills = {"Python", "Git", "SQL"}
empty_dict = {}  # 这是一个空字典
empty_set = set()  # 这才是一个空集合
duplicate_numbers = [1,2,5,2,3,4,5,1]
unique_numbers = set(duplicate_numbers)
print(f"the numbers after deduplicating is {unique_numbers}")

# add/del/read
#add
skills.add("Docker") # add a single element
skills.update("Flask","React") # add serval elements

'''
del
1. .remove(element) remove a certain element. Will return KeyError if there isn't exist the element.
2. .discard(element) remove an element safely
3. .pop(element) remove an element randomly
'''

# Read / Check membership
# Can't index. but can use the "in" operator to check the membership of the element
if "Python" in skills:
    print("You have master th Python")

my_sports = {"running", "basketball", "swimming"}
friend_sports = {"basketball", "badminton", "tennis"}
#Union
all_sports = my_sports | friend_sports
all_sport_2 = my_sports.union(friend_sports)

#intersection
common_sports = my_sports & friend_sports
common_sport_2 = my_sports.intersection(friend_sports)
# 结果: {'basketball'}

#difference
my_only_sports = my_sports - friend_sports
my_only_sport_2 = my_sports.difference(friend_sports)
# 结果: {'running', 'swimming'}

# symmetric difference
unique_to_each = my_sports ^ friend_sports
unique_to_each_2 = my_sports.symmetric_difference(friend_sports)
# 结果: {'running', 'swimming', 'badminton', 'tennis'}
