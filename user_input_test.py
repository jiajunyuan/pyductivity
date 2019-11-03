from random import uniform
from weakref import WeakSet


# cat_dict = {}


class IterableCategory(type):
    _categories = WeakSet()

    def __iter__(cls):
        return iter(cls._categories)

    def add_category(cls, category):
        cls._categories.add(category)


class Category(metaclass=IterableCategory):
    def __init__(self, name, chance_param):
        self.__class__.add_category(self)
        self.name = name
        self.chance_param = chance_param
        self.append_to_dict()

    @classmethod
    def user_input(self):
        while 1:
            try:
                name = str(input('Enter name: '))
                chance_param = int(input('Enter chance parameter: '))
                return self(name, chance_param)
            except:
                print('Invalid input!')
                continue

    def append_to_dict(self):
        cat_dict[self.name] = self.chance_param


# To initiate user input
# Category.user_input()

cat_dict = {'Work': 50,
            'Self Care': 20,
            'Play': 20, }


def Category_prob_calculation():
    cat_denom = 0
    for x in cat_dict:
        cat_denom += cat_dict[x]
    for x in cat_dict:
        cat_dict[x] = [cat_dict[x]]
        cat_dict[x].append(cat_dict[x][0] / cat_denom * 100)
        print(x, 'has {:.2f}% chance of occurance'.format(cat_dict[x][1]))
    return cat_denom


def Category_roulette():
    cat_prob_cum = 0
    cat_uniform = uniform(0, cat_denom)
    cat_res = ''
    for x in cat_dict:
        '''lower bound'''
        cat_dict[x].append(cat_prob_cum)
        cat_prob_cum += cat_dict[x][0]
        '''upper bound'''
        cat_dict[x].append(cat_prob_cum)
    for x in cat_dict:
        if cat_dict[x][2] <= cat_uniform and cat_dict[x][3] >= cat_uniform:
            cat_res = x
        return 'And the winning category is {}!'.format(cat_res)
        break


cat_denom = Category_prob_calculation()
print(Category_roulette())