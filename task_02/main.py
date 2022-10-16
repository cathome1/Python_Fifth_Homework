# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
path_in = input("Введите название файла с кодируемым текстом: ")
path_out = input("Введите название файла куда записать закодированный текст: ")
def extract_text(file):
    arr = []
    with open(file,'r',encoding="utf-8" ) as f:
        for i in f.readlines():
            arr.append(i.replace('\n',''))
        f.close()
        return arr
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
a = extract_text(path_in)        
encode_text(a,path_out)
