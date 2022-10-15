# Напишите программу, удаляющую из текста все слова, 
# содержащие "абв". В тексте используется разделитель пробел.
from random import sample
def make_array (size):
    arr = []
    for i in range(size):
        str = ''.join(sample("абв", 3))
        arr.append(str)
    return arr
test = make_array(10)
print(test)
clear_array = lambda array : " ".join(array).replace('абв', '').split()
print(clear_array(test))