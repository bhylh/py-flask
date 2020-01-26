import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
print(my_array)
print(my_array.shape)
print(my_array[0])
print(my_array[1])

my_array[0] = -1
print(my_array)

my_new_array = np.zeros((5))
print(my_new_array)

my_random_array = np.random.random((5))

print(my_random_array)

my_2d_array = np.zeros((2, 3))
print(my_2d_array)

my_array = np.array([[4, 5], [6, 1]])
print(my_array[0][1])
print(my_array.shape)

a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])

sum = a + b
difference = a - b
product = a * b
quotient = a / b
print("Sum = \n", sum)
print("Difference = \n", difference)
print("Product = \n", product)
print("Quotient = \n", quotient)

matrix_product = a.dot(b)
print("a.dot(b)", matrix_product)

matrix_product = b.dot(a)
print("b.dot(a)", matrix_product)

a = np.array([
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35]
])
print(type(a))
print(a.dtype)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.ndim)
print(a.nbytes)
print(a.dot(a))