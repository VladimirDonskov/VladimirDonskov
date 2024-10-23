def area(a, h):
    '''
    Принимает числа a и h и возвращает половину их произведения ( Площадь треугольника )
        Параметры:
            a (int): Сторона треугольника
            h (int): Высота, падающая на сторону a
    Пример вызова:
        S = area(5, 2)
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
        Принимает числа a, b, c и возвращает их сумму ( Периметр треугольника )
            Параметры:
                a (int): Сторона треугольника
                b (int): Другая сторона треугольника
                c (int): Оставшаяся сторона треугольника
            Пример вызова:
                P = perimetr(2, 3, 9)
        '''
    return a + b + c
