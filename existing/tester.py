list1 = ["cock str", "piss str", "wam str"]
list2 = ["too imp", "cock str", "piss str", "fire hazard",  "wam str"]
list3 = ["too imp", "okay", "piss str"]

flag = False
for i in list1:
    if i not in list2:
        print("list2 doestn own green")
        flag = True
        break

if not flag:
    print("list2 owns green")
