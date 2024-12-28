import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator_By_dangquochuy2025")
        self.root.geometry("500x500")
        
        # Entry to show calculations
        self.display = tk.Entry(self.root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)
        
        # Button layout with additional advanced operations
        buttons = [
            ('7', 1, 0, 'num'), ('8', 1, 1, 'num'), ('9', 1, 2, 'num'), ('/', 1, 3, 'operator'), ('%', 1, 4, 'operator'),
            ('4', 2, 0, 'num'), ('5', 2, 1, 'num'), ('6', 2, 2, 'num'), ('x', 2, 3, 'operator'), ('1/x', 2, 4, 'operator'),
            ('1', 3, 0, 'num'), ('2', 3, 1, 'num'), ('3', 3, 2, 'num'), ('-', 3, 3, 'operator'), ('sqrt', 3, 4, 'operator'),
            ('0', 4, 0, 'num'), ('.', 4, 1, 'num'), ('+', 4, 2, 'operator'), ('=', 4, 3, 'equal'), ('pi', 4, 4, 'constant'),
            ('C', 5, 0, 'clear'), ('(', 5, 1, 'bracket'), (')', 5, 2, 'bracket'), ('^', 5, 3, 'operator'), ('log', 5, 4, 'operator'),
            ('sin', 6, 0, 'operator'), ('cos', 6, 1, 'operator'), ('tan', 6, 2, 'operator'), ('e', 6, 3, 'constant')
        ]
        
        # Create buttons with hover and click effects
        for (text, row, col, button_type) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 18), height=2, width=5, relief="raised", 
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            button.bind("<Enter>", self.on_hover)
            button.bind("<Leave>", self.on_leave)
            button.bind("<ButtonPress-1>", self.on_button_press)
            button.bind("<ButtonRelease-1>", self.on_button_release)
            
            # Set button colors based on type
            if button_type == 'num':
                button.config(bg="#f0f0f0", fg="black")
            elif button_type == 'operator':
                button.config(bg="#ff9800", fg="white")
            elif button_type == 'equal':
                button.config(bg="#4CAF50", fg="white")
            elif button_type == 'clear':
                button.config(bg="#f44336", fg="white")
            elif button_type == 'bracket':
                button.config(bg="#2196F3", fg="white")
            elif button_type == 'constant':
                button.config(bg="#9C27B0", fg="white")

        # Make grid cells resizable
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)
        
        # Style adjustments
        self.root.config(bg="#f0f0f0")
        
    def on_button_click(self, char):
        current = self.display.get()
        
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = self.calculate_result(current)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, char)

    def calculate_result(self, expr):
        # Cập nhật hàm để hỗ trợ các phép toán phức tạp
        expr = expr.replace('x', '*').replace('^', '**').replace('1/x', '1/').replace('sqrt', 'math.sqrt')
        expr = expr.replace('pi', str(math.pi)).replace('e', str(math.e)).replace('log', 'math.log')
        expr = expr.replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan')
        
        # Xử lý phép toán
        return eval(expr)

    def on_hover(self, event):
        # Change color when mouse enters button
        event.widget.config(bg="#66bb6a")

    def on_leave(self, event):
        # Revert to original color when mouse leaves button
        if event.widget.cget('text') in ['+', '-', '*', '/', '=', 'C']:
            event.widget.config(bg="#ff9800")
        elif event.widget.cget('text') == 'C':
            event.widget.config(bg="#f44336")
        elif event.widget.cget('text') == '=':
            event.widget.config(bg="#4CAF50")
        elif event.widget.cget('text') in ['(', ')']:
            event.widget.config(bg="#2196F3")
        else:
            event.widget.config(bg="#f0f0f0")

    def on_button_press(self, event):
        # Change color when button is pressed
        event.widget.config(bg="#388e3c")

    def on_button_release(self, event):
        # Revert color after button is released
        if event.widget.cget('text') in ['+', '-', '*', '/', '=', 'C']:
            event.widget.config(bg="#ff9800")
        elif event.widget.cget('text') == 'C':
            event.widget.config(bg="#f44336")
        elif event.widget.cget('text') == '=':
            event.widget.config(bg="#4CAF50")
        elif event.widget.cget('text') in ['(', ')']:
            event.widget.config(bg="#2196F3")
        else:
            event.widget.config(bg="#f0f0f0")


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
