from engine2D import Engine2D
from figures import Circle, Triangle, Rectangle


def test_add_figure():
    """_add_figure() должна добавлять в список на отрисовку новую фигуру"""
    t_engine = Engine2D.DrawEngine()
    t_engine.add_figure('Figure')
    expected = 'Figure'
    assert t_engine.canvas[0] == expected


def test_changing_pencil():
    """_changing_pencil должна менять цвет карандаша на заданный параметр"""
    t_engine = Engine2D.DrawEngine()
    t_engine.changing_pencil('red')
    expected = 'red'
    assert t_engine.pencil_color == expected


def test_engine():
    """_engine тест всего движка с применением всех методов"""
    new_engine = Engine2D.DrawEngine()
    new_engine.add_figure(Circle(1, 0, 5))
    new_engine.changing_pencil('red')
    new_engine.add_figure(Triangle(5, 6, 10, 11, 4))
    new_engine.changing_pencil('orange')
    new_engine.add_figure(Rectangle(4, 7, 10, 25))
    print('\n')
    new_engine.draw()
