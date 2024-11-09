import subprocess
import customtkinter as ctk

def run_cli():
    subprocess.call(['python', 'CLI.py'])

def run_gui():
    subprocess.call(['python', 'GUI.py'])

def run_compare():
    subprocess.call(['python', 'graph_comparison.py'])


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Search Algorithms")
app.geometry("600x400")


compare_text = "Compare using Graph\nCompare the performance of different search algorithms using a graph."
gui_text = "Run GUI\nRun the GUI version of the search algorithms.\n Works best for small input sizes."
cli_text = "Run CLI\nRun the CLI version of the search algorithms.\n Works best for large input sizes."

button_frame = ctk.CTkFrame(app)

compare_button = ctk.CTkButton(button_frame, text=compare_text, command=run_compare, width=30, height=10)
gui_button = ctk.CTkButton(button_frame, text=gui_text, command=run_gui, width=30, height=10)
cli_button = ctk.CTkButton(button_frame, text=cli_text, command=run_cli, width=30, height=10)


gui_button.grid(row=0, column=0, padx=10, pady=10)
cli_button.grid(row=1, column=0, padx=10, pady=10)
compare_button.grid(row=2, column=0, padx=10, pady=10)

button_frame.place(relx=0.5, rely=0.5, anchor='center')

app.mainloop()