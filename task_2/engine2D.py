from typing import Any
from figures import Circle, Triangle, Rectangle


class Engine2D:
    """Class Engine 2d"""
    class DrawEngine:
        """
        Class Draw engine.
        Args:
            canvas (list): текущий список примитивов для отрисовки
            pencil color (Any): текущий цвет отрисовки
        """
        canvas = []
        pencil_color = None

        def add_figure(self, figure: Any) -> None:
            """
            Функция добавления фигуры.
            :param figure:
            :return: None
            """
            if self.pencil_color is not None:
                self.canvas.append([figure, self.pencil_color])
            else:
                self.canvas.append(figure)

        def draw(self, color=None) -> None:
            """
            Функция отрисовки фигур.
            :param color:
            :return: None
            """
            if self.canvas:

                for i_figure in self.canvas:

                    if isinstance(i_figure, list):
                        color = i_figure[1]
                        i_figure = i_figure[0]
                    if isinstance(i_figure, Circle):
                        i_figure.draw()
                    elif isinstance(i_figure, Triangle):
                        i_figure.draw()
                    elif isinstance(i_figure, Rectangle):
                        i_figure.draw()

                    if color is not None:
                        print('Pencil color: {pencil_color}'.format(
                               pencil_color=color))

                self.canvas = []
            else:
                print('First add at least one shape using the method draw()')

        def changing_pencil(self, color: str) -> None:
            """
            Функция смены цвета отрисовки.
            :param color:
            :return: None
            """
            self.pencil_color = color

