import numpy as np
from colorama import init, Fore, Back, Style

## Tutorial de: 
## https://numpy.org/devdocs/user/absolute_beginners.html

init()
def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function 
    but with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)
# ------------------------------------------------------------------



# arrays

a = np.array([1, 2, 3, 4])
print(a[0])
a = np.array([[1, 2, 3, 4],[3, 4, 5, 6]])
print(a[0])

## How to create a basic array
# np.array, np.zeros, np.ones, np.empty, np.arange
# np.linspace
print_with_color('How to create a basic array-----------------', color = Fore.RED, brightness = Style.BRIGHT)
print(np.array([1, 2, 3, 4]))
print(np.zeros((2, 3)))
print(np.ones((3, 3)))
print(np.empty((2, 1)))
print(np.arange(2, 10, 2))
print(np.linspace(0, 10, num = 100))

## Adding, removing, and sorting elements.
# np.sort(), np.concatenate()
# others: argsort, lexsort, searchsorted, partition.

print_with_color('Adding, removing and sorting elements-----------------', color = Fore.RED, brightness = Style.BRIGHT)
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr))

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.concatenate((a,b)))


# We can concatenate by different axes o dimensions.
print_with_color('Concatenate  elements-----------------', color = Fore.RED, brightness = Style.BRIGHT)
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
z = np.concatenate((x, y), axis = 0)

print(x.ndim)
print(x.size)
print(x.shape)

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

# How do you know the shape and size of an array
# ndarray.ndim; ndarray.shape; ndarray.size

print_with_color('How we know the shape, dim and size of an array-----------------', color = Fore.RED, brightness = Style.BRIGHT)

print(array_example.ndim)
print(array_example.size)
print(array_example.shape)

# Can you reshape an array
# arr.reshape()
print_with_color('Reshaping an array-----------------', color = Fore.RED, brightness = Style.BRIGHT)

a = np.arange(6)
print(a)
b = a.reshape(2, 3)
print(b)

# How to convert an array of 1D to 2D.
print_with_color('1D to 2D array-----------------', color = Fore.RED, brightness = Style.BRIGHT)
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
a2 = a[np.newaxis, :]
print(a2)
print(a2.shape)
a2 = a[:,np.newaxis]
print(a2)
print(a2.shape)
c = np.expand_dims(a, axis = 0)
print(c.shape)

# Indexing and slicing
print_with_color('Indexing and slicing-----------------', color = Fore.RED, brightness = Style.BRIGHT)
data = np.array([1, 2, 4])
print(data[1])
print(data[0:2])
print(data[1:])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a > 5)
five_up = (a >= 5)
print(a[five_up])
divisible_by_2 = a[a % 2 == 0]
print(divisible_by_2)
c = a[(a < 2) & (a < 11)]
print(c)
