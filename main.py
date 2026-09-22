
data_set_1 = [10, 20, 30, 40, 50]
data_set_2 = [5, -3, 12, 0, -8]
data_set_3 = [100, 250, 75, 420, 130]

data_table = [data_set_1, data_set_2, data_set_3]

numbers = data_set_1

def array_valid(array):
    """Checks if the array is valid"""
    check = True
    for item in array:
        if type(item) is str:
            check = False
            print("This list is not valid.")
        else:
            pass
    return check 
 
def print_list(array):
    """Prints all of the numbers in the numbers list."""
    
    print("\r")
    print("Current List:")
    print(*array, sep = ", ")  

print_list(numbers)

def sum_array(array):
    """Finds and prints the sum of all numbers in the list without using 
         the sum() function."""
    
    total = 0
    for item in array:
        total = total + item
    return total 
   

print(f"Total of current list is: {sum_array(numbers)}")

def avg_array(array):
    """Calculate and print the average of the numbers."""
    
    total = sum_array(array)
    count = 0
    for item in array:
        count = count + 1
    return round(total/count,3)
    

print(f"Average of current list is: {avg_array(numbers)}")

def min_array(array):
    """ Determine and print the smallest number in the list without using the 
           min() function."""
    
    min = array[0]
    for item in array:
        if item < min:
            min = item
        else:
            pass
    return min


print(f"Min of current list is: {min_array(numbers)}")

def max_array(array):
    """Determines and prints the largest number in the list without using the 
         max() function."""
    
    max = array[0]
    for item in array:
        if item > max:
            max = item
        else:
            pass
    return max

print(f"Max of current list is: {max_array(numbers)}")

print (f"Sum: {sum_array(numbers)}, Average: {avg_array(numbers)}, Smallest: {min_array(numbers)}, Largest: {max_array(numbers)}")

def array_stats(array):
    """Prints a single string using an f-string formatted exactly as: "Sum: [total_sum],
       Average: [average], Smallest: [smallest], Largest: [largest]"."""
    print (f"Sum: {sum_array(numbers)}, Average: {avg_array(numbers)}, Smallest: {min_array(numbers)}, Largest: {max_array(numbers)}")


for list in data_table:
    numbers = list
    if array_valid(numbers):
        array_stats(numbers)