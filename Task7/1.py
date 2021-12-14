class Rectangle:
    def __init__(self, a: float = 4.0, b: float = 3.0):
        if a <= 0 or b <= 0:
            raise ValueError

        self.__side_a = a
        self.__side_b = b

    def get_side_a(self):
        return self.__side_a

    def get_side_b(self):
        return self.__side_b

    def area(self):
        return self.__side_a * self.__side_b

    def perimeter(self):
        return 2 * (self.__side_a + self.__side_b)

    def is_square(self):
        return self.__side_a == self.__side_b

    def replace_sides(self):
        self.__side_a, self.__side_b = self.__side_b, self.__side_a


class ArrayRectangles:
    def __init__(self, *args, n=0):
        self.__rectangle_array = [None for _ in range(n)]
        lst = []
        for el in args:
            if type(el) is list:
                for nested_el in el:
                    lst.append(nested_el)
            else:
                lst.append(el)
        self.__rectangle_array = lst
        if n > len(self.__rectangle_array):
            self.__rectangle_array.extend([None for _ in range(n - len(self.__rectangle_array))])
        if not all(type(el) is Rectangle or el is None for el in self.__rectangle_array):
            raise ValueError

    def add_rectangle(self, rectangle):
        if None not in self.__rectangle_array:
            return False
        self.__rectangle_array[self.__rectangle_array.index(None)] = rectangle
        return True

    def number_max_area(self):
        max_area = self.__rectangle_array[0]
        for rectangle in self.__rectangle_array:
            if rectangle is None:
                break
            if rectangle.area() > max_area.area():
                max_area = rectangle
        return self.__rectangle_array.index(max_area)

    def number_min_perimeter(self):
        min_perimeter = self.__rectangle_array[0]
        for rectangle in self.__rectangle_array:
            if rectangle is None:
                break
            if rectangle.perimeter() < min_perimeter.perimeter():
                min_perimeter = rectangle
        return self.__rectangle_array.index(min_perimeter)

    def number_square(self):
        number_of_square = 0
        for rectangle in self.__rectangle_array:
            if rectangle is None:
                break
            if rectangle.is_square():
                number_of_square += 1
        return number_of_square
