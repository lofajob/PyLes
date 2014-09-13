# Score of workout result


class Attempt:
    def __init__(self, weight, iteration):
        self.weight = weight
        self.iteration = iteration
        self.att_value = self.weight * self.iteration

class Ex(object):
    def __init__(self, title, number):
        self.title = title
        self.number = number
    def fill(self):
        __loop = 0
        self.list = []
        while __loop < self.number:
            weight = input("Insert weight of barbell ")
            iteration = input("Insert number of lifting ")
            self.list.append(Attempt(weight,iteration))
            __loop += 1
    def count(self):
        score = 0
        for i in self.list:
            score += i.att_value
        return score
