import pygame
import time
import datetime
import tkinter as tk
from threading import Thread
from PIL import Image, ImageTk
import sys
import os

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def set_alarm(alarm_time, status_label):
    status_label.config(text=f"アラームを設定しました: {alarm_time}")
    sound_file = resource_path("Pururin ringtone (Welcome to the NHK).mp3")
    global is_running
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        status_label.config(text=f"現在の時間: {current_time}")

        if current_time == alarm_time:
            status_label.config(text="おきろ。")
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                print("音が鳴る")
            except Exception as e:
                status_label.config(text=f"音声の読み込みエラー: {e}")
                print(f"エラー: {e}")
                is_running = False

            while pygame.mixer.music.get_busy() and is_running:
                time.sleep(1)
                # MP3が終わるか中止されるまで再生します。


            is_running = False

        time.sleep(1)

def start_alarm():
    alarm_time = entry.get()
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        Thread(target=set_alarm, args=(alarm_time, status_label)).start()
    except ValueError:
        status_label.config(text="HH:MM:SSを使用して。")

def on_closing():
    global is_running
    is_running = False
    root.destroy()


root = tk.Tk()
root.title("アラーム")
root.geometry("250x250")


try:
    image = Image.open(resource_path("background.webp"))#purirnrpirnrnrnniin
    image = image.resize((250, 250), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = photo
except Exception as e:
    print(f"画像の読み込みエラー: {e}")

# Place the widgets
tk.Label(root, text="アラーム時間を入力 (HH:MM:SS):").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="アラームを設定", command=start_alarm).pack(pady=20)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)





root.protocol("WM_DELETE_WINDOW", on_closing)

#
root.mainloop()

is_running = False


#--no console to DROP THE CNSOEL WINDOW