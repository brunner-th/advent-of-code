

with open('input.txt', 'r') as file:
    contents = file.readlines()

first_list = []
second_list = []

for line in contents:
    numbers = line.split("   ")
    first_list.append(int(numbers[0]))
    second_list.append(int(numbers[1]))


def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list


sorted_first_list = insertion_sort(first_list)
sorted_second_list = insertion_sort(second_list)

sum = 0

for (first, second) in zip(sorted_first_list, sorted_second_list):
    distance = abs(first - second)
    sum += distance

print(sum)

similarity_score = 0

for first in sorted_first_list:
    cnt = 0
    for second in sorted_second_list:
        if first == second:
            cnt += 1
    similarity_score += first*cnt

print(similarity_score)
