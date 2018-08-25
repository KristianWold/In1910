def less_than(original,n):
    N = len(original)
    return [original[i] for i in range(N) if original[i]<n]
