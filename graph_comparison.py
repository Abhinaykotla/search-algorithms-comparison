import customtkinter as ctk
import tkinter 
import random
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
from search_algorithms import *


def start_graphs():
    input_sizes = sizes_input_box.get("1.0", tkinter.END).strip('[]\n').split(',')
    input_sizes = [int(size) for size in input_sizes]

    arrays = [[random.randint(-9999, 9999) for n in range(size)] for size in input_sizes]

    key_to_find = 10000

    times_algo1 = []
    times_algo2 = []
    times_algo3 = []
    times_algo4 = []

    for array in arrays:
        start = time.perf_counter()
        linear_search(array, key_to_find)
        end = time.perf_counter()
        times_algo1.append(end - start)

        sorted_input_array = sorted(array)
        start = time.perf_counter()
        binary_search_in_sorted_array(sorted_input_array, key_to_find)
        end = time.perf_counter()
        times_algo2.append(end - start)


        root = array_to_bst(array)
        start = time.perf_counter()
        search_binary_search_tree(root, key_to_find)
        end = time.perf_counter()
        times_algo3.append(end - start)

        RBroot = build_RBtree(array)
        start = time.perf_counter()
        search_RB_tree(RBroot, key_to_find)
        end = time.perf_counter()
        times_algo4.append(end - start)


    times_output_label.configure(text=f"Time taken to search for a key that is not in the array\nInput Size : {input_sizes}\nLinear Search: {times_algo1}\nBinary Search in a sorted array: {times_algo2}\nBinary Search Tree: {times_algo3}\nRed-Black Tree: {times_algo4}")
    times_output_label.pack(pady=10, padx=1)

    fig = Figure(figsize=(5, 5), dpi=100, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(111)

    ax.plot(input_sizes, times_algo1, label="Linear Search")
    ax.plot(input_sizes, times_algo2, label="Binary Search in a sorted array")
    ax.plot(input_sizes, times_algo3, label="Binary Search Tree")
    ax.plot(input_sizes, times_algo4, label="Red-Black Tree")

    ax.set_xlabel("Input size")
    ax.set_ylabel("Time taken")
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0, sticky='nsew', padx=10, pady=20)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Search Algorithms")
app.geometry("1050x900")


input_frame = ctk.CTkFrame(master=app)
input_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

input_sizes_lable = ctk.CTkLabel(master=input_frame, width=10, text="Input sizes", font=("Arial", 20))
input_sizes_lable.pack(pady=10, padx=1)

sizes_input_box = ctk.CTkTextbox(master=input_frame, width=10, height=1, font=("Arial", 20))
sizes_input_box.pack(pady=10, padx=10, fill="x" )

sizes_input_box.insert('1.0', "100,200,300,400,500,600,700,800,900,1000,1100,1200,1300")

input_array_label = ctk.CTkLabel(master=input_frame, text="Input arrays are generated at random and are not sorted. A key that is not in the arrays is used to search the arrays to show the worst case scenario", font=("Arial", 15))
input_array_label.pack(pady=10, padx=1)


start_button = ctk.CTkButton(master=input_frame, text="Start",command= lambda : start_graphs())
start_button.pack(pady=10, padx=1)

times_output_label = ctk.CTkLabel(master=input_frame, text="Time taken to search for a key that is not in the array", font=("Arial", 15))

app.mainloop()