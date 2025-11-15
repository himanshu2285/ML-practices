def square(x):
    return x * x
lst = [1, 2, 3, 4, 5]
squared_lst = list(map(square, lst))
print(squared_lst)
