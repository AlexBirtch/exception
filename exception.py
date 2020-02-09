# ввод от пользователя
def user_input():
    user = input('\nВведите два числа и выражение в виде префиксной нотации: ')

    return  user



# вычисления и проверки
def operation(func):
    function_length = len(func.split())

    # выражение [ + - / * ]
    impression = func.split()[0]

    # С помощью выражения assert проверять, что первая операция в списке доступных операций (+, -, *, /)
    assert impression in ['+', '-', '/', '*'], 'НЕ ВЕРНОЕ ВЫРАЖЕНИЕ'


    # если введено больше или меньше 3-ех выражений/чисел
    if function_length != 3:
        return 'введено не верное кол-во операндов'


    # С помощью конструкций try/except ловим ошибки
    try:
        first_num = int (func.split ()[1])
        second_num = int (func.split ()[2])

        if impression == '+':
            return first_num + second_num
        elif impression == '-':
            return first_num - second_num
        elif impression == '/':
            return round((first_num / second_num), 2)
        elif impression == '*':
            return first_num * second_num
    except ZeroDivisionError:
        return '[ОШИБКА] деление на ноль'
    except ValueError:
        return  '[ОШИБКА] операция со строками'
    except Exception as e:
        return f'[ОШИБКА] {e}'



def main():
    print(operation(user_input()))



if __name__ == '__main__':
    while True:
        main()