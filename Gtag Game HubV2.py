import tkinter as tk
import webbrowser
import time

class GameLauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gtag Menu Temps")
        self.root.geometry("400x300")

        self.games = {
            "Shiba-Gt Temp": "https://cdn.discordapp.com/attachments/1166660207884111903/1197700503681900614/ShibaGTTemplate.zip?ex=65bc3884&is=65a9c384&hm=66a1e812dbe0f7f96bbca81230d6b1baaf0a5239f0dfeec75dfc7ab280023dc3&",
            "iis Temp": "https://cdn.discordapp.com/attachments/1169905985222094848/1215972290794360962/lost_the_money_in_my_bank_account.zip?ex=6607ebf1&is=65f576f1&hm=1b964b7bcc700e3f47aaec8afecf7b72c9fbc73806a084f6c838b9773d269070&",
            "KMan Temp": "https://cdn.discordapp.com/attachments/1166660207884111903/1197700504332029972/Templatekman_1.zip?ex=65bc3884&is=65a9c384&hm=24048539edab0a2a5d2df603bba84d6f6bc147e093024c43e0d04d7f5c48f2f0&",
            "My Yt With Tuts": "https://www.youtube.com/@2024joe",
        }

        self.create_gui()

    def create_gui(self):
        self.title_bar = tk.Frame(self.root, bg="blue")
        self.title_bar.pack(fill="x")

        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas = tk.Canvas(self.root, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar.config(command=self.canvas.yview)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.hover_menu = None
        self.hover_button = tk.Button(self.title_bar, text="≡", bg="gray", fg="white", command=self.show_hover_menu)
        self.hover_button.pack(side="left")

    def populate_game_buttons(self):
        for game_name, game_url in self.games.items():
            game_button = tk.Button(self.frame, text=game_name, command=lambda url=game_url: self.open_game_link(url))
            game_button.pack(pady=5)
            game_button.configure(
                background="#5D30AF",  # Hexadecimal color with transparency
                borderwidth=1,
                cursor="hand2",  # Use "hand2" for a hand cursor
                font=("Arial", 14, "bold"),
                border=1,
                relief="solid",
                width=30,
                height=2,
            )
            game_button.bind("<Enter>", self.on_button_hover)
            game_button.bind("<Leave>", self.on_button_leave)

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def open_game_link(self, url):
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"Error opening URL: {e}")

    def on_button_hover(self, event):
        event.widget.configure(
            background="#4A1F94",  # Color change on hover
            relief="raised",
            border=2,
            font=("Arial", 15, "bold"),
        )

    def on_button_leave(self, event):
        event.widget.configure(
            background="#5D30AF",  # Hexadecimal color with transparency
            relief="solid",
            border=1,
            font=("Arial", 14, "bold"),
        )

    def show_hover_menu(self):
        # Add code to show a hover menu
        pass


def loading_screen(root, loading_finished_callback):
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading...")
    loading_window.geometry("300x150")

    loading_frame = tk.Frame(loading_window, bg="#1a1a1a")
    loading_frame.pack(expand=True, fill="both")

    loading_text = tk.Label(loading_frame, text="Loading...", font=("Courier New", 16, "bold"), bg="#1a1a1a", fg="#0f0")
    loading_text.pack(pady=20)

    loading_loader = tk.Frame(loading_frame, bd=2, relief="solid", bg="#1a1a1a")
    loading_loader.pack()

    text_widget = tk.Label(loading_loader, text="", font=("Courier New", 12), fg="#0f0", bg="#1a1a1a")
    text_widget.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="w")

    for i in range(1, 6):
        dots = "." * i
        text_widget.config(text=f"Loading{dots}")
        loading_window.update()
        time.sleep(1)

    loading_window.destroy()
    loading_finished_callback()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window initially

    def on_loading_finished():
        root.deiconify()  # Make the main window visible
        app = GameLauncherApp(root)
        app.populate_game_buttons()

    # Schedule loading screen for 5 seconds
    root.after(0, lambda: loading_screen(root, on_loading_finished))

    root.mainloop()
