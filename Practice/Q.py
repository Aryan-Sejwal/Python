def seq(q):
    maximum=q[0]
    minimum=q[0]
    for x in q[1:]:
        if x>maximum:
            maximum=x
        elif x<minimum:
            minimum=x
    return maximum , minimum
tupple=(1, 2, 3, 4, 2,)
max,mim=seq(tupple)
print(max    ,    min )
    