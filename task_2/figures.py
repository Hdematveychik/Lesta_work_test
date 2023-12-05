class Circle:
    """
    Класс окружность.
    Args and attrs:
        pos_x (int): координата x
        pos_y (int): координата y
        radius (int): радиус окружности
    """
    def __init__(self, pos_x, pos_y, radius) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius

    def draw(self) -> None:
        """
        Функция отрисовки окружности по заданным параметрам.
        :return: None
        """
        print('Drawing Circle: ({x}, {y}) with radius {radius}.'.format(
              x=self.pos_x, y=self.pos_y, radius=self.radius))


class Triangle:
    """
    Класс треугольник.
    Args and attrs:
        pos_x (int): координата x
        pos_y (int): координата y
        first_side (int): первая сторона треугольника
        second_side (int): вторая сторона треугольника
        third_side (int): третья сторона треугольника
    """
    def __init__(self, pos_x, pos_y, first_side, second_side, third_side) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def draw(self) -> None:
        """
        Функция отрисовки треугольника по заданным параметрам.
        :return: None
        """
        print('Drawing Triangle: ({x}, {y}) with sides {first_side}, {second_side} and {third_side}.'.format(
            x=self.pos_x, y=self.pos_y, first_side=self.first_side,
            second_side=self.second_side, third_side=self.third_side))


class Rectangle:
    """
    Класс прямоугольник.
    Args and attrs:
        pos_x (int): координата x
        pos_y (int): координата y
        width (int): ширина прямоугольника
        height (int): длина прямоугольника
    """
    def __init__(self, pos_x, pos_y, width, height) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

    def draw(self) -> None:
        """
        Функция отрисовки прямоугольника по заданным параметрам.
        :return: None
        """
        print('Drawing Rectangle: ({x}, {y}) with width {width} and height {height}.'.format(
            x=self.pos_x, y=self.pos_y, width=self.width, height=self.height))
