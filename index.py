import tkinter as tk

# ======== CONFIGURABLE SETTINGS ===========
version = "4.0.2"

COLOR_BG = "#FFFFFF"
COLOR_FG = "#212121"
COLOR_BTN_BG_MAIN = "#212121"
COLOR_BTN_BG_OP = "#757575"
COLOR_BTN_AC_BG = "#129688"
COLOR_BTN_FG = "white"

FONT_MAIN = ("Arial", 24)
FONT_BUTTON = ("Arial", 18)

update_log_text = (
    "Update Log:\n\n"
    "Version 1.0.0 - First release\n"
    "Version 1.0.1 - Minor fixes and improvements\n"
    "Version 1.0.2 - Added number formatting with commas\n"
    "Version 2.0.0 - Major UI overhaul and new features\n"
    "Version 3.0.0 - Calculation overhaul & Calculation log added\n"
    "Version 3.0.1 - Text display fixes\n"
    "Version 3.0.2 - Code reformatting & Settings\n"
    "Version 4.0.0 - Fixed negative number handling\n"
    "Version 4.0.1 - Added simple BIDMAS calculation system\n"
    "Version 4.0.2 - Added disclaimer to terminal message\n"
    "\nThank you for using this calculator!"
)

# ======== GLOBALS ========
calculation_history = []
last_expression = ""

# ======== FUNCTIONS ========

def format_number(number_str):
    # Handle negative sign
    negative = False
    if number_str.startswith('-'):
        negative = True
        number_str = number_str[1:]

    parts = number_str.split('.')
    integer_part = parts[0]
    try:
        integer_part_with_commas = f"{int(integer_part):,}"
    except ValueError:
        # If conversion fails (e.g. empty or non-numeric), return original with negative sign if any
        return ('-' if negative else '') + number_str

    if len(parts) > 1:
        if parts[1] == '0':
            formatted = integer_part_with_commas
        else:
            formatted = f"{integer_part_with_commas}.{parts[1]}"
    else:
        formatted = integer_part_with_commas

    if negative:
        formatted = '-' + formatted
    return formatted

def show_update_log():
    width = root.winfo_width()
    height = root.winfo_height()

    update_window = tk.Toplevel(root)
    update_window.title("Update Log")
    update_window.geometry(f"{width}x{height}")
    update_window.resizable(False, False)

    # Match color theme
    update_window.configure(bg=COLOR_BG)

    text_widget = tk.Text(update_window, wrap="word", font=FONT_BUTTON,
                          bg=COLOR_BG, fg=COLOR_FG, bd=0, relief="flat")
    text_widget.insert("1.0", update_log_text)
    text_widget.config(state="disabled")
    text_widget.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(update_window, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar.set)

def click_button(value):
    global last_expression
    current_text = entry_label['text']

    # Reset if Error or empty display
    if current_text == "Error" or current_text == "":
        # Allow starting with a minus sign for negative number
        if value == '-':
            entry_label.config(text=value)
            last_expression = value
            return
        elif value in "+*/×÷":
            # Don't allow starting with these operators
            return
        else:
            entry_label.config(text=value)
            last_expression = value
            return

    operators = "+-*/×÷"
    clean_text = current_text.replace(',', '')

    # Last character in the current display
    last_char = clean_text[-1] if clean_text else ''
    second_last_char = clean_text[-2] if len(clean_text) > 1 else ''

    if value in operators:
        if last_char in operators:
            if value == '-':
                # Allow multiple minus signs only if not already two consecutive minus signs
                if last_char == '-' and second_last_char == '-':
                    # Prevent more than two consecutive minus signs
                    return
                else:
                    new_text = clean_text + value
            else:
                # Replace last operator with new one (except for multiple minus handled above)
                new_text = clean_text[:-1] + value
        else:
            new_text = clean_text + value

        entry_label.config(text=new_text)
        last_expression = new_text

    else:
        # Append digits or dot normally
        new_text = clean_text + value
        entry_label.config(text=new_text)
        last_expression = new_text

    root.update_idletasks()
    update_scrollbar_visibility()
    canvas.xview_moveto(1.0)

def clear():
    global last_expression
    entry_label.config(text="")
    last_expression = ""
    canvas.xview_moveto(0)
    update_scrollbar_visibility()

def backspace():
    global last_expression
    current_text = entry_label['text']
    if current_text == "Error":
        entry_label.config(text="")
        last_expression = ""
    elif current_text:
        new_text = current_text[:-1]
        entry_label.config(text=new_text)
        last_expression = new_text.replace(',', '')
    update_scrollbar_visibility()
    canvas.xview_moveto(1.0)

def calculate():
    global last_expression
    current_text = entry_label['text']
    if current_text.strip() == "":
        show_update_log()
        return

    try:
        expression = current_text.replace('×', '*').replace('÷', '/').replace(',', '')
        result = eval(expression)
        formatted_result = format_number(str(result))

        # Store and print calculation history
        record = f"{expression} = {formatted_result}"
        calculation_history.append(record)
        print(record)

        entry_label.config(text=formatted_result)
        last_expression = str(result)
        canvas.xview_moveto(1.0)
    except Exception:
        entry_label.config(text="Error")
        last_expression = ""
        canvas.xview_moveto(1.0)
    update_scrollbar_visibility()

def on_key_press(event):
    key = event.keysym
    char = event.char

    allowed_chars = "0123456789.+-*/×÷"

    current_text = entry_label['text']

    if char in allowed_chars:
        if current_text == "Error":
            entry_label.config(text=char)
            global last_expression
            last_expression = char
        else:
            click_button(char)
    elif key == "Return":
        calculate()
    elif key == "BackSpace":
        backspace()
    elif key in ("Escape", "Delete"):
        clear()

def update_scrollable_region_and_pos():
    canvas.configure(scrollregion=canvas.bbox("all"))
    label_height = entry_label.winfo_height()
    canvas_height = canvas.winfo_height()
    y = max((canvas_height - label_height) / 2, 0)
    canvas.coords(label_window, (0, y))

def update_scrollbar_visibility():
    update_scrollable_region_and_pos()
    label_width = entry_label.winfo_reqwidth()
    canvas_width = canvas.winfo_width()
    if label_width > canvas_width:
        h_scroll.lift()
        h_scroll.place(relx=0, rely=1, relwidth=1, anchor='sw')
    else:
        h_scroll.place_forget()
        canvas.xview_moveto(0)

nonlocal_vars = {'mouse_over_canvas': False, 'mouse_over_scroll': False}

def on_enter_canvas(event):
    nonlocal_vars['mouse_over_canvas'] = True
    update_scrollbar_visibility()

def on_leave_canvas(event):
    nonlocal_vars['mouse_over_canvas'] = False
    root.after(100, check_mouse_leave)

def on_enter_scroll(event):
    nonlocal_vars['mouse_over_scroll'] = True
    update_scrollbar_visibility()

def on_leave_scroll(event):
    nonlocal_vars['mouse_over_scroll'] = False
    root.after(100, check_mouse_leave)

def check_mouse_leave():
    if not nonlocal_vars['mouse_over_canvas'] and not nonlocal_vars['mouse_over_scroll']:
        h_scroll.place_forget()
        canvas.xview_moveto(0)

def print_current_settings_and_history():
    print(f"Welcome to Python Calculator Version {version}!")
    print("Made by cdr-int | https://github.com/cdr-int\n")
    
    print("DISCLAIMER: This calculator is NOT a scientific calculator.")
    print("The calculator tries to follow BIDMAS rules, but using this\n\
software requires some descresion from the user, as it may\n\
not be 100% acurate.\n")
    
    print("=== Calculator Settings ===")
    print(f"Version: {version}")
    print(f"Background Color: {COLOR_BG}")
    print(f"Foreground Color: {COLOR_FG}")
    print(f"Button Background (Main): {COLOR_BTN_BG_MAIN}")
    print(f"Button Background (Operators): {COLOR_BTN_BG_OP}")
    print(f"Button Background (AC): {COLOR_BTN_AC_BG}")
    print(f"Button Foreground: {COLOR_BTN_FG}")
    print(f"Main Font: {FONT_MAIN}")
    print(f"Button Font: {FONT_BUTTON}")
    print("===========================\n")

    if calculation_history:
        print("=== Calculation History ===")
        for record in calculation_history:
            print(record)
        print("===========================")
    else:
        print("Calculation History:\n")

# ======== UI SETUP ========

root = tk.Tk()
root.title(f"Calculator {version}")

entry_frame = tk.Frame(root, bd=0, relief="flat")
entry_frame.grid(row=0, column=0, columnspan=3, sticky="ew")

dummy_button = tk.Button(root, text="AC", width=7, height=2, font=(FONT_BUTTON[0], FONT_BUTTON[1], "bold"))
dummy_button.grid(row=0, column=3, sticky="nsew")
root.update_idletasks()
ac_height = dummy_button.winfo_height()
dummy_button.grid_forget()

canvas = tk.Canvas(entry_frame, height=ac_height, bg=COLOR_BG)
canvas.pack(side=tk.TOP, fill=tk.X, expand=True)

entry_label = tk.Label(canvas, text="", font=FONT_MAIN, anchor="w", bg=COLOR_BG, fg=COLOR_FG, relief="flat")
label_window = canvas.create_window((0, 0), window=entry_label, anchor="nw")

h_scroll = tk.Scrollbar(entry_frame, orient=tk.HORIZONTAL, command=canvas.xview, width=20)
canvas.configure(xscrollcommand=h_scroll.set)
h_scroll.place(relx=0, rely=1, relwidth=1, anchor='sw')

canvas.bind("<Enter>", on_enter_canvas)
canvas.bind("<Leave>", on_leave_canvas)
h_scroll.bind("<Enter>", on_enter_scroll)
h_scroll.bind("<Leave>", on_leave_scroll)

entry_label.bind("<Configure>", lambda e: update_scrollbar_visibility())
canvas.bind("<Configure>", lambda e: update_scrollbar_visibility())

clear_button = tk.Button(
    root, text="AC", width=7, height=2, font=(FONT_BUTTON[0], FONT_BUTTON[1], "bold"),
    command=clear, bg=COLOR_BTN_AC_BG, fg=COLOR_BTN_FG, relief="flat"
)
clear_button.grid(row=0, column=3, sticky="nsew")

buttons = [
    ('9', 1, 2, COLOR_BTN_BG_MAIN), ('8', 1, 1, COLOR_BTN_BG_MAIN), ('7', 1, 0, COLOR_BTN_BG_MAIN), ('+', 1, 3, COLOR_BTN_BG_OP),
    ('6', 2, 2, COLOR_BTN_BG_MAIN), ('5', 2, 1, COLOR_BTN_BG_MAIN), ('4', 2, 0, COLOR_BTN_BG_MAIN), ('-', 2, 3, COLOR_BTN_BG_OP),
    ('3', 3, 2, COLOR_BTN_BG_MAIN), ('2', 3, 1, COLOR_BTN_BG_MAIN), ('1', 3, 0, COLOR_BTN_BG_MAIN), ('/', 3, 3, COLOR_BTN_BG_OP),
    ('0', 4, 0, COLOR_BTN_BG_MAIN), ('.', 4, 1, COLOR_BTN_BG_MAIN), ('=', 4, 2, COLOR_BTN_BG_MAIN), ('×', 4, 3, COLOR_BTN_BG_OP)
]

for (text, row, col, bg_color) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=7, height=2, font=FONT_BUTTON,
                           command=calculate, bg=bg_color, fg=COLOR_BTN_FG, relief="flat")
    else:
        button = tk.Button(root, text=text, width=7, height=2, font=FONT_BUTTON,
                           command=lambda value=text: click_button(value),
                           bg=bg_color, fg=COLOR_BTN_FG, relief="flat")
    button.grid(row=row, column=col, sticky="nsew")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.bind("<Key>", on_key_press)

# Print welcome message and settings on startup
print_current_settings_and_history()

root.mainloop()
