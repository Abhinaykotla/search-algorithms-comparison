from search_algorithms import *
import random
import time
import subprocess

def start_search():
        
    input_size = int(input("Enter the size of the array: "))
    input_array = []


    choice = input("Enter M for manual input or R for random array: ")

    if choice == "M" or choice == "m":
        for i in range(input_size):
            input_array.append(int(input()))
    else:
        input_array = [random.randint(-9999,9999) for i in range(input_size)]

    print("Input array: ", input_array)

    key_to_find = int(input("Enter the key to find: "))


    # Linear search
    start_time = time.perf_counter()
    LS_res = linear_search(input_array, key_to_find)
    end_time = time.perf_counter()

    time_taken = end_time - start_time
    if LS_res == -1:
        print(f"Linear Search: {key_to_find} not found in the array, time taken: {time_taken} seconds")

    else:
        print(f"Linear Search: Found {key_to_find} at index {LS_res} in {time_taken} seconds")

    # Binary search in a sorted array

    sorted_input_array = sorted(input_array)

    start_time = time.perf_counter()
    BSSA_res = binary_search_in_sorted_array(sorted_input_array,key_to_find)            
    end_time = time.perf_counter()

    time_taken = end_time - start_time
    if BSSA_res == -1:
        print(f"Binary Search in a sorted array: {key_to_find} not found in the array, time taken: {time_taken} seconds")

    else:
        print(f"Binary Search in a sorted array: Found {key_to_find} at index {BSSA_res} (index after sorting the array) in {time_taken} seconds")

    # Binary search tree

    root = array_to_bst(input_array)

    start_time = time.perf_counter()
    BST_res = search_binary_search_tree(root, key_to_find)
    end_time = time.perf_counter()

    time_taken = end_time - start_time
    if BST_res == None:
        print(f"Binary Search Tree: {key_to_find} not found in the array, time taken: {time_taken} seconds")

    else:
        print(f"Binary Search Tree: Found {key_to_find} in the binary search tree in {time_taken} seconds")

    # Red black tree

    RB_root = build_RBtree(input_array)

    start_time = time.perf_counter()
    RBT_res = search_RB_tree(RB_root, key_to_find)
    end_time = time.perf_counter()

    time_taken = end_time - start_time
    if RBT_res == None:
        print(f"Red Black Tree: {key_to_find} not found in the array, time taken: {time_taken} seconds")

    else:
        print(f"Red Black Tree: Found {key_to_find} in the RB-Tree in {time_taken} seconds")

start_search()

restart_program = input("Do you want to restart the program? (Y/N): ")
while restart_program == "Y" or restart_program == "y":
    subprocess.call(['python', 'main.py'])
    restart_program = input("Do you want to restart the program? (Y/N): ")