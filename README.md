---

# 🧮 Python GUI Calculator

A clean, modern, and feature-rich calculator built with **Tkinter** in Python. It supports basic arithmetic operations, follows a simple **BIDMAS** rule system, and includes a scrollable history display and update log viewer. Ideal for everyday use, and perfect for learning about GUI programming in Python.

---

## 📦 Features

- Beautiful **Tkinter-based GUI**
- Arithmetic operations: `+`, `-`, `×`, `÷`, `.` (decimal support)
- Supports basic **BIDMAS** order of operations
- Number formatting with **commas**
- Responsive layout and scrollable display
- Interactive **Update Log** viewer
- Keyboard support (`Enter`, `Backspace`, `Escape`, etc.)
- Real-time calculation history output in terminal
- Customizable **themes and fonts**

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.6+
- No external libraries required (uses built-in `tkinter`)

### 🖥️ Run the Calculator

Clone the repository and run the Python file:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
python calculator.py
````

---

## 🎨 UI Preview

> This is a fully GUI-based calculator. All buttons are styled with customizable colors and fonts. The input field supports horizontal scrolling for long expressions, and the result is displayed with comma formatting.
<img width="769" height="589" alt="Python Calculator" src="https://github.com/user-attachments/assets/d133ff83-8e42-444c-a3fe-85119f2d7de3" />
---

## 🧰 Keyboard Shortcuts

| Key                            | Action            |
| ------------------------------ | ----------------- |
| `0-9`, `+`, `-`, `*`, `/`, `.` | Add to expression |
| `Enter`                        | Calculate         |
| `Backspace`                    | Delete last char  |
| `Escape` / `Delete`            | Clear all         |

---

## 🛠️ Customization

Modify the following variables at the top of the script to customize the appearance:

```python
COLOR_BG = "#FFFFFF"
COLOR_FG = "#212121"
COLOR_BTN_BG_MAIN = "#212121"
COLOR_BTN_BG_OP = "#757575"
COLOR_BTN_AC_BG = "#129688"
COLOR_BTN_FG = "white"

FONT_MAIN = ("Arial", 24)
FONT_BUTTON = ("Arial", 18)
```
<img width="1198" height="690" alt="Python Calculator" src="https://github.com/user-attachments/assets/20e85110-0144-406f-8f9d-11007f414857" />
---

## 📝 Update Log

Accessible from within the calculator by pressing `Enter` on an empty field.

```
Version 1.0.0 - First release  
Version 1.0.1 - Minor fixes and improvements  
Version 1.0.2 - Added number formatting with commas  
Version 2.0.0 - Major UI overhaul and new features  
Version 3.0.0 - Calculation overhaul & Calculation log added  
Version 3.0.1 - Text display fixes  
Version 3.0.2 - Code reformatting & Settings  
Version 4.0.0 - Fixed negative number handling  
Version 4.0.1 - Added simple BIDMAS calculation system  
Version 4.0.2 - Added disclaimer to terminal message  
```

---

## ⚠️ Disclaimer

> This is **not** a scientific calculator.
> While it implements a simple BIDMAS logic, the use of Python’s `eval()` means results may not always reflect complex mathematical precedence accurately. Use with discretion.

---

## 👨‍💻 Author

**cdr-int**
GitHub: [https://github.com/cdr-int](https://github.com/cdr-int)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

Thanks for checking out this calculator! Feel free to star ⭐ the repo or contribute with a PR!

