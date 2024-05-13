from sys import argv
from st import st
from ex import ex
from tr import tr
from nr import nr
from gm import gm
from ln import ln
from ls import ls
from bi import bi


def out_in_file(result, cod):
    output_file = f'distr-{cod}.dat'
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
    match parameters['/d']:
        case 'st':
            out_in_file(st(float(parameters['/p1']), float(parameters['/p2']), parameters['/f']), 'st')
        case 'ex':
            out_in_file(ex(float(parameters['/p1']), float(parameters['/p2']), parameters['/f']), 'ex')
        case 'tr':
            out_in_file(tr(float(parameters['/p1']), float(parameters['/p2']), parameters['/f']), 'tr')
        case 'nr':
            out_in_file(nr(float(parameters['/p1']), float(parameters['/p2']), parameters['/f']), 'nr')
        case 'gm':
            out_in_file(gm(float(parameters['/p1']), float(parameters['/p2']), int(parameters['/p3']), parameters['/f']),
                        'gm')
        case 'ln':
            out_in_file(ln(float(parameters['/p1']), float(parameters['/p2']), parameters['/f']), 'ln')
        case 'ls':
            out_in_file(ls(float(parameters['/p1']), float(parameters['/p2']), parameters['/f']), 'ls')
        case 'bi':
            out_in_file(bi(float(parameters['/p1']), int(parameters['/p2']), parameters['/f']), 'bi')
        case 'help':
            print('Справочная информация: \n\n'
                  'Параметры программы:\n'
                  '/f:<имя_файла> - имя файла с входной последовательностью.\n'
                  '/d:<распределение> - код распределения для преобразования последовательности.\n'
                  'Коды распределений:\n'
                  'st – стандартное равномерное с заданным интервалом;\n'
                  'tr – треугольное распределение;\n'
                  'ex – общее экспоненциальное распределение;\n'
                  'nr – нормальное распределение;\n'
                  'gm – гамма распределение;\n'
                  'ln – логнормальное распределение;\n'
                  'ls – логистическое распределение;\n'
                  'bi – биномиальное распределение\n'
                  '/p1:<параметр1> - 1-й параметр, необходимый, для генерации ПСЧ заданного распределения.\n'
                  '/p2:<параметр2> - 2-й параметр, необходимый, для генерации ПСЧ заданного распределения.\n'
                  '/p3:<параметр3> - 3-й параметр, необходимый, для генерации ПСЧ гамма-распределением.\n'
                  'Примеры параметров программы:\n'
                  '/d:st /p1:0 /p2:1 /f:out.txt\n'
                  '/d:tr /p1:1 /p2:2 /f:out.txt\n'
                  '/d:ex /p1:1 /p2:2 /f:out.txt\n'
                  '/d:nr /p1:1 /p2:2 /f:out.txt\n'
                  '/d:gm /p1:2 /p2:3 /p3:2 /f:out.txt\n'
                  '/d:ln /p1:1 /p2:2 /f:out.txt\n'
                  '/d:ls /p1:1 /p2:2 /f:out.txt\n'
                  '/d:bi /p1:0.2 /p2:10 /f:out.txt\n'
                  )
        case _:
            print('Введены некорректные данные')


if __name__ == '__main__':
    main()
