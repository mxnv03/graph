import tkinter as tk
from tkinter import messagebox, filedialog
from visual import show
import re
from on_ditrict import diss


class GraphShow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Directed graphs")
        self.geometry("600x450")
        self.configure(bg='#c6efbf')
        self.resizable(True, True)

        self.size = tk.IntVar()
        self.edges = tk.StringVar()
        self.snowiness = tk.BooleanVar()

        self.edges_list = []
        self.start_point = tk.StringVar()
        self.end_point = tk.StringVar()
        # default
        self.size.set(value=3)
        self.edges.set(value='a b c')
        self.start_point.set('a')
        self.end_point.set('c')
        self.create_widgets()

    def create_widgets(self):
        self.size_label = tk.Label(self, text="Input size: ")
        self.edges_label = tk.Label(self, text="Input edges: ")

        self.size_entry = tk.Entry(self, textvariable=self.size)
        self.edges_entry = tk.Entry(self, textvariable=self.edges)

        self.start_label = tk.Label(self, text="Начальная точка: ")
        self.end_label = tk.Label(self, text="Конечная точка: ")

        self.start_entry = tk.Entry(self, textvariable=self.start_point)
        self.end_entry = tk.Entry(self, textvariable=self.end_point)

        self.snowiness1 = tk.Radiobutton(text="Матрица смежности", variable=self.snowiness, value=True)
        self.snowiness0 = tk.Radiobutton(text="Матрица инцидентности", variable=self.snowiness, value=False)

        self.sub = tk.Button(text="Сгенерировать \nматрицу", command=self.create_matrix, background='#af9aeb')
        self.sub1 = tk.Button(text="Сгенерировать \nиз файла", command=self.graph_from_file, background='#af9aeb')
        self.sub2 = tk.Button(text="Считать", command=self.get_all, background='#af9aeb')

        self.size_label.grid(row=1, column=0, padx=5, pady=5)
        self.size_entry.grid(row=1, column=1, padx=5, pady=5)
        self.edges_label.grid(row=2, column=0, padx=5, pady=5)
        self.edges_entry.grid(row=2, column=1, padx=5, pady=5)

        self.start_label.grid(row=3, column=0, padx=5, pady=5)
        self.start_entry.grid(row=3, column=1, padx=5, pady=5)
        self.end_label.grid(row=4, column=0, padx=5, pady=5)
        self.end_entry.grid(row=4, column=1, padx=5, pady=5)

        self.snowiness1.grid(row=5, column=1, padx=5, pady=5)
        self.snowiness0.grid(row=5, column=2, padx=5, pady=5)
        self.sub.grid(row=8, padx=5, pady=5)
        self.sub1.grid(row=9, padx=5, pady=5)
        self.sub2.grid(row=10, padx=5, pady=5)

        self.matrix = []
        self.entries = []
        self.weighted_edges = []

    def graph_from_file(self):
        filename = filedialog.askopenfilename(title="Открыть файл", initialdir="/")
        if filename:
            input = diss(filename)
            self.edges.set(input[1])
            self.size.set(input[2])
            show(input[0], self.start_point.get(), self.end_point.get())



    def get_all(self):
        self.G = []
        edges_pattern = r'^[a-zA-Z0-9\s]+$'
        if re.match(edges_pattern, self.edges.get()):
            self.edges_list = self.edges.get().replace(',', '').split()
            for x in range(self.size.get()):
                self.G.append([])
                for y in range(self.size.get()):
                    self.G[x].append([])
                    self.G[x][y] = int(self.matrix[x][y].get())

            for i in range(len(self.G)):
                for j in range(len(self.G)):
                    if i != j and self.G[i][j] != 0:
                        self.weighted_edges.append((self.edges_list[i], self.edges_list[j], self.G[i][j]))
            try:
                show(weighted_edge=self.weighted_edges, start=self.start_point.get(), end=self.end_point.get())
            except KeyError:
                messagebox.showerror("Что-то пошло не так",
                                     f"Невозможно попасть из [{self.start_point.get()}] в [{self.end_point.get()}]")
        else:
            messagebox.showerror('Неправильные наименования вершин', 'В строке могут быть только пробелы, буквы или цифры')

    def create_matrix(self):
        x2 = 100
        y2 = 150
        for i in range(self.size.get()):
            self.matrix.append([])
            self.entries.append([])
            for j in range(self.size.get()):
                self.matrix[i].append(tk.IntVar())
                self.entries[i].append(tk.Entry(textvariable=self.matrix[i][j], width=3))
                self.entries[i][j].place(x=60 + x2, y=50 + y2)
                x2 += 30
            y2 += 30
            x2 = 100


if __name__ == "__main__":
    app = GraphShow()
    app.mainloop()
