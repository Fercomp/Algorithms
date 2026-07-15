def exclusiveTime(n, logs):
    times = [0] * n
    time_spended = 0
    stack = []

    for log in logs:
        l = log.split(":")

        if l[1] == "start":
            stack.append(l)

        else:
            start_log = stack.pop()
            func_interval = int(l[2]) - int(start_log[2]) + 1
            times[int(l[0])] += func_interval - time_spended
            time_spended += func_interval

    return times

exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"])