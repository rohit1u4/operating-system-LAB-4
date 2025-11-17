# ------------------ FCFS ------------------
def fcfs(burst_times):
    wt = [0] * len(burst_times)
    tat = [0] * len(burst_times)

    for i in range(1, len(burst_times)):
        wt[i] = wt[i-1] + burst_times[i-1]

    for i in range(len(burst_times)):
        tat[i] = wt[i] + burst_times[i]

    return wt, tat


# ------------------ SJF ------------------
def sjf(burst_times):
    indexed = list(enumerate(burst_times))
    indexed.sort(key=lambda x: x[1])

    wt = [0]*len(burst_times)
    tat = [0]*len(burst_times)

    current = 0
    for pid, bt in indexed:
        wt[pid] = current
        tat[pid] = current + bt
        current += bt

    return wt, tat


# ------------------ Priority ------------------
def priority_scheduling(burst_times, priority):
    indexed = list(enumerate(zip(burst_times, priority)))
    indexed.sort(key=lambda x: x[1][1])  # sort by priority value

    wt = [0]*len(burst_times)
    tat = [0]*len(burst_times)

    current = 0
    for pid, (bt, pr) in indexed:
        wt[pid] = current
        tat[pid] = current + bt
        current += bt

    return wt, tat


# ------------------ Round Robin ------------------
def round_robin(burst_times, quantum):
    remaining = burst_times[:]
    n = len(burst_times)
    t = 0
    wt = [0]*n
    tat = [0]*n
    done = False

    while not done:
        done = True
        for i in range(n):
            if remaining[i] > 0:
                done = False
                if remaining[i] > quantum:
                    t += quantum
                    remaining[i] -= quantum
                else:
                    t += remaining[i]
                    wt[i] = t - burst_times[i]
                    remaining[i] = 0

    for i in range(n):
        tat[i] = wt[i] + burst_times[i]

    return wt, tat


# ------------------ MAIN PROGRAM ------------------
if __name__ == "__main__":
    print("----- CPU Scheduling Algorithms -----")
    n = int(input("Enter number of processes: "))

    burst = []
    for i in range(n):
        burst.append(int(input(f"Enter burst time for P{i+1}: ")))

    print("\nFCFS Scheduling:")
    wt, tat = fcfs(burst)
    print("WT =", wt)
    print("TAT =", tat)

    print("\nSJF Scheduling:")
    wt, tat = sjf(burst)
    print("WT =", wt)
    print("TAT =", tat)

    print("\nPriority Scheduling:")
    priority_list = []
    for i in range(n):
        priority_list.append(int(input(f"Enter priority for P{i+1}: ")))
    wt, tat = priority_scheduling(burst, priority_list)
    print("WT =", wt)
    print("TAT =", tat)

    print("\nRound Robin Scheduling:")
    quantum = int(input("Enter time quantum: "))
    wt, tat = round_robin(burst, quantum)
    print("WT =", wt)
    print("TAT =", tat)
