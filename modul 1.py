numbers = int(input("Введите ключ: "))
numbers_list = [int(digit) for digit in str(numbers)]
numbers_result = []
for i in range(0, len(numbers_list), 2):
  if i + 1 < len(numbers_list):
    print(numbers_list[i] + numbers_list[i + 1])
    numbers_result.append(numbers_list[i] + numbers_list[i + 1])
print(numbers_result)