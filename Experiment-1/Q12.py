print("A B  A&B  A|B  A^B")
print("--------------------")

for A in [0, 1]:
    for B in [0, 1]:
        print(A, B, " ", A & B, "   ", A | B, "   ", A ^ B)
