import tkinter as tk
from tkinter import colorchooser

class PixelArtEditor:
    def __init__(self, root, grid_size=16, pixel_size=20):
        self.root = root
        self.grid_size = grid_size
        self.pixel_size = pixel_size
        self.current_color = "#000000"
        self.grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]

        self.create_widgets()
        self.draw_grid()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.grid_size * self.pixel_size, height=self.grid_size * self.pixel_size)
        self.canvas.pack()

        self.color_button = tk.Button(self.root, text="Choose Color", command=self.choose_color)
        self.color_button.pack()

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_grid)
        self.clear_button.pack()

        self.canvas.bind("<Button-1>", self.paint_pixel)

    def draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x1 = i * self.pixel_size
                y1 = j * self.pixel_size
                x2 = x1 + self.pixel_size
                y2 = y1 + self.pixel_size
                self.grid[i][j] = self.canvas.create_rectangle(x1, y1, x2, y2, outline="#CCCCCC", fill="#FFFFFF")

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.current_color = color

    def paint_pixel(self, event):
        x = event.x // self.pixel_size
        y = event.y // self.pixel_size
        self.canvas.itemconfig(self.grid[x][y], fill=self.current_color)

    def clear_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.canvas.itemconfig(self.grid[i][j], fill="#FFFFFF")

if __name__ == "__main__":
    root = tk.Tk()
    editor = PixelArtEditor(root)
    root.mainloop()