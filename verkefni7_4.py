def sum_of_range(start, end, step):
    total_sum = 0
    for i in range(0, (end - start) // step + 1):
        total_sum += (start + i * step)
    return total_sum
