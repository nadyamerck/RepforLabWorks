numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# непонятно, программа для действительно случайного пропщуенного или для данного случая
position = 4
summ = sum(numbers[:position]) + sum(numbers[position + 1:])
# for i in range(len(numbers)):
#     if numbers[i] is None:
#         position = i
#         continue
#     summ += numbers[i]
numbers[position] = summ / len(numbers)
print("Измененный список:", numbers)
