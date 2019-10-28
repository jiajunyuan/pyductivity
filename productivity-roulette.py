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
    def user_input(cls):
        while 1:
            try:
                name = str(input('Enter name: '))
                chance_param = int(input('Enter chance parameter: '))
                return cls(name, chance_param)
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


def category_denom_calculation():
    denom = 0
    for x in cat_dict:
        denom += cat_dict[x]
    return denom


cat_denom = category_denom_calculation()


def category_prob_calculation():
    for x in cat_dict:
        cat_dict[x] = [cat_dict[x]]
        cat_dict[x].append(cat_dict[x][0] / cat_denom * 100)
        # print('{} has {:.2f}% chance of occurrence'.format(x, cat_dict[x][1]))


category_prob_calculation()


def category_roulette():
    prob_cum = 0
    randit = uniform(0, cat_denom)
    res = ''
    for x in cat_dict:
        '''lower bound'''
        cat_dict[x].append(prob_cum)
        prob_cum += cat_dict[x][0]
        '''upper bound'''
        cat_dict[x].append(prob_cum)
    for x in cat_dict:
        if cat_dict[x][2] <= randit and cat_dict[x][3] >= randit:
            res = x
    print('The winning category is {}!'.format(res))
    return res


cat_roulette_selection = category_roulette()

# act_dict = {}

class IterableActivity(type):
    _activities = WeakSet()

    def __iter__(cls):
        return iter(cls._activities)

    def add_activity(cls, activity):
        cls._activities.add(activity)


class Activity(metaclass=IterableActivity):
    def __init__(self, category, name, chance_param):
        self.__class__.add_activity(self)
        self.category = category
        self.name = name
        self.chance_param = chance_param
        self.append_to_dict()

    @classmethod
    def user_input(cls):
        while 1:
            try:
                category = str(input('Enter category: '))
                name = str(input('Enter name: '))
                chance_param = int(input('Enter chance parameter: '))
                return cls(category, name, chance_param)
            except:
                print('Invalid input!')
                continue

    def append_to_dict(self):
        act_dict[self.name] = [self.category, self.chance_param]
#
#
# # Activity.user_input()
# # testing param
act_dict = {'Python DataQuest Course': ['Work', 50],
            'Python Productivity Roulette': ['Work', 30],
            'Exercise': ['Self Care', 20],
            'Whatever you want': ['Play', 10]}


def category_based_activities():
    res_dict = {}

    for x in act_dict:
        if act_dict[x][0] == cat_roulette_selection:
            res_dict[x] = act_dict[x]
    return res_dict


act_cat_dict = category_based_activities()


def activity_denom_calculation():
    denom = 0

    for x in act_cat_dict:
        denom += act_cat_dict[x][1]
    return denom

act_cat_denom = activity_denom_calculation()

def activity_prob_calculation():  # todo separate function to return category based and global percentage
    for x in act_cat_dict:
        act_cat_dict[x].append(act_cat_dict[x][1] / act_cat_denom * 100)
        for y in cat_dict:
            if act_cat_dict[x][0] == y:
                act_cat_dict[x].append(act_cat_dict[x][2] * cat_dict[y][1] / 100)
        #print('{} has {:.2f}% chance of occurrence given its category is selected, or {:.2f}% globally'.format(x, act_dict[x][2], act_dict[x][3]))

activity_prob_calculation()

def activity_roulette():
    prob_cum = 0
    randit = uniform(0, act_cat_denom)
    res = ''

    for x in act_dict:
        if act_dict[x][0] == cat_roulette_selection:
            act_cat_dict[x] = act_dict[x]
    for x in act_cat_dict:
        '''lower bound'''
        act_cat_dict[x].append(prob_cum)
        prob_cum += act_cat_dict[x][1]
        '''upper bound'''
        act_cat_dict[x].append(prob_cum)
    for x in act_cat_dict:
        if act_cat_dict[x][4] <= randit and act_cat_dict[x][5] >= randit:
            res = x
    return 'And the winning activity is {}!'.format(res)


act_roulette_selection = activity_roulette()
print(act_roulette_selection)
