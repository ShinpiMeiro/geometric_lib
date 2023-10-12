import math


def area(r):
    '''
    Возвращает площадь круга согласно формуле Pi*r*r
        :param r:
            r (int/float/complex) : число, радиус
        :return:
            area(float/complex) :  число, площадь круга по формуле Pi*r*r
            area(3)  # Возвращает: 28.274333882308138
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга согласно формуле 2*Pi*r
        :param r:
            r (int/float/complex) : число, радиус
        :return:
            perimeter(float/complex) :  число, периметр круга по формуле 2*Pi*r
        '''
    return 2 * math.pi * r
