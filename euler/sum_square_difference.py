n = 100

square_of_sum = 0
sum_of_square = 0
for i in range(1,n+1):
    square_of_sum += i**2
    sum_of_square += i


sum_of_square = sum_of_square ** 2
print(f"differnce between Square of sum - sum of squares is {sum_of_square} - {square_of_sum} = ", sum_of_square -square_of_sum)