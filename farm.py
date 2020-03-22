import random


class Cattle:
    def __init__(self, type, name, weight, sound):
        self.type = type
        self.name = name
        self.weight = weight
        self.satisfied = False
        self.voice = sound

    def feed(self):
        self.satisfied = True

    def benefit(self):
        print('Просто полюбоваться!')

    @staticmethod
    def know_by_voice(sound):
        if sound == 'Га-га-га':
            return 'Это гуси'
        elif sound == 'Мууу':
            return 'Это корова'
        elif sound == 'Бееее':
            return 'Это овца'
        elif sound == 'Ку-ка-ре-ку':
            return 'Это курица'
        elif sound == 'Мееее':
            return 'Это коза'
        elif sound == 'Кря-кря':
            return 'Это утка'
        else:
            return 'На ферме такого животного нет!'


class DairyAnimal(Cattle):
    def __init__(self, type, name, weight, sound):
        super().__init__(type, name, weight, sound)
        self.milkness = random.randint(1, 10)

    def benefit(self):
        self.satisfied = False
        return f'Удой {self.milkness} л'


class Fowl(Cattle):
    def __init__(self, type, name, weight, sound):
        super().__init__(type, name, weight, sound)
        self.eggs_count = random.randint(1, 10)

    def benefit(self):
        self.satisfied = False
        return f'Собрали {self.eggs_count} яиц'


class Sheep(Cattle):
    def __init__(self, type, name, weight, sound):
        super().__init__(type, name, weight, sound)
        self.wool_volume = random.randint(1, 10)

    def benefit(self):
        self.satisfied = False
        return f'Состригли {self.wool_volume} ус.ед шерсти'


if __name__ == '__main__':
    farm_cattles = list()

    # fill farm cattles list
    farm_cattles.append(Fowl('Гусь', 'Серый', 10, 'Га-га-га'))
    farm_cattles.append(Fowl('Гусь', 'Белый', 10, 'Га-га-га'))

    farm_cattles.append(DairyAnimal('Корова', 'Манька', 150, 'Мууу'))

    farm_cattles.append(Sheep('Овца', 'Барашек', 45, 'Бееее'))
    farm_cattles.append(Sheep('Овца', 'Кудрявый', 40, 'Бееее'))

    farm_cattles.append(Fowl('Курица', 'Ко-Ко', 5, 'Ку-ка-ре-ку'))
    farm_cattles.append(Fowl('Курица', 'Кукареку', 4, 'Ку-ка-ре-ку'))

    farm_cattles.append(DairyAnimal('Коза', 'Рога', 89, 'Бееее'))
    farm_cattles.append(DairyAnimal('Коза', 'Копыта', 91, 'Бееее'))

    farm_cattles.append(Fowl('Утка', 'Кряква', 3, 'Кря-кря'))


    # TEST
    print('Узнать голоса всех животных:')
    for pet in farm_cattles:
        print(f'\tЗагадываем {pet.type} - Угадаем по голосу {pet.voice} - {Cattle.know_by_voice(pet.voice)}')

    print()
    print('Сыты ли животные:')
    for pet in farm_cattles:
        print(f'{pet.name} - {pet.satisfied}')

    print('Накормим голодных!')
    for pet in farm_cattles:
        if not pet.satisfied:
            pet.feed()
            print(f'{pet.name} - {pet.satisfied}')

    print()
    print('Пора поработать на ферме!')
    for pet in farm_cattles:
        print(f'{pet.type}: {pet.name} - {pet.benefit()}')

    print()
    print(f'Общий вес животных на ферме: {sum(x.weight for x in farm_cattles)}')
    print(f'Самое тяжелое животное на ферме: {max(x.weight for x in farm_cattles)}')
