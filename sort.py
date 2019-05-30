import random
import math


class Group:
    def __init__(self):
        self.max_grouping_one = None
        self.mim_grouping_one = None

    def print_grouping(self, array, line):
        print(" \r")
        for i in range(line):
            print("  ", array[i])
        print("\n")

    def search_max_and_min(self, array, line, column):
        self.max_grouping_one = array[0][0]
        self.mim_grouping_one = array[0][0]
        for x in range(line):
            for y in range(column):
                if array[x][y] > self.max_grouping_one:
                    self.max_grouping_one = array[x][y]
                if array[x][y] < self.mim_grouping_one:
                    self.mim_grouping_one = array[x][y]
        print('\n\n Min: ', self.mim_grouping_one)
        print('\n\n Max: ', self.max_grouping_one)

    def grouping_part_one(self):
        line = 20
        column = 3
        mass = []
        N = 20
        intervals_of_groups = 0
        for x in range(line):
            mass.append([])
            for y in range(column):
                if y == 0:
                    mass[x].append(random.randint(1, 10))
                else:
                    mass[x].append(random.randint(1000, 50000))
        self.print_grouping(mass, line)
        self.search_max_and_min(mass, line, column)
        self.print_grouping(mass, line)
        quantity = 1 + 3.322 * math.log10(N)
        interval = ((self.max_grouping_one - self.mim_grouping_one) / float(quantity))
        intervals_of_groups = self.mim_grouping_one
        print('\n\n Quantity of groups: ', quantity)
        print('\n\n Interval: ', interval)
        print('Groups:\n')
        for step in range(int(quantity)):
            print('| ', intervals_of_groups, ' - ', intervals_of_groups + interval)
            intervals_of_groups = intervals_of_groups + interval

        print('| ', self.mim_grouping_one, ' - ', self.mim_grouping_one + interval)


if __name__ == '__main__':
    student = Group()
    student.grouping_part_one()
