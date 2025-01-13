import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import os

class MusicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music App")
        self.root.geometry("360x640")  # Small screen design
        self.root.configure(bg="#121212")

        # Header
        header = tk.Label(self.root, text="Music App", fg="white", bg="#121212", font=("Arial", 18, "bold"))
        header.pack(pady=20)

        # Buttons container
        button_frame = tk.Frame(self.root, bg="#121212")
        button_frame.pack(pady=20)

        # Buttons
        self.create_button(button_frame, "Spotify", "spotify_logo.png", self.open_spotify)
        self.create_button(button_frame, "Local", "local_logo.png", self.open_local)
        self.create_button(button_frame, "YouTube Music", "youtube_music_logo.png", self.open_youtube_music)

    def create_button(self, parent, text, logo_path, command):
        frame = tk.Frame(parent, bg="#1e1e1e", bd=2, relief="ridge")
        frame.pack(pady=10, fill="x", padx=30)

        logo_image = self.get_logo(logo_path, size=(40, 40))
        logo_label = tk.Label(frame, image=logo_image, bg="#1e1e1e")
        logo_label.image = logo_image
        logo_label.pack(side="left", padx=10)

        button = tk.Button(frame, text=text, command=command, bg="#1e1e1e", fg="white", font=("Arial", 14), bd=0, activebackground="#333333", activeforeground="white")
        button.pack(side="left", padx=10, expand=True)

    def get_logo(self, path, size):
        if os.path.exists(path):
            image = Image.open(path).resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image)
        else:
            return None

    def open_spotify(self):
        webbrowser.open("https://open.spotify.com", new=1)

    def open_youtube_music(self):
        webbrowser.open("https://music.youtube.com", new=1)

    def open_local(self):
        local_window = tk.Toplevel(self.root)
        local_window.title("Local Music")
        local_window.geometry("360x640")
        local_window.configure(bg="#121212")

        # Header
        header = tk.Label(local_window, text="Local Music", fg="white", bg="#121212", font=("Arial", 18, "bold"))
        header.pack(pady=20)

        # Search bar
        search_frame = tk.Frame(local_window, bg="#1e1e1e", bd=2, relief="ridge")
        search_frame.pack(pady=10, fill="x", padx=20)

        search_entry = tk.Entry(search_frame, font=("Arial", 14), bg="#333333", fg="white", insertbackground="white", relief="flat")
        search_entry.pack(side="left", fill="x", expand=True, padx=10)

        search_button = tk.Button(search_frame, text="Search", bg="#333333", fg="white", font=("Arial", 12), bd=0, activebackground="#555555", activeforeground="white")
        search_button.pack(side="right", padx=10)

        # Dummy songs
        dummy_songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5"]
        
        for song in dummy_songs:
            song_label = tk.Label(local_window, text=song, fg="white", bg="#121212", font=("Arial", 14), anchor="w")
            song_label.pack(fill="x", padx=20, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicApp(root)
    root.mainloop()
