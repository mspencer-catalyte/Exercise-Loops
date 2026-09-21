#Test Data
#Your code must be verified against these three specific lists:
#List 1: [10, 20, 30, 40, 50]
#List 2: [5, -3, 12, 0, -8]
#List 3: [100, 250, 75, 420, 130]

#Requirements
#All code for the project exists in a file named main.py.
#Initialize three lists named data_set_1, data_set_2, and data_set_3 
# using the provided test data.
#
data_set_1 = [10, 20, 30, 40, 50]
data_set_2 = [5, -3, 12, 0, -8]
data_set_3 = [100, 250, 75, 420, 130]

data_table = [data_set_1, data_set_2, data_set_3]



   
# Assign data_set_1 to a variable named numbers for use in your calculations.
numbers = data_set_1
# Print all of the numbers in the numbers list.
def print_list(array):
    
    print("\r")
    print("Current List:")
    for item in array:
        print(item)
    print("\r")  

#print_list(numbers)
# Find and print the sum of all numbers in the list without using 
# the sum() function.
def sum_array(array):
    total = 0
    for item in array:
       total = total + item
    return total 

#print("Total of current list is: " + str(sum_array(numbers)))
# 
# Calculate and print the average of the numbers.
def avg_array(array):
    total = sum_array(array)
    count = 0
    for item in array:
        count = count + 1
    return(total/count)

#print("Average of current list is: " + str(avg_array(numbers)))

# Determine and print the smallest number in the list without using the 
# min() function.
def min_array(array):
    min = array[0]
    for item in array:
        if item < min:
            min = item
        else:
            pass
    return min

#print("Min of current list is: " + str(min_array(numbers)))

# Determine and print the largest number in the list without using the 
# max() function.
def max_array(array):
    max = array[0]
    for item in array:
        if item > max:
            max = item
        else:
            pass
    return max

#print("Max of current list is: " + str(max_array(numbers)))
#
# Print a single string using an f-string formatted exactly as: "Sum: [total_sum],
# Average: [average], Smallest: [smallest], Largest: [largest]".
#
print("Sum: " + str(sum_array(numbers)) + ", Average: " + str(avg_array(numbers)) + ", Smallest: " + str(min_array(numbers)) + ", Largest: " + str(max_array(numbers)))

# Leaving your original code the way it is (it's fine to copy and paste), create 
# a function that takes a list as a parameter and performs steps 3 through 8.
#
def array_stats(array):
    print("Sum: " + str(sum_array(array)) + ", Average: " + str(avg_array(array)) + ", Smallest: " + str(min_array(array)) + ", Largest: " + str(max_array(array)))

# Invoke the function three times, once for each list in the Test Data. 
# The final result of the program is two prints for list 1 
# (one from your original code in step 9, one from the function), 
# one print for list 2, 
# and one print for list 3.

for list in data_table:
    numbers = list
    array_stats(numbers)