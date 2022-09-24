'''
Модуль с инструментами для частотного анализа текста
'''
import operator
import sys
from collections import Counter

import caesar

# EN_ch = " EARIOTNSLCUDPMHGBFYWKVXZJQ".lower()

def true_analiz(filename:str, outfilename:str, freq_letters:str):
    '''
    Частотный анализ текста
    '''
    frequency = {}
    str_frequency = {}
    with open(outfilename, "w",encoding="utf-8") as filewrite:
        with open(filename,encoding="utf-8") as file:
            if not file:
                print("no file")
                sys.exit(1)
            # Подсчет частоты
            for line in file:
                for i in line:
                    if i.lower() not in frequency:
                        frequency[i.lower()] = 1
                    else:
                        frequency[i.lower()] += 1
            maxlen = len(frequency)
            for i in range(maxlen):
                max_ = max(frequency.items(), key=operator.itemgetter(1))[0]
                str_frequency[max_] = frequency.pop(max_)
        letters = ''.join(list(str_frequency))
        # print(''.join(list(freq_letters))) #Печать символов для отладки
        # print(''.join(letters))
        with open(filename,encoding="utf-8") as file:
            if not file:
                print("no file")
                exit(1)
            # m = 0
            # Чтение, преобразование и запись в файл
            for line in file:
                for i in line:
                    # m+=1
                    # if m >10: break
                    ind = letters.find(i.lower())
                    if ind < len(freq_letters):
                        # print("ind:", ind, i, EN_ch[ind])
                        filewrite.write(freq_letters[ind])
                    else:
                        filewrite.write(i)

def caesar_analiz(filename:str, outfilename:str, alfabet:str, freq_letters:str, letterscnt:int):
    '''
    Определяет смещение в шифре цезаря и изменяет по нему слова из файла filename
    Запись в файл outfilename
    letterscnt - количество букв, по которому определяется смещение
    '''
    frequency = {}
    str_frequency = {}
    with open(outfilename, "w",encoding="utf-8") as filewrite:
        with open(filename,encoding="utf-8") as file:
            if not file:
                print("no file")
                sys.exit(1)
            # Подсчет частоты
            for line in file:
                for i in line:
                    if i.lower() not in frequency:
                        frequency[i.lower()] = 1
                    else:
                        frequency[i.lower()] += 1
            maxlen = len(frequency)
            for i in range(maxlen):
                max_ = max(frequency.items(), key=operator.itemgetter(1))[0]
                str_frequency[max_] = frequency.pop(max_)
            letters = ''.join(list(str_frequency))
            # print(''.join(list(freq_letters))) #Печать символов для отладки
            # print(''.join(letters))
            # Определение смещения
            diff = []
            for i in range(letterscnt):
                ind1 = (alfabet.find(freq_letters[i].lower()))
                ind2 = (alfabet.find(letters[i].lower()))
                diff.append(ind1-ind2)
            # print(diff)
            most_common = Counter(diff).most_common(1)[0][0]
            # print("most common:",most_common)
        with open(filename,encoding="utf-8") as file:
            if not file:
                print("no file")
                exit(1)
            for line in file:
                filewrite.write(caesar.caesar(line,most_common))
    return most_common


    # print(ch)
    # print(ch1)
def main():
    '''
    Main function
    '''
    freq_letters = ' оаеитнлрсвкмдупбгычьзяйхжшюфэщёцъ'
    alfabet = " абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    true_analiz("output.txt","output_true_analiz.txt",freq_letters)
    smesh = caesar_analiz("output.txt","output_caesar_analiz.txt",alfabet,freq_letters,5)
    print("Смещение = ", smesh)
    print("DONE!")
    input("Нажмите Enter для завершения программы")

if __name__ == "__main__":
    main()
