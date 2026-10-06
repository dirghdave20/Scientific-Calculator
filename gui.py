import tkinter as tk
from tkinter import messagebox

from calculator import calculate
from vector import (
    add_vectors,
    subtract_vectors,
    dot_product,
    magnitude,
    scalar_multiply
)


class CalculatorGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("500x550")

        # Title
        title = tk.Label(
            root,
            text="SCIENTIFIC CALCULATOR",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        # Tabs
        tabs = tk.Frame(root)
        tabs.pack()

        calculator_button = tk.Button(
            tabs,
            text="Calculator",
            command=self.show_calculator
        )
        calculator_button.grid(row=0, column=0, padx=5)

        vector_button = tk.Button(
            tabs,
            text="Vector",
            command=self.show_vector
        )
        vector_button.grid(row=0, column=1, padx=5)

        # Main area
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)

        self.show_calculator()

    # ---------------- CALCULATOR ----------------

    def show_calculator(self):

        self.clear_frame()

        self.expression = tk.Entry(
            self.main_frame,
            width=30,
            font=("Arial", 18)
        )
        self.expression.grid(
            row=0,
            column=0,
            columnspan=4,
            pady=10
        )

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3)
        ]

        for text, row, column in buttons:

            button = tk.Button(
                self.main_frame,
                text=text,
                width=6,
                height=2,
                command=lambda x=text: self.calculator_button(x)
            )

            button.grid(
                row=row,
                column=column,
                padx=3,
                pady=3
            )

        # Scientific buttons
        scientific = [
            ("sin(", 5, 0),
            ("cos(", 5, 1),
            ("tan(", 5, 2),
            ("sqrt(", 5, 3),

            ("log(", 6, 0),
            ("ln(", 6, 1),
            ("factorial(", 6, 2),
            ("^", 6, 3),

            ("pi", 7, 0),
            ("e", 7, 1),
            ("(", 7, 2),
            (")", 7, 3)
        ]

        for text, row, column in scientific:

            button = tk.Button(
                self.main_frame,
                text=text,
                width=6,
                height=2,
                command=lambda x=text: self.calculator_button(x)
            )

            button.grid(
                row=row,
                column=column,
                padx=3,
                pady=3
            )

        clear_button = tk.Button(
            self.main_frame,
            text="CLEAR",
            width=28,
            height=2,
            command=self.clear_calculator
        )

        clear_button.grid(
            row=8,
            column=0,
            columnspan=4,
            pady=10
        )

    def calculator_button(self, value):

        if value == "=":

            expression = self.expression.get()
            result = calculate(expression)

            self.expression.delete(0, tk.END)
            self.expression.insert(0, str(result))

        else:

            self.expression.insert(tk.END, value)

    def clear_calculator(self):

        self.expression.delete(0, tk.END)

    # ---------------- VECTOR ----------------

    def show_vector(self):

        self.clear_frame()

        title = tk.Label(
            self.main_frame,
            text="VECTOR OPERATIONS",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=5)

        tk.Label(
            self.main_frame,
            text="Enter Vector A:"
        ).pack()

        self.vector_a = tk.Entry(
            self.main_frame,
            width=30
        )
        self.vector_a.pack(pady=5)

        tk.Label(
            self.main_frame,
            text="Enter Vector B:"
        ).pack()

        self.vector_b = tk.Entry(
            self.main_frame,
            width=30
        )
        self.vector_b.pack(pady=5)

        tk.Label(
            self.main_frame,
            text="Example: 1,2,3"
        ).pack()

        buttons = [
            ("Addition", self.vector_add),
            ("Subtraction", self.vector_subtract),
            ("Dot Product", self.vector_dot),
            ("Magnitude of A", self.vector_magnitude),
            ("Scalar Multiplication", self.vector_scalar)
        ]

        for text, command in buttons:

            tk.Button(
                self.main_frame,
                text=text,
                width=25,
                command=command
            ).pack(pady=3)

        self.vector_result = tk.Label(
            self.main_frame,
            text="Result: ",
            font=("Arial", 12, "bold")
        )

        self.vector_result.pack(pady=15)

    def get_vectors(self):

        try:

            a = [
                float(x.strip())
                for x in self.vector_a.get().split(",")
            ]

            b = [
                float(x.strip())
                for x in self.vector_b.get().split(",")
            ]

            if len(a) != len(b):
                messagebox.showerror(
                    "Error",
                    "Both vectors must have the same size."
                )
                return None, None

            return a, b

        except:

            messagebox.showerror(
                "Error",
                "Enter vectors like: 1,2,3"
            )

            return None, None

    def vector_add(self):

        a, b = self.get_vectors()

        if a is not None:
            result = add_vectors(a, b)
            self.show_result(result)

    def vector_subtract(self):

        a, b = self.get_vectors()

        if a is not None:
            result = subtract_vectors(a, b)
            self.show_result(result)

    def vector_dot(self):

        a, b = self.get_vectors()

        if a is not None:
            result = dot_product(a, b)
            self.show_result(result)

    def vector_magnitude(self):

        try:

            a = [
                float(x.strip())
                for x in self.vector_a.get().split(",")
            ]

            result = magnitude(a)
            self.show_result(result)

        except:

            messagebox.showerror(
                "Error",
                "Enter Vector A correctly."
            )

    def vector_scalar(self):

        try:

            a = [
                float(x.strip())
                for x in self.vector_a.get().split(",")
            ]

            number = float(
                self.vector_b.get()
            )

            result = scalar_multiply(a, number)
            self.show_result(result)

        except:

            messagebox.showerror(
                "Error",
                "Enter Vector A and scalar correctly."
            )

    def show_result(self, result):

        self.vector_result.config(
            text="Result: " + str(result)
        )

    # ---------------- COMMON ----------------

    def clear_frame(self):

        for widget in self.main_frame.winfo_children():
            widget.destroy()