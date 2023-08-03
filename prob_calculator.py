import copy
import random

class Hat:
    contents =[]

    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents += [color] * count

    def draw(self, drawnum):
        picked_balls = []
        if drawnum >= len(self.contents):
            return self.contents
        else:
            for i in range(drawnum):
                name = self.contents.pop(random.randrange(len(self.contents)))
                picked_balls.append(name)
            return picked_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        temp_draw = temp_hat.draw(num_balls_drawn)
        found = True
        for key, value in expected_balls.items():
            if temp_draw.count(key) < value:
                found = False
                break
        if found:
            count += 1
    return count/num_experiments

