import bisect


def parseAndSort():
    l = []
    for i in range(int(input())):
        s, f, w = input().split()
        l.append((int(s), int(f), int(w)))
    l.sort(key=lambda x: x[1])
    return l

def previousIntervals (jlist):
    p = []
    start = [job[0] for job in jlist]
    end = [job[1] for job in jlist]
    for i in range(len(jlist)):
        index = bisect.bisect(end, start[i]) - 1
        p.append(index)
    return p


def M_Compute_Opt(j):
    if j == -1:
        return 0

    elif (0 <= j) and (j < len(M)):
        return M[j]

    else:
        return max(jobs[j][2] + M_Compute_Opt(p[j]), M_Compute_Opt(j - 1))

def bestJobs(jobslist):
    for i in range(len(jobslist)):
        res = M_Compute_Opt(i)
        M.append(res)

    return M[-1]


if __name__ == '__main__':

    M = []
    O = []

    jobs = parseAndSort()
    p = previousIntervals(jobs)
    max = bestJobs(jobs)

    print(max)



















