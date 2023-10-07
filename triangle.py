
def area(a, h):
    '''
    Возвращает площадь треугольника согласно формуле a * h / 2
        :param a:
            a (int/float/complex) : число, основание треугольника
        :param h:
            h (int/float/complex) : число, высота треугольника
        :return:
            area(float/complex) :  число, площадь треугольника по формуле a * h / 2
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника согласно формуле a + b + c
        :param a:
            a (int/float/complex) : число, сторона треугольника
        :param b:
            b (int/float/complex) : число, сторона треугольника
        :param c:
            c (int/float/complex) : число, сторона треугольника
        :return:
            area(float/complex) :  число, периметр треугольника по формуле a + b + c
    '''
    return a + b + c
