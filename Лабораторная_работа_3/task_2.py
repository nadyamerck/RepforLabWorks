def find_common_participants(str1, str2, sep=','):
    list1 = str1.split(sep)
    list2 = str2.split(sep)
    ans = list()
    for i in list1:
        for j in list2:
            if i == j:
                ans.append(i)
                break
    return ans


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
