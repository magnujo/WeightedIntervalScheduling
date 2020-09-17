class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

    def print(self):
        print("Start:  ", self.start)
        print("Finish: ", self.finish)
        print("Profit: ", self.profit)


j1 = Job(1, 2, 3)

j1.print()
