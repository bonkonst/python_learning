class Mathematician:

    def square_nums(self, list_integers_1):
        return [i ** 2 for i in list_integers_1]

    def remove_positives(self, list_integers_2):
        new_list = []
        for i in list_integers_2:
            if i > 0:
                continue
            else:
                new_list.append(i)
        return new_list

    def filter_leaps(self, list_integers_3):
        new_list = []
        for i in list_integers_3:
            if i % 4 == 0:
                new_list.append(i)
        return new_list


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


class Product:
    def __init__(self, type, name, price, quantity):
        self.type = type
        self.name = name
        self.price = price
        self.quantity = quantity

    def add(self, quantity_specific):
        self.quantity = self.quantity + quantity_specific
        return self.quantity

    def set_discount(self, discount):
        self.price = self.price - (discount*self.price)/100
        return self.price


p = Product('Sport', 'Football T-Shirt', 100, 30)

p.quantity == 30
p.add(90)
print(p.quantity)
assert p.quantity == 120

assert p.price == 100
p.set_discount(25)
assert p.price == 75
print(p.price)