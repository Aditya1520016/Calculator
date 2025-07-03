import tkinter as tk

#COLORS AND STYLES
BG_COLOR = "#2D2F31"
BTN_COLOR = "#393B3D"
BTN_HOVER = "#505254"
TEXT_COLOR = "#FFFFFF"
ENTRY_BG = "#1E1E1E"
FONT = ("Segoe UI", 18)

# MAIN APP
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("350x500")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# ENTRY DISPLAY
entry = tk.Entry(root, font=("Segoe UI", 24), bg=ENTRY_BG, fg=TEXT_COLOR, border=0, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=(20, 10), padx=10)

# BUTTON FRAME 
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(expand=True, fill='both')

# BUTTON LAYOUT
buttons = [
    ["C", "←", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

#BUTTON CLICK FUNCTION 
def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "←":
        entry.delete(len(entry.get()) - 1)
    else:
        entry.insert(tk.END, text)

# BUTTON CREATION 
for row in buttons:
    row_frame = tk.Frame(btn_frame, bg=BG_COLOR)
    row_frame.pack(expand=True, fill="both", padx=10, pady=5)
    for btn_text in row:
        if btn_text == "":
            tk.Label(row_frame, text="", bg=BG_COLOR).pack(side="left", expand=True, fill="both")
            continue
        btn = tk.Label(
            row_frame,
            text=btn_text,
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            font=FONT,
            width=4,
            height=2,
            relief="flat",
            cursor="hand2"
        )
        btn.pack(side="left", expand=True, fill="both", padx=4, pady=2)
        btn.bind("<Button-1>", on_click)
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg=BTN_HOVER))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg=BTN_COLOR))

#START
root.mainloop()
