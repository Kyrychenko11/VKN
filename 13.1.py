class River:
    def __init__(self, name, continent, length):
        self.name = name
        self.continent = continent
        self.length = length

    def change_name(self, new_name):
        self.name = new_name

    def change_length(self, new_length):
        self.length = new_length

    def __str__(self):
        return f'Назва: {self.name}, континент: {self.continent}, довжина: {self.length}'

    def __repr__(self):
        return f'Назва: {self.name}, континент: {self.continent}, довжина: {self.length}'

    def __eq__(self, other):
        return self.name == other.name and self.continent == other.continent and self.length == other.length

    def __ne__(self, other):
        return self.name != other.name or self.continent != other.continent or self.length != other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length


river_list = []
river_list.append(River('Дніпро', 'Європа', 2870))
river_list.append(River('Ніл', 'Африка', 6850))
river_list.append(River('Амазонка', 'Америка', 6400))

print(river_list)
river_list[0].change_name('Дніпро-Дніпро')
river_list[0].change_length(3000)
river_list[1].change_name('Шакіл')
river_list[1].change_length(8000)

print(river_list)
