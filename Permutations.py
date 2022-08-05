from itertools import combinations
import csv
d = {1 : "bum bum", 2 : "aaa", 3 : "ba ba", 4 : "mm mm", 5 : "ahh ahh ahh"}
l = []
for r in range(5):
    l.append(list(combinations(range(1, 6), r)))
flat_list = []
l.pop(0)
for sublist in l:
    for item in sublist:
        flat_list.append(item)
og_list = []
for x in flat_list:
    tmp = []
    for i in x:
        tmp.append(d[i])
    og_list.append(tmp)
# Add bum1
list_2 = []
for x in og_list:
    list_2.append(x)
    if "bum bum" in x:
        tmp = []
        for i in x:
            tmp.append(i)
        tmp.append("bum1")
        list_2.append(tmp)
# Add ba1
list_3 = []
for x in list_2:
    list_3.append(x)
    if "ba ba" in x:
        tmp = []
        for i in x:
            tmp.append(i)
        tmp.append("ba1")
        list_3.append(tmp)
# Add ahh1
list_4 = []
for x in list_3:
    list_4.append(x)
    if "ahh ahh ahh" in x:
        tmp = []
        for i in x:
            tmp.append(i)
        tmp.append("ahh1")
        list_4.append(tmp)
list_4.append(["bum bum", "aaa", "ba ba", "mm mm", "ahh ahh ahh", "bum1", "ba1", "ahh1"])
print(list_4)
file = open('/Users/cd/Desktop/AnjulieExcel.csv', 'w+', newline='')

# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerows(list_4)





