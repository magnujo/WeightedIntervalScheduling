class Job:
    def __init__(self, start, finish, profit, index):
        self.start = start
        self.finish = finish
        self.profit = profit
        self.index = index

    def print(self):
        print("Start:  ", self.start)
        print("Finish: ", self.finish)
        print("Profit: ", self.profit)

    def isOverlapping(self, that):
        if self.finish > that.start:
            return True
        else:
            return False


j1 = Job(1, 2, 3, 0)
j2 = Job(3, 4, 2, 1)
j3 = Job(2, 5, 3, 2)
j4 = Job(1, 6, 6, 3)
j5 = Job(4, 7, 10, 4)

jobs = [j1, j2, j3, j4, j5]


def p(jlist, index):
    i = index
    while i >= 0:
        if jlist[index].isOverlapping(jobs[i]):
            print("if")
            i -= 1
        else:
            print("else")
            return i
    print("end")
    return 0


print(p(jobs, 4))










