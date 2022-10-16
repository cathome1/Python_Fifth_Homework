# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
path_in = input("Введите название файла с исходным текстом: ")
path_out = input("Введите название файла куда записать результат: ")
def extract_text(file):
    arr = []
    with open(file,'r',encoding="utf-8" ) as f:
        for i in f.readlines():
            arr.append(i.replace('\n',''))
        f.close()
        return arr
a = extract_text(path_in) 
def encode_text(arr, file):
    with open(file, 'a+', encoding='utf-8' ) as f:
        for i in arr:
            while(len(i)>0):
                letter = i[0]
                count=1
                while(i[count] == letter):
                    count+=1
                    if (len(i)==count):
                        break
                f.write(f"{count}{letter}")
                i=i[count:]
            f.write('\n')
        f.close()       
def decode_text(arr, file):
    with open(file, 'a+', encoding='utf-8' ) as f:
        for i in arr:
            n=''
            for k in i:
                if k.isdigit():
                    n+=k
                else:
                    f.write(k*int(n))
                    n=''
            f.write('\n')
        f.close()
def choice_func(arr=a, file=path_out):
    a = int(input("Выберите действие\n1.Закодировать\n2.Декодироать\n"))
    if a == 1: encode_text(arr,file)
    elif a ==2 : decode_text(arr,file)
    else : print("Введен некоректный вариант, введите правильный вариант")
choice_func()