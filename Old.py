""" Based on Python 3.X; Numpy and Matplotlib are also required.
    This script, by default, will output 6 files totalling ~ 1MB
    Created by Joe Renaud (7/2016)
    www.josephrenaud.com
    Free to use and edit but please keep this header is included. """

# =====================================================================================================================
## TABLE OF CONTENTS ##
#   Topic              Approximate Line #
# Commenting           26
# Input/Output         38
# Basic Math           54
# Comparisons          77
# If/Else              90
# Lists                114
# Tuples               147
# Dictionaries         169
# Printing & Strings   192
# For/While            219
# Numpy                270
# Matplotlib           318
# =====================================================================================================================


# =====================================================================================================================
# Commenting
# =====================================================================================================================

# These are comments.
# They will not be read by the interpretor.

""" This is a
Multi-line
Comment.
"""

# =====================================================================================================================
# Basic Input/Output
# =====================================================================================================================
# "print" is a built-in function of python that takes unlimited arguments and prints them to the terminal.
# You can always tell a function by the () after the word.

print("Welcome!")
# name = input("What is your name?\n")  # "\n" creates a new line, like a return.
# print("Hello,", name)  # Print function can be given many arguments seperated by commas. It will automatically input spaces between these.

# The "" designate that Welcome is a String. You can add strings together
#print("Hi" + "There")
print("Hi" + " There")
#print("It is " + 84 + " degrees today.")  # Remove the first "#" to see an error
print("It is " + str(84) + " degrees today.")  # str() is another built-in function of Python.

