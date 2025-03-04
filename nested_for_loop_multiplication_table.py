# MARKJOHN OBIAS
# Week 04 - looping Statements
# Laboratory # 14 - Guided Coding Exercise: Nested for Loop to Print a Multiplication Table

for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{product:4}", end="")  # Prints with spacing for alignment
    print()  # Moves to the next line after inner loop
