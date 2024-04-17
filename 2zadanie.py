#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_x(self, delta_x):
        """Перемещение точки по оси X."""
        self.x += delta_x

    def move_y(self, delta_y):
        """Перемещение точки по оси Y."""
        self.y += delta_y

    def distance_to_origin(self):
        """Определение расстояния до начала координат."""
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to_point(self, other):
        """Расстояние между двумя точками."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def to_polar(self):
        """Преобразование в полярные координаты."""
        r = self.distance_to_origin()
        theta = math.atan2(self.y, self.x)
        return (r, theta)

    def __eq__(self, other):
        """Сравнение на совпадение."""
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """Сравнение на несовпадение."""
        return not self.__eq__(other)

    def __str__(self):
        """Строковое представление класса."""
        return f"Point({self.x}, {self.y})"


# Пример использования класса Point
if __name__ == "__main__":
    point1 = Point(3, 4)
    point2 = Point(6, 8)

    print("Первая точка:", point1)
    print("Вторая точка:", point2)

    point1.move_x(2)
    point1.move_y(-1)
    print("Первая точка после перемещения:", point1)

    origin_dist = point1.distance_to_origin()
    print("Расстояние от первой точки до начала координат:", origin_dist)

    points_dist = point1.distance_to_point(point2)
    print("Расстояние между первой и второй точками:", points_dist)

    polar_coords = point1.to_polar()
    print("Полярные координаты первой точки:", polar_coords)

    print("Точки совпадают:" if point1 == point2 else "Точки не совпадают:")
