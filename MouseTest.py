import tkinter as tk
import random
import time

class ClickTestApp:
    def __init__(self, root, duration=10):
        self.root = root
        self.root.title("Click Test")
        self.root.attributes('-fullscreen', True)  # Ventana en pantalla completa
        self.root.configure(bg="white")
        
        self.duration = duration
        self.start_time = None
        self.click_times = []
        self.points_clicked = 0
        
        self.label_timer = tk.Label(root, text=f"Time: {self.duration}s", font=("Arial", 14), bg="white")
        self.label_timer.pack()
        
        self.canvas = tk.Canvas(root, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)  # Ajustar canvas a pantalla completa
        
        self.point = None
        self.running = False
        
        self.start_button = tk.Button(root, text="Start", command=self.start_test)
        self.start_button.pack()
        
        self.root.bind("<Escape>", self.exit_fullscreen)  # Permitir salir con Escape
        
    def start_test(self):
        self.start_button.pack_forget()
        self.start_time = time.time()
        self.click_times = []
        self.points_clicked = 0
        self.running = True
        self.update_timer()
        self.spawn_point()
    
    def update_timer(self):
        elapsed = int(time.time() - self.start_time)
        remaining = max(0, self.duration - elapsed)
        self.label_timer.config(text=f"Time: {remaining}s")
        
        if remaining > 0:
            self.root.after(1000, self.update_timer)
        else:
            self.end_test()
    
    def spawn_point(self):
        if not self.running:
            return
        
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        x, y = random.randint(20, width - 20), random.randint(20, height - 20)
        self.point = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="red", outline="red")
        self.canvas.tag_bind(self.point, "<Button-1>", self.click_point)
    
    def click_point(self, event):
        if self.start_time:
            reaction_time = time.time() - self.start_time - sum(self.click_times)
            self.click_times.append(reaction_time)
            self.points_clicked += 1
            self.spawn_point()
    
    def end_test(self):
        self.running = False
        self.canvas.delete("all")
        
        avg_time = sum(self.click_times) / len(self.click_times) if self.click_times else 0
        result_text = f"Test Completed!\nTotal Clicks: {self.points_clicked}\nAverage Reaction Time: {avg_time:.2f} sec"
        
        self.result_label = tk.Label(self.root, text=result_text, font=("Arial", 14), bg="white")
        self.result_label.pack()
        
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_test)
        self.restart_button.pack()
    
    def restart_test(self):
        self.result_label.destroy()
        self.restart_button.destroy()
        self.start_button.pack()
    
    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickTestApp(root, duration=10)
    root.mainloop()
