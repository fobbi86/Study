print('Задача 7. Костя хочет выигрывать')

# После игры в кубики Костя захотел немного изучить работу игровых автоматов,
# а заодно математику и теорию вероятностей.
# Но ему нужно с чего-то начать:
# написать программу, которая поможет выявить закономерности в комбинациях чисел на автомате.
 
# Даны три целых числа.
# Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны).
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a == b and a == c:
  print(3)
elif a == b or a == c or b == c:
  print('2')
else:
  print('0')