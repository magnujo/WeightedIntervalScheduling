import bisect
import sys


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


def parseAndSort():
    l = []
    for i in range(int(input())):
        s, f, w = input().split()
        l.append((int(s), int(f), int(w)))
    l.sort(key=lambda x: x[1])
    print(l)
    return l







def previousIntervals (jlist):
    p = []
    start = [job[0] for job in jlist]
    end = [job[1] for job in jlist]
    # end = [2, 4, 5, 6, 7]
    # start [1, 3, 2, 1, 4]
    # p = [-1, 0, 0, -1, 1]
    for i in range(len(jlist)):
        index = bisect.bisect(end, start[i]) - 1
        p.append(index)
    print(p)
    return p


def M_Compute_Opt(j):
    if j == -1:
        return 0

    elif (0 <= j) and (j < len(M)):
        return M[j]

    else:
        return max(jobs[j][2] + M_Compute_Opt(p[j]), M_Compute_Opt(j - 1))

def Find_Solution(j):
    if j == -1:
        return
    else:
        if jobs[j][2] + M[p[j]] >= M[j - 1]:
            O.append(jobs[j])
            Find_Solution(p[j])
        else:
            Find_Solution(j-1)

def Compute_Opt(j):
    if j == -1:
        return 0
    else:
        return max(jobs[j][2] + Compute_Opt(p[j]), Compute_Opt(j - 1))

def bestJobs(jobslist):
    for i in range(len(jobslist)):
        res = M_Compute_Opt(i)
        M.append(res)

    Find_Solution(len(jobslist) - 1)
    return M[-1]


if __name__ == '__main__':

    M = []
    O = []

    jobs = parseAndSort()
    p = previousIntervals(jobs)
    max = bestJobs(jobs)

    print("Best jobs: ", O[::-1])
    print("Max: ", max)



















