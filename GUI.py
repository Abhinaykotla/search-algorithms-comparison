import customtkinter as ctk
import tkinter 
import random
import time
from search_algorithms import *

def validate_input(input_str):
    return input_str.isdigit() or input_str == ""

def start_search():
    # get inputs and validae them, convert them to the right type

    # input size
    input_size = int(input_size_var.get())
    if input_size < 1:
        output_content_label.configure(text="Input size cannot be less than 1")
        output_content_label.pack(pady=10, padx=1)
        return

    input_array = list(map(int, array_input_box.get("1.0", tkinter.END).strip('[]\n').split(',')))

    if len(input_array) == 0:
        print("Input array cannot be empty")
        output_content_label.configure(text="Input array cannot be empty")
        output_content_label.pack(pady=10, padx=1)
        return

    if len(input_array) != input_size:
        print("Input size and input array size do not match")
        print("New input size: ", len(input_array))

    key_to_find = int(key_to_find_var.get())

    if switch_var_LSS.get() == "off" and switch_var_BSSAS.get() == "off" and switch_var_BSTS.get() == "off" and switch_var_RBTS.get() == "off":
        print("No algorithm selected")
        return

    LS_Output = ""
    BSSA_Output = ""
    BST_Output = ""
    RBT_Output = ""

    # Linear search
    if switch_var_LSS.get() == "on":

        start_time = time.perf_counter()
        LS_res = linear_search(input_array, key_to_find)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        if LS_res == -1:
            LS_Output = (f"Linear Search: {key_to_find} not found in the array, time taken: {time_taken} seconds")
            
        else:
            LS_Output = (f"Linear Search: Found {key_to_find} at index {LS_res} in {time_taken} seconds")
        
        print(LS_Output)
        
    # Binary search in a sorted array
    if switch_var_BSSAS.get() == "on":

        sorted_input_array = sorted(input_array)

        start_time = time.perf_counter()

        BSSA_res = binary_search_in_sorted_array(sorted_input_array, key_to_find)            
        end_time = time.perf_counter()

        time_taken = end_time - start_time
        if BSSA_res == -1:
            BSSA_Output = (f"Binary Search in a sorted array: {key_to_find} not found in the array, time taken: {time_taken} seconds")
            
        else:
            BSSA_Output = (f"Binary Search in a sorted array: Found {key_to_find} at index {BSSA_res} (index after sorting the array) in {time_taken} seconds")
        print(BSSA_Output)

    # Binary search tree
    if switch_var_BSTS.get() == "on":
        
        root = array_to_bst(input_array)

        start_time = time.perf_counter()
        BST_res = search_binary_search_tree(root, key_to_find)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        if BST_res == -1:
            BST_Output = (f"Binary Search Tree: {key_to_find} not found in the binary search tree, time taken: {time_taken} seconds")
            
        else:
            BST_Output = (f"Binary Search Tree: Found {key_to_find} at {BST_res} in {time_taken} seconds")
        print(BST_Output)

    # Red black tree
    if switch_var_RBTS.get() == "on":
        
        root = build_RBtree(input_array)

        start_time = time.perf_counter()
        RBT_res = search_RB_tree(root, key_to_find)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        if RBT_res == -1:
            RBT_Output = (f"Red Black Tree: {key_to_find} not found in the RB-Tree, time taken: {time_taken} seconds")
            
        else:
            RBT_Output = (f"Red Black Tree: Found {key_to_find} at {RBT_res} in {time_taken} seconds")
        print(RBT_Output)

    output_content_label.configure(text=f"{LS_Output}\n{BSSA_Output}\n{BST_Output}\n{RBT_Output}")
    output_content_label.pack(pady=10, padx=1)


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Search Algorithms")
app.geometry("1050x1030")

input_frame = ctk.CTkFrame(master=app)
input_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)


# Input frame
# input size

input_size_label = ctk.CTkLabel(master=input_frame, text="Input size", font=("Arial", 20))
input_size_label.pack(pady=10, padx=1)

input_size_var = tkinter.StringVar()
input_size_var.set("999")
validatecmd_input_size = (app.register(validate_input), '%P')

input_size_entry = tkinter.Entry(master=input_frame, textvariable=input_size_var, font=("Arial", 15), fg="black", bg="darkgray", bd=5, relief="sunken", justify="center", validate="key", validatecommand=validatecmd_input_size)
input_size_entry.pack(pady=10, padx=1)

# input array

input_array_label = ctk.CTkLabel(master=input_frame, text="Input array", font=("Arial", 20))
input_array_label.pack(pady=10, padx=1)

array_input_box = ctk.CTkTextbox(master=input_frame)
array_input_box.pack(pady=10, padx=10, fill="x")

def randon_input_generator(n):
    random_array = [random.randint(-9999,9999) for i in range(n)]
    array_input_box.delete("1.0", tkinter.END)
    array_input_box.insert("0.0",str(random_array))

random_input_button = ctk.CTkButton(master=input_frame, text="Generate random input", command=lambda: randon_input_generator(int(input_size_var.get())))
random_input_button.pack(pady=10, padx=1)

pick_algo_label = ctk.CTkLabel(master=input_frame, text="Pick algorithms that you want to compare", font=("Arial", 20))
pick_algo_label.pack(pady=10, padx=1)

# select algorithms

switch_var_LSS = ctk.StringVar(value="on")
linear_search_switch = ctk.CTkSwitch(master=input_frame, text="Linear Search", variable=switch_var_LSS, onvalue="on", offvalue="off")
linear_search_switch.pack(pady=10, padx=1)

switch_var_BSSAS = ctk.StringVar(value="on")
binary_search_in_sorted_array_switch = ctk.CTkSwitch(master=input_frame, text="Binary Search in a sorted array", variable=switch_var_BSSAS, onvalue="on", offvalue="off")
binary_search_in_sorted_array_switch.pack(pady=10, padx=1)

switch_var_BSTS = ctk.StringVar(value="on")
binary_search_tree_switch = ctk.CTkSwitch(master=input_frame, text="Binary Search Tree", variable=switch_var_BSTS, onvalue="on", offvalue="off")
binary_search_tree_switch.pack(pady=10, padx=1)

switch_var_RBTS = ctk.StringVar(value="on")
red_black_tree_switch = ctk.CTkSwitch(master=input_frame, text="Red Black Tree", variable=switch_var_RBTS, onvalue="on", offvalue="off")
red_black_tree_switch.pack(pady=10, padx=1)

# Key to find

key_to_find_label = ctk.CTkLabel(master=input_frame, text="Key to find", font=("Arial", 20))
key_to_find_label.pack(pady=10, padx=1)

key_to_find_var = tkinter.StringVar()
key_to_find_entry = tkinter.Entry(master=input_frame, textvariable=key_to_find_var, font=("Arial", 15), fg="black", bg="darkgray", bd=5, relief="sunken", justify="center")
key_to_find_entry.pack(pady=10, padx=1)

# start button

start_button = ctk.CTkButton(master=input_frame, text="Start", font=("Arial", 20), command= lambda: start_search())
start_button.pack(pady=10, padx=1)

output_label = ctk.CTkLabel(master=input_frame, text="Output", font=("Arial", 20))
output_label.pack(pady=10, padx=1)

output_content_label = ctk.CTkLabel(master=input_frame, text="Output will be displayed here", font=("Arial", 15))


app.mainloop()


