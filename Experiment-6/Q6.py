def max_min(seq):
    maximum=seq[0]
    minimum=seq[0]
    for x in seq[1:]:
        if x>maximum:
            maximum=x
        if x<minimum:
            minimum=x
    return maximum , minimum
tuple=(95,43,1,0,56,3,-2)
max,min=max_min(tuple)
print(max   ,  min)