# -*- coding: UTF-8 -*-
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

squares = [value**3 for value in range(2,12)]
print(squares)
