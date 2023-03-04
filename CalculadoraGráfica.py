import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
class Menu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Proyecto POO")
        self.root.geometry("200x100")

        self.calc_button = tk.Button(self.root, text="Calculadora", command=self.open_calculator)
        self.calc_button.pack(pady=10)

        self.game_button = tk.Button(self.root, text="Gráfica", command=self.open_graph)
        self.game_button.pack(pady=10)

    def open_calculator(self):
        self.root.destroy()
        calculator = Calculator()

    def open_graph(self):
        self.root.destroy()
        grafica = graph(self)()

    def run(self):
        self.root.mainloop()

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora")
        self.root.geometry("300x400")

        self.display = tk.Entry(self.root, width=40, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        self.create_buttons()

    def create_buttons(self):
        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C"
        ]

        row = 1
        col = 0
        for button_text in button_list:
            button = tk.Button(self.root, text=button_text, width=7, height=3,
                               command=lambda text=button_text: self.button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)

    def run(self):
        self.root.mainloop()

def graph(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Valores de prueba
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(np.sqrt(X**2 + Y**2))

        ax.plot_surface(X, Y, Z)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()

menu = Menu()
menu.run()