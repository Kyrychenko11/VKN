class Enterprise:
    def __init__(self, name, finance, year, owner):
        self.name = name
        self.finance = finance
        self.year = year
        self.owner = owner

    def set_finance(self, new_finance):
        self.finance = new_finance

    def get_finance(self):
        return self.finance

    def display_all(self):
        print(f'Назва: {self.name}, активи: {self.finance}, рік створення: {self.year}, власник: {self.owner}')

    def set_owner(self, new_owner):
        self.owner = new_owner

    def get_owner(self):
        return self.owner


Enterprise1 = Enterprise('Enterprise1', 1020000000, 1000, 'Owner1')
Enterprise2 = Enterprise('Enterprise2', 30000, 300001, 'Owner2')
Enterprise3 = Enterprise('Enterprise3', 4000, 4002201, 'Owner3')
Enterprise4 = Enterprise('Enterprise4', 50000, 500055501, 'Owner4')

list_of_enterprises = [Enterprise1, Enterprise2, Enterprise3, Enterprise4]

for enterprise in list_of_enterprises:
    if enterprise.get_finance() > 1000000:
        enterprise.display_all()
