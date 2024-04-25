# 3. Write a Python script to calculate average of elements of a list.
# lst = [12,13,14,25,15,13,14,16,27]
# avg = sum(lst)/len(lst)
# print(avg)

lst = []
for i in range(6):
    lt = int(input("give me list elements: "))
    lst.append(lt)
avg_lst = sum(lst)/len(lst)
print(avg_lst)


