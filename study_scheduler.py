def make_schedule(time_est, time_remaining, start_time=12, fudge_ratio=2.0):
    # First, we compensate for planning fallacy
    time_needed = time_est * fudge_ratio
    # We then calculate the sleep requirements and available slack
    sleep_need = 8 * (time_remaining // 24)
    # print(f'Sleep need: {sleep_need}')
    slack = time_remaining - time_needed - sleep_need
    slack_ratio = slack / time_remaining
    # Next, we use a Pomodoro scheme to create work/break bins
    bins = int(2 * (time_remaining - sleep_need))
    bin_assignments = []
   
    time_stamp = float(start_time)
    for i in range(bins):
        btype = 'Revise'
        if i%3 == 0:
            btype = 'Break'
        if i%6 == 0:
            btype = 'Food'
        if i%12 == 0:
            btype = 'Exercise'
        if i == 0:
            btype = 'Revise'
        bin_assignments.append(f'From {time_stamp} to {time_stamp + 0.5}, {btype}')
        time_stamp += 0.5
    return bin_assignments
