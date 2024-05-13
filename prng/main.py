from sys import argv
from bbs import bbs
from rsa import rsa
from lc import lc
from rc4 import rc4
from lfsr import lfsr
from add import add
from mt import mt
from nfsr import nfsr
from p5 import p5


base_output_file = 'rnd.dat'


def out_in_file(result, output_file):
    if not output_file:
        output_file = base_output_file
    with open(output_file, 'w+') as f:
        for i in result:
            f.write(str(i) + ' ')
    print('Последовательность сгенерирована и записана в файл:', output_file, '\n\nВыполнение завершено')


def main():
    arg = list(i.split(':') for i in argv)
    parameters = {'/n': 10000, '/g': 'help'}
    if len(arg[1]) > 1:
        for i in arg[1::]:
            parameters[i[0]] = i[1]
    match parameters['/g']:
        case 'lc':
            out_in_file(lc(int(parameters['/n']), parameters['/i'].split(';')), parameters.get('/f'))
        case 'add':
            out_in_file(add(int(parameters['/n']), parameters['/i'].split(';')), parameters.get('/f'))
        case '5p':
            out_in_file(p5(int(parameters['/n']), parameters['/i'].split(';')), parameters.get('/f'))
        case 'lfsr':
            out_in_file(lfsr(True, int(parameters['/n']), parameters['/i'].split(';')), parameters.get('/f'))
        case 'nfsr':
            out_in_file(nfsr(int(parameters['/n']), parameters['/i'].split(';')), parameters.get('/f'))
        case 'mt':
            out_in_file(mt(int(parameters['/n']), parameters['/i'].split(';')), parameters.get('/f'))
        case 'rc4':
            out_in_file(rc4(int(parameters['/n']), parameters['/i'].split(';')), parameters.get('/f'))
        case 'rsa':
            out_in_file(rsa(int(parameters['/n']), parameters['/i'].split(';')), parameters.get('/f'))
        case 'bbs':
            out_in_file(bbs(int(parameters['/n']), parameters['/i'].split(';')), parameters.get('/f'))
        case 'help':
            print('Справочная информация: \n\n'
                  'Параметры программы:\n'
                  '/g:<method_code> – метод генерации ПСЧ.\n'
                  'Возможные значения: lc, add, 5p, lfstr, nfsr, mt, rc4, rsa, bbs\n'
                  '/i:<init_vector> – инициализационный вектор генератора (вводится через ";")\n'
                  '/n:<sequence_length> – количество генерируемых чисел. Значение по умолчанию: 10 000\n'
                  '/f:<file_name> – полное имя файла, в который будут выводиться данные. Значение по умолчанию: '
                  'rnd.dat\n'
                  '/h - справочная информация\n\n'
                  'Примеры инициализационных векторов генераторов (являются векторами по умолчанию):\n'
                  'Линейный конгруэнтный метод – /g:lc /i:6075;106;1283;7\n'
                  '(Модуль = 6075, множитель = 106, приращение = 1283, начальное значение = 7)\n'
                  'Аддитивный метод – /g:add /i:128, 9, 49\n'
                  '(Модуль = 128, младший индекс = 9, старший индекс = 49)\n'
                  'Пятипараметрический метод – /g:5p /i:89;20;40;69;10;12\n'
                  '(p = 89, q1 = 20, q2 = 40, q3 = 69, w = 10, начальное значение = 12)\n'
                  'Регистр сдвига с обратной связью (РСЛОС) – /g:lfsr /i:1010110101010;541;10 \n'
                  '(Двоичное представление вектора коэффициентов = 1010110101010, начальное значение регистра = 541,'
                  'длина слова = 10)\n'     
                  'Нелинейная комбинация РСЛОС – /g:nfsr /i:1010110101010;1010110101010;1010110101010;541;993;117;10\n'
                  '(101101010, 100001010, 100110 – двоичные представления векторов коэффициентов регистров, '
                  '541, 993, 117, – десятичное представление начальных состояний регистров, длина слова = 10)\n'
                  'Blum-Blum-Shab – rng.exe /g:bbs /i:7\n'
                  '(начальное значение x = 7)\n'
                  'RC4 – /g:rc4 /i:1,2,3,4,5,6,7,31,48,178,46,91,30,15,132,154,108,222,245,211,103\n'
                  '(вектор инициализации = ключ генерации)\n'
                  'RSA – /g:rsa /i:100151,224951,287,22528,22\n'
                  '(p = 100151, q = 224951 [n = p * q], e = 287, x_0 = 22528, l = 22)\n'
                  'вихрь Мерсенна – /g:mt /i:624\n'
                  '(Модуль = 624)\n\n'
                  'Для вызова параметров по умолчанию, оставьте параметр i пустым\n'
                  'Пример такого вызова: /g:nfsr /f:out.txt /i: \n'
                  '(Генерация 10000 чисел  методом нелинейной комбинации РСЛОС с вектором по умолчанию: '
                  '1010110101010;1010110101010;1010110101010;541;993;117;10'
                  )
        case _:
            print('Введены некорректные данные')


if __name__ == '__main__':
    main()
