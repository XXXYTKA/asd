numbers = int(input("Введите ключ: "))
stealth = 0
stealth_list = 0
carculated = 0
numbers_result = []
for i in range(0, numbers):
  for j in range(numbers):
      if i <= j:
          if i == j:
              stealth_list = stealth + 1
          else:
               carculated = i + j
               if numbers % carculated == 0:
                   if i == 0:
                       stealth_list = stealth + 1
                   else:
                       numbers_result.append(i)
                       numbers_result.append(j)
print(''.join(str(x) for x in numbers_result))
