import tkinter as tk
from tkinter import messagebox, ttk

class MaquinaTuringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina de Turing - Suma Binaria")
        self.root.geometry("800x550")
        self.root.configure(bg="#1f1f2e")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background="#1f1f2e", foreground="#c4c4c4")
        style.configure("TNotebook.Tab", font=("Courier New", 11, "bold"), padding=(10, 5), background="#29293d", foreground="#00ff00")
        style.configure("TFrame", background="#1f1f2e")
        style.configure("TLabel", background="#1f1f2e", foreground="#00ff00", font=("Courier New", 12, "bold"))

        notebook = ttk.Notebook(root)
        notebook.pack(expand=True, fill="both", padx=10, pady=10)
        self.create_input_tab(notebook)
        self.create_table_tab(notebook)

    def create_input_tab(self, notebook):
        input_frame = ttk.Frame(notebook)
        notebook.add(input_frame, text="Entrada")

        title = ttk.Label(input_frame, text="Máquina Turing - Suma Binaria", font=("Courier New", 18, "bold"), foreground="#00ccff")
        title.pack(pady=15)

        label = ttk.Label(input_frame, text="Ingresa binarios separados por '+':")
        label.pack(pady=10)

        self.entry = ttk.Entry(input_frame, font=("Courier New", 13), width=30, foreground="#1f1f2e")
        self.entry.pack(pady=10)

        button_frame = ttk.Frame(input_frame, style="TFrame")
        button_frame.pack(pady=20)

        self.run_button = ttk.Button(button_frame, text="Ejecutar", command=self.run_machine, style="TButton")
        self.run_button.grid(row=0, column=0, padx=5)

        self.clear_button = ttk.Button(button_frame, text="Limpiar", command=self.clear_input, style="TButton")
        self.clear_button.grid(row=0, column=1, padx=5)

        self.result_label = ttk.Label(input_frame, text="", font=("Courier New", 13, "bold"), foreground="#c4c4c4")
        self.result_label.pack(pady=15)

    def create_table_tab(self, notebook):
        table_frame = ttk.Frame(notebook)
        notebook.add(table_frame, text="Tabla")

        table_title = ttk.Label(table_frame, text="Conversión Binaria", font=("Courier New", 16, "bold"), foreground="#00ccff")
        table_title.pack(pady=15)

        columns = ("decimal", "binary")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
        self.table.heading("decimal", text="Decimal")
        self.table.heading("binary", text="Binario")

        data = [
            ("0", "0"), ("1", "1"), ("2", "10"), ("3", "11"),
            ("4", "100"), ("5", "101"), ("6", "110"), ("7", "111")
        ]
        for decimal, binary in data:
            self.table.insert("", "end", values=(decimal, binary))
        self.table.pack(pady=20)

    def run_machine(self):
        input_text = self.entry.get().strip()
        if not input_text:
            self.show_error("Por favor, ingresa una entrada binaria.")
            return

        try:
            machine = MaquinaTuring(input_text)
            result = machine.run()
            self.result_label.config(text=f"Resultado: {result}", foreground="#00ff00")
        except ValueError as e:
            self.show_error(str(e))
        except Exception as e:
            print(f"Error: {e}")
            self.show_error("Error inesperado.")

    def clear_input(self):
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

    def show_error(self, message):
        messagebox.showerror("Error", message)
        self.result_label.config(text=f"Error: {message}", foreground="red")

class MaquinaTuring:
    def __init__(self, tape):
        self.numbers = tape.split('+')
        if not all(num.isdigit() and all(bit in '01' for bit in num) for num in self.numbers):
            raise ValueError("Entrada debe contener binarios válidos separados por '+'.")
        
        self.result = 0

    def add_binary(self):
        for binary in self.numbers:
            self.result += int(binary, 2)  
        return bin(self.result)[2:] 

    def run(self):
        return self.add_binary()

if __name__ == "__main__":
    root = tk.Tk()
    app = MaquinaTuringApp(root)
    root.mainloop()