'''
Реализация алгоритма Цезаря
'''
import sys
# EN = ""
EN = " 1234567890abcdefghijklmnopqrstuvwxyz"
RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
def caesar(text:str, offset:int):
    '''
    Алгоритм цезаря string, int
    '''
    ret_string = ""
    for i in text:
        if i.lower() in EN:
            ret_string += EN[(EN.find(i.lower())+offset)%len(EN)]
        elif i.lower() in RU:
            ret_string += RU[(RU.find(i.lower())+offset)%len(RU)]
        else:
            ret_string += i.lower()
            # ret_string += ""

    return ret_string
def file_caesar(filename:str, outfilename:str, offset:int):
    '''
    Изменение файла filename по алгоритму Цезаря на offset
    '''
    with open(outfilename, "w",encoding="utf-8") as filewrite:
        with open(filename,encoding="utf-8") as file:
            if not file:
                print("no file")
                sys.exit(1)
            for line in file:
                # Построчное вычисление
                res_str = caesar(line, offset)
                # Запись в файл
                filewrite.write(res_str)
def main():
    '''
    Main function
    '''

    offs = int(input("Введите число:\n"))
    # file_caesar("test.txt","output.txt", offs)
    file_caesar("voyna-i-mir-tom-1.txt","output.txt", offs)
    file_caesar("output.txt","output№2.txt", -offs)

    print("DONE!")
    input("Нажмите Enter для завершения программы")

if __name__ == "__main__":
    main()
