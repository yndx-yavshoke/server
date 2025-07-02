from faker import Faker

class NewNameCreate:
    # функция генерации нового имени
    def __init__(self, locale='ru_RU'):
        self.faker = Faker(locale)
    
    def get_name(self):
        return self.faker.name()