import tkinter as tk

from datetime import date

import os

if not os.path.exists("dairy"):
    os.makedirs("dairy")

today = str(date.today())
full_file_path = os.path.join("dairy", today)

root = tk.Tk() 

# --- WINDOW SETUP ---
root.title("todai")
root.geometry("800x700")
root.configure(bg="#9B7E69") 

def save_button_c():
    content = writing_area.get("1.0", tk.END + "-1c")
    with open(f'{full_file_path}', 'w') as page:
        page.write(content)

root.grid_rowconfigure(0, weight=1) 
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)


control_frame = tk.Frame(root, bg="#9B7E69")

control_frame.grid(
    row=0, 
    column=1, 
    rowspan=2,
    padx=(5, 20),
    pady=(20, 20), 
    sticky='ns'
)


control_frame.grid_rowconfigure(100, weight=1)

try:
    with open(r'last_date', 'r') as ld:
        if ld.read() != f"{today}":
            save = tk.Button(
                control_frame, 
                text="     save     ", 
                command=save_button_c,
                bg="#8B4513",
                fg="#FFF8DC",
                font=('Times New Roman', 12, 'bold')
            )

            save.grid(
                row=99,
                column=0, 
                padx=5,
                pady=10,
                sticky='s'
            )

            writing_area = tk.Text(
                root,
                wrap=tk.WORD,
                font=("Times New Roman", 14),
                bg="#F5E9D5", 
                fg="#2A2928", 
                bd=5,
                relief=tk.SUNKEN
            )

            writing_area.grid(
                row=0, 
                column=0, 
                rowspan=2,
                padx=(20, 5),
                pady=(20, 20), 
                sticky='nsew'
            )
        else:
            _all = tk.Label(root, text="YOU HAVE ALREAD WROTE TODAY")
            _all.grid(row=0, column=0, padx=5, pady=5)

except:
    with open(r'last_date', 'w') as ld:
        ld.write(today)
        save = tk.Button(
                control_frame, 
                text="     save     ", 
                command=save_button_c,
                bg="#8B4513",
                fg="#FFF8DC",
                font=('Times New Roman', 12, 'bold')
            )

        save.grid(
                row=99,
                column=0, 
                padx=5,
                pady=10,
                sticky='s'
            )

        writing_area = tk.Text(
                root,
                wrap=tk.WORD,
                font=("Times New Roman", 14),
                bg="#F5E9D5", 
                fg="#2A2928", 
                bd=5,
                relief=tk.SUNKEN
            )

        writing_area.grid(
                row=0, 
                column=0, 
                rowspan=2,
                padx=(20, 5),
                pady=(20, 20), 
                sticky='nsew'
            )


root.mainloop()
