first = int(input("Введите число: "))
sekond = int(input("Введите число: "))
third = int(input("Введите число: "))
if first == sekond and sekond == third and third == first:
print(3)
elif first == sekond or sekond == third or third == first:
print(2)
elif first != sekond and sekond != third and third != first:
print(0)
else:
print('Не соответствует условию задачи')
