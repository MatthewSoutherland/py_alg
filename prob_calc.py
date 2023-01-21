import copy
import random


class Hat():

    # kwargs gives us a dictionary
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
        print(self.contents)

    def draw(self, number):
        all_removed = []
        if (number > len(self.contents)):
            removed = self.contents.pop(
                int(random.random() * len(self.contents)))
            all_removed.append(removed)
        return all_removed
