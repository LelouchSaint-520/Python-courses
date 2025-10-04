# --- 任务一：数据清洗 - 列表去重 ---
print("--- 列表去重 ---")
guest_list_with_duplicates = ["Alice", "Bob", "Charlie", "Bob", "David", "Alice"]

# deduplicate
unique_guests_set = set(guest_list_with_duplicates)

# change the set into list
final_guest_list = list(unique_guests_set)

print(f'原始名单：{guest_list_with_duplicates}')
print(f"去重后的集合:{unique_guests_set}")
print(f"最终的唯一名单:{final_guest_list}")
print("\n")

# --- 任务二：技能标签管理 ---
print("--- 技能标签管理 ---")
my_skills = {"Python","Git"}
print(f"初始技能:{my_skills}")

#学习新技能
my_skills.add("SQl")
my_skills.update("HTML","CSS")
print(f"学习新技能后:{my_skills}")

# 尝试删除一个存在的技能和一个不存在的技能
my_skills.discard("HTML")
my_skills.discard("JavaScript")
print(f"整理技能后:{my_skills}")

#检查是否会某项技能
if "Python" in my_skills:
    print("Yes, I mastered Python")
print("\n")

#分析共同兴趣:
print("Analyse the same Hobby")
userA_movies = {"The Matrix", "Inception", "Interstellar", "The Dark Knight"}
userB_movies = {"Inception", "Parasite", "The Dark Knight", "Spirited Away"}

# 1. 两人看过的所有电影
all_movies = userA_movies.union(userB_movies)
#all_movies = userA_movies ｜ userB_movies
print(f"两人看过的所有电影：{all_movies}")

# 2. 两人共同看过的电影
common_movies = userA_movies.intersection(userB_movies)
#common_movies = userA_movies & userB_movies
print(f"两人共同看过的电影：{common_movies}")

# 3. 只有UserA看过，但UserB没看过的电影
userA_only = userA_movies.difference(userB_movies)
# userA_only = userA_movies - userB_movies
print(f"只有UserA看过的电影：{userA_only}")

# 4. 只有UserA看过，或者只有UserB看过的电影(仅可两两运算)
symmetric_movies = userA_movies.symmetric_difference(userB_movies)
#symmetric_movies = userA_movies ^ userA_movies
print(f"the symmetric movies:{symmetric_movies} ")
