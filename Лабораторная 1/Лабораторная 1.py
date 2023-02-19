import doctest
from typing import Union


class Table:
    def __init__(self, width: Union[int, float],
                 length: Union[int, float]):  # Класс "Стол" с 2 характеристиками - высота и ширина
        """
        Создание и подготовка к работе объекта "Cтол"
        :param width: ширина стола
        :param length: длина стола
        Примеры:
        table1 = Table(10,20)
        """
        self.length = None
        self.width = None
        self.init_width(width)  # Атрибут ширины
        self.init_lenght(length)  # Атрибут длины

    def init_width(self, wid: (int, float)):
        if not isinstance(wid, (int, float)):
            raise TypeError('Значение должно быть числом')
        if wid < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.width = wid

    def init_lenght(self, leng: (int, float)):
        if not isinstance(leng, (int, float)):
            raise TypeError('Значение должно быть числом')
        if leng < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.length = leng

    def sqr_table(self):
        """
        функция по поиску площади стола
        :return: площадь
        """
        print(f"{self.length * self.width} - площадь стола")

    def perim_table(self):
        """
        функция по поиску периметра стола
        :return: периметр
        """
        print(f'{2 * (self.length + self.width)} - периметр стола')


class Mouse:
    def __init__(self, price: Union[int, float],
                 weight: Union[int, float]):  # Класс "Мышь" c 2 характеристиками - цена и вес
        """
        Создание и подготовка к работе объекта "Мышь2
        :param price: цена
        :param weight: вес
        """
        self.price = None
        self.weight = None
        self.init_price(price)  # Атрибут чуствительности
        self.init_weight(weight)  # Атрибут веса

    def init_price(self, pr: (int, float)):
        if not isinstance(pr, (int, float)):
            raise TypeError('Значение должно быть числом')
        if pr < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.price = pr

    def init_weight(self, wei: (int, float)):
        if not isinstance(wei, (int, float)):
            raise TypeError('Значение должно быть числом')
        if wei < 0:
            raise ValueError('Объем должен быть больше нуля')
        self.weight = wei

    def wei_to_pr(self):
        """
        Функция по поиску веса мышки к её цене
        :return: отношение веса к цене
        """
        print(f"{self.weight / self.price} - отношение массы к цене")

    def acceleration(self, power):
        """
        Функция по поиску ускорения при данной силе
        :param power: сила
        :return: ускорение
        """
        print(f"{power / self.weight} - ускорение мыши при данной силе")


class Keyboard:
    def __init__(self, square: Union[int, float], numbuttons: Union[int, float], numweight: Union[int, float]):  # Класс "Клавиатура" с 3 характеристиками - площадь, число клавиши и вес одной клавиши.
        """
         Создание и подготовка к работе объекта "Клавиатура"
         :param square: площадь клавиатуры
         :param numbuttons: число клавишь
         :param numweight: вес клавиши
         """
        self.square = None
        self.numbuttons = None
        self.numweight = None
        self.init_square(square)  # Атрибут площади
        self.init_numbuttons(numbuttons)  # Атрибут числа кнопок
        self.init_numweight(numweight)  # Атрибут веса одной клавиши

    def init_square(self, sqr: (int, float)):
        if not isinstance(sqr, (int, float)):
            raise TypeError('Значение должно быть числом')
        if sqr < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.square = sqr

    def init_numbuttons(self, numb: (int, float)):
        if not isinstance(numb, (int, float)):
            raise TypeError('Значение должно быть числом')
        if numb < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.numbuttons = numb

    def init_numweight(self, nwei: (int, float)):
        if not isinstance(nwei, (int, float)):
            raise TypeError('Значение должно быть числом')
        if nwei < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.numweight = nwei

    def sqr_num(self):
        """
         Функция по поиску средней площади клавиши на клавиатуре
         :return: средняя плозщадь клавиши
         """
        print(f"{self.square / self.numbuttons} - площадь!")

    def sumweight(self):
        """
         Функция по поиску веса всех клавиш на клавиатуре
         :return: вес всех клавиш
         """
        print(f"{self.numbuttons * self.numweight} - вес всех кнопок")


# TODO Написать 3 класса с документацией и аннотацией типов


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
table1 = Table(100, 200)
table1.perim_table()
table1.sqr_table()
mouse1 = Mouse(1000, 200)
mouse1.wei_to_pr()
mouse1.acceleration(2)
keyboard1 = Keyboard(100, 30, 3)
keyboard1.sqr_num()
keyboard1.sumweight()