# =====================================================================================================================
# Basic Math
# =====================================================================================================================
print("\n\nHere is a bunch of Math!\n")
x = 2
y = 3
print("x =", x, "y =", y)
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("Modulus x % y =", x % y)
print("Floor Divide: x // y =", x // y)
print("-x =", -x)
print("|-x| = ", abs(-x))
print("x^y = ", x**y)

print("\nBeware of the float!")
print("6.0/2.0 =", 6.0/2.0)
print("0.6/0.2 =", 0.6/0.2)
print("6.0/2.0 equals 0.6/0.2?", 6.0/2.0 == 0.6/0.2)
print("0.6//0.2 =", 0.6//0.2)

# =====================================================================================================================
# Comparisons
# =====================================================================================================================
print("\nComparisons")
print("6 > 2:", 6 > 2)
print("6 >= 2:", 6 >= 2)
print("6 < 2:", 6 < 2)
print("6 <= 2:", 6 <= 2)
print("6 equals 2:", 6 == 2)
print("6 not equals 2:", 6 != 2)
print("\nHello equals Hello:", "Hello" == "Hello")
print("\nHello equals hello:", "Hello" == "hello")

# =====================================================================================================================
# If Statements
# =====================================================================================================================
print("\nIf, else, else ifs.")
if 6 == 2:
    print("6 = 2!")
else:
    print("6 does not equal 2 :(")
print("----- ----- -----\n")

number = 2
# number = 6
if 6 < number:
    print("6 is less than", number)
elif 6 > number:
    print("6 is greater than", number)
elif 6 >= number:
    print("6 is >= to", number)
elif 6 <= number:
    print("6 is <= to", number)
else:
    print("6 is equal to", number)


# =====================================================================================================================
# Lists: Store multiple values
# =====================================================================================================================
print("\nLists")
my_list = [1,2,3,4]
print("my list:", my_list)
print("It has", len(my_list), "members.")
my_list.append(10)
print("I can add 10 to it:", my_list)
for item in my_list:
    print("This item is", item)

for i, item in enumerate(my_list):
    print("Item", i, "is", item)

print("Item 0:", my_list[0])
print("Items 2 to end:", my_list[2:])
print("Items 2 to 2nd from end:", my_list[2:-1])
print("Skip Every Other Item:", my_list[0::2])
print("Skip Every Other Item (Evens):", my_list[1::2])
print("My original list", my_list[:], "Or I can just do:", my_list)
# Lists can be changed (we say that lists are "mutable")
my_list[0] = 1000
print(my_list)
my_list[0:2] = [20, 25]
print(my_list)
# Notice that the slice is EXCLUSIVE (the value in spot "2" did not change)

# All members do not need to be of the same type (aka: all integers)
t = "Blue"
my_new_list = [1, 2, 3, 2/3, "Hi There", t]
print("\n", my_new_list)

# =====================================================================================================================
# Tuples: like lists but are immutable (can not be changed after creation), and are useful for assignments.
# =====================================================================================================================
my_tuple = (1, 2, 3, 4)
print("\n\nMy Tuple:", my_tuple)

# Slicing is the same
print("Item 0:", my_tuple[0])
print("Items 2 to end:", my_tuple[2:])
print("Items 2 to 2nd from end:", my_tuple[2:-1])
print("Skip Every Other Item:", my_tuple[0::2])
print("Skip Every Other Item (Evens):", my_tuple[1::2])
print("My original list", my_tuple[:], "Or I can just do:", my_tuple)

# But no post-creation assignment
#my_tuple[0] = 1000  # Get rid of the "#" to see an error.

# Assign other variables quickly
x, y, z, q = my_tuple
print('My tuple:', my_tuple)
print('x =', x, 'y =', y, 'z =', z, 'q =', q)

# =====================================================================================================================
# Dictionaries: mutable, have both a key and a corresponding value.
# =====================================================================================================================
my_dictionary = {'key1': 100}
print('\n\nMy dictionary:', my_dictionary)
print('key1:', my_dictionary['key1'])

# Change value
my_dictionary['key1'] =  200

# Add new values
my_dictionary['key2'] = 300

# Values can be nearly any python object.
my_dictionary['key3'] = [1, 2, 3]
my_dictionary['key4'] = {'sub_key1': 100, 'sub_key2': -100}

# Keys can be many things too
my_dictionary[10] = 'apples'
my_dictionary['This is a really dumb key that you should never use'] = 'oranges'
print('\nMy new dictionary:\n', my_dictionary)
print('my subkey:', my_dictionary['key4']['sub_key1'])

# =====================================================================================================================
# More On Printing
# =====================================================================================================================
x = 'Hi'
y = 10
z = 10.0
print('\n')
print('x = %s,  y = %i, z = %f' % (x, y, z))
print('x = {},  y = {}, z = {}'.format(x, y, z))  # Notice how format automatically cleaned up our float
z = 10.00002
print('x = {},  y = {}, z = {}'.format(x, y, z))

# The . is accessing the string's object attributes and/or methods. This is a more advanced topic for another day.
#     In short: strings have a method, or function, called "format" that achives the above result.

# Many built-in functions have optional keyword arguments. See the difference below
print("I don't like ")
print("this.")
print("I don't like ", end="")
print("this.")

print('\n')
x = ['this','is','a','list','of','words']
print(' '.join(x))
print('-~-'.join(x))
print('\n\n')

# =====================================================================================================================
# For/while loops
# =====================================================================================================================
# Used to do some action multiple (or infinite times)
for i in range(10):
    print(i)

print('\n')
for i in range(3, 5):
    print(i-1)

print('While Loops:')
i = 0
while i < 10:
    print('{}, '.format(i), end='')
    i += 1

print('\n')
for i in range(15):
    if i%2 == 0:
        print('{}, '.format(i), end='')

print('\n')
loop_list = [1, 2, 3, 'potato']
for item in loop_list:
    print(item)

print('\n')
loop_list = [1, 2, 3, 'potato']
for spot, item in enumerate(loop_list):
    print('Item #{} is {}'.format(spot, item))

print('\n')
loop_list_2 = [1, [1, 2, 3]]
for item in loop_list_2:
    print(item)
    if type(item) == type(['dummy', 'list']):
        print('I found a sublist!')
        for sub_item in item:
            print('   ', sub_item)

print('\n')
# "infinite loops"
while True:
    # This will run forever unless we break out of it.
    test = input('enter 1 to break out: ')
    if test == '1' or test in ['q', 'quit', 'exit']:
        break
    else:
        print('Here we go again...')

# =====================================================================================================================
# Science with Python
# =====================================================================================================================
import numpy as np

# Numpy Arrays
my_array = np.random.rand(3)
print('my numpy array: {}'.format(my_array))
my_array = np.random.rand(3, 3)
print('my new numpy array:\n{}'.format(my_array))
# numpy arrays act like matrices
print('spot 1,1: {}. spot 2,1: {}\n\n'.format(my_array[1,1], my_array[2,1]))
my_array = np.asarray([1, 2, 5])  # asarray converts a python list into a numpy array.
print('2 * my array = {}\nmy array ^ 2 = {}'.format(2*my_array, my_array**2))
for i in my_array:
    print(i)
print('\n\n')
matrix_1 = np.asarray([[1, 2],
                      [6, 7]])
matrix_I = np.asarray([[1, 0],
                      [0, 1]])
matrix_2 = np.asarray([[2, 1],
                      [1, 2]])
print('\n\nI*1 =\n{}\nI*2 =\n{}\n1*2 =\n{}\n2*1 =\n{}\n\n'.format(np.dot(matrix_I, matrix_1),
                                                                  np.dot(matrix_I, matrix_2),
                                                                  np.dot(matrix_1, matrix_2),
                                                                  np.dot(matrix_2, matrix_1)))

my_array   = np.asarray([1, 2, 5])
my_array_2 = np.asarray([2, 2, 2])
print('Mean 1: {}. Mean 2: {}'.format(np.mean(my_array),
                                      np.mean(my_array_2)))

#print('Dot: {}. Cross: {}'.format(np.dot(my_array, my_array_2),
#                                  np.cross(my_array, my_array_2)))  # Get rid of first # to see an error

print('Dot: {}. Cross: {}'.format(np.dot(my_array, my_array_2),
                                  np.cross(my_array, my_array_2)))
print('Matrix 1:\n{}\nMatrix 1 Transpose:\n{}\n\n'.format(matrix_1,
                                                          np.transpose(matrix_1)))

np.savetxt('my_array.txt', my_array, fmt="%d", delimiter='\t', header='x\ty\tz')

# If you don't care about human readability this is much faster for large datasets:
np.save('my_matrix_binary', matrix_1)
new_matrix = np.load('my_matrix_binary.npy')
print('Old Matrix:\n{}\nNew Matrix:\n{}'.format(matrix_1,
                                                new_matrix))
# =====================================================================================================================
# Plotting
# =====================================================================================================================
import matplotlib.pyplot as plt

############################# OPTIONAL ########################################
# Comment out these next two lines if you do not have a latex engine installed
plt.rc('text', usetex=True)
font = {'family' : 'serif',
        'size'   : 14}


plt.rc('font', **font)
###############################################################################

x = np.arange(-5, 5, 0.1)
y = x**2

# Get figure and "axis" objects
figure, axis = plt.subplots(figsize=(6,3))

# Make three different plots on the same "axis"
axis.plot(x, x**2, 'blue', label='$t^{2}$')
axis.plot(x, x**3, 'red', label='$t^{3}$')
axis.plot(x, x**4, 'green', label='$t^{4}$')

# Set y-axis limits
axis.set_ylim([-5, 10])

# Set x,y titles
axis.set_xlabel('Time [s]')
axis.set_ylabel('Unknown Parameter, $\gamma_{2}$')

# Change Scaling
#axis.set_yscale('log')

# Show legend
axis.legend(loc='best')

# Show the plot.
plt.show()

# Save the figure
figure.savefig('my_figure.png', format='png', bbox_inches='tight')
# The pdf save may not work if you do not have vector graphics software installed.
figure.savefig('my_figure.pdf', format='pdf', bbox_inches='tight')

# =====================================================================================================================
# Contour Plotting
# =====================================================================================================================

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)

x_len = len(x)
y_len = len(y)

z = np.outer(x, y)

# Add in some noise
z = z + 10*np.random.rand(x_len, y_len)

# Switches
coarse = False

if coarse:
    # Number of plot levels (is this number + 1)
    N = 4
else:
    N = 25

from matplotlib import gridspec
# Figure acts as a master container for everything that follows.
figure_2 = plt.figure(figsize=(6,6))
# Setup a gridspace so we can have more than 1 plot.
gs = gridspec.GridSpec(2, 2, height_ratios=(3, 1), width_ratios=(9, 1), hspace=0.4)
fig2_axis_1 = plt.subplot(gs[0,0])


# Filled Contour
ct = fig2_axis_1.contourf(x, y, z, N)

# Labels
fig2_axis_1.set_xlabel('X-Coord [m]')
fig2_axis_1.set_ylabel('Y-Coord [m]')

# Make a colorbar for the ContourSet returned by the contourf call.
fig2_CB_axis = plt.subplot(gs[0,1])
cbar = plt.colorbar(ct, cax=fig2_CB_axis)

# Color bar label
cbar.ax.set_ylabel('Intensity, I, [W m$^{-2}$]')

# =====================================================================================================================
# Contour Sub Plot
# =====================================================================================================================

fig2_axis_2 = plt.subplot(gs[1,0])
# Couples of subplots
#   The rounds in the label names are so a bunch of digits don't show. I am rounding to the tenths place.
fig2_axis_2.plot(x, z[:, 25], 'g', label='y={}'.format(round(y[25]*10)/10))
fig2_axis_2.plot(x, z[:, 50], 'b:', label='y={}'.format(round(y[50]*10)/10))
fig2_axis_2.plot(x, z[:, 75], 'r', label='y={}'.format(round(y[75]*10)/10))
fig2_axis_2.set_ylim([-30, 30])
# Labels
fig2_axis_2.set_xlabel('X-Coord [m]')
fig2_axis_2.set_ylabel('I')
# Legend
fig2_axis_2.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0)
plt.show()

# Save
figure_2.savefig('my_contour.png', format='png', bbox_inches='tight')
# The pdf save may not work if you do not have vector graphics software installed.
figure_2.savefig('my_contour.pdf', format='pdf', bbox_inches='tight')