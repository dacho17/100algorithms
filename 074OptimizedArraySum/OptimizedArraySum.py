def get_sum_quickly(sequence, frm, til):
    sums = [0]
    for index, num in enumerate(sequence):
        sums.append(num + sums[index])
    return sums[til + 1] - sums[frm]
