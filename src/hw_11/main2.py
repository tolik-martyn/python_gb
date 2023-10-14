class Auto:
    auto_count = 0

    # <__init__> - это конструктор нашего класса. <__> (два нижних подчеркивания) определяют, что метод не обычный, а могический.
    def __init__(self, auto_name, auto_model, auto_year):
        print("Автомобиль заведен")
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto.auto_count += 1


a = Auto('Volvo', 'x90', 2015)
print(a.auto_year)
