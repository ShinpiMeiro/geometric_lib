
def area(a, b):
    '''
    Возвращает площадь прямоугольника согласно формуле a*b
        :param a:
            a (int/float/complex) : число, сторона прямоугольника
        :param b:
            b (int/float/complex) : число, сторона прямоугольника
        :return:
            area(int/float/complex) :  число, площадь прямоугольника по формуле a*b
        :example:
            area(4, 5)  # Возвращает: 20

    '''
    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника согласно формуле (a + b)*2
        :param a:
            a (int/float/complex) : число, сторона прямоугольника
        :param b:
            b (int/float/complex) : число, сторона прямоугольника
        :return:
            perimeter(int/float/complex) :  число, площадь прямоугольника по формуле (a + b)*2
        :example:
            perimeter(4, 5)  # Возвращает: 18
    '''
    return (a + b)*2
