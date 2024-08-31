# Importing the necessary libraries
import time

# Define a function to demonstrate the operation and time complexity of a hash set
def compare_operations():
    
    # Create a list and a set
    data_list = []
    data_set = set()

    # Adding elements to list and set
    for i in range(10**6):
        data_list.append(i)
        data_set.add(i)

    # Set and List are ready; now let's define a non-existing item to search for
    test_item = 10**6 + 1  # This item is not in our set or list

    # TODO: Time the 100 consecutive operations of checking whether `test_item` is in `data_set` and print the result and time taken
    start_time_set = time.time()
    for _ in range(100):
        _=test_item in data_set
    end_time_set = time.time()
    set_time_taken = end_time_set - start_time_set
    print(f"Operation time for 'in' operation in set: {set_time_taken:.6f} seconds")
    # TODO: Time the 100 consecutive operations of checking whether `test_item` is in `data_list` and print the result and time taken
    start_time_list = time.time()
    for _ in range(100):
        _ = test_item in data_list
    end_time_list = time.time()
    list_time_taken = end_time_list - start_time_list
    print(f"Operation time for 'in' operation in list: {list_time_taken:.6f} seconds")
# Execute the function
compare_operations()