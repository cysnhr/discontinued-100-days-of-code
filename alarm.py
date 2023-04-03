import tkinter as tk
import datetime
import RPi.GPIO as GPIO
import os
import random
import vlc
import time
import threading

"""
The alarm application will display the time, a greeting, and a stop alarm button, with Tkinter.
When the alarm goes off, the lights on the breadboard will start glowing, and music will play from a speaker.
"""

# Setting up the user interface
app = tk.Tk()
app.title("Raspberry Pi Alarm")
app.attributes("-fullscreen", True)
app.configure(bg="black")
app.geometry("500x500")

# Because it's full screen we need an exit button
exit_button = tk.Button(app, fg="white", bg="black", width=2, height=1, padx=2, pady=1, text="X", command=app.destroy)
exit_button.pack(side="top", anchor="nw")

time_label = tk.Label(app, font=("Roboto", 20), fg="white", bg="black", text="")
time_label.pack(side="top", anchor="center", expand=True)

# Display time
def time_display():
    current_time = datetime.datetime.now().strftime("%H:%M")
    time_label.config(text=current_time)
    app.after(30000, time_display)  # 1 second = 1000 milliseconds

time_display()

# Says hi to the user under different conditions
# Default is good night because the alarm is turned on at night
greeting_label = tk.Label(app, font=("Roboto", 20), fg="white", bg="black", text="Good night!")
greeting_label.pack(side="top", anchor="center", expand=True)

# Set up lights with GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

# The actual program of the alarm

ALARM_TIME = "19"

# Uses a class so that the playing song won't get lost, accessible to both on and off functions
class Alarm:
    def __init__(self):
        self.playlist_dir = "/home/gis/Downloads/Alarm Sounds"
        self.playlist = [os.path.join(self.playlist_dir, f) for f in os.listdir(self.playlist_dir)]
        # The line above is written with the help of ChatGPT. I had no idea how to use a VLC Media Player until now.
        # For ensuring academic honesty, I'll paste our conversation in a separate document.
        self.song = random.choice(self.playlist)
        self.player = vlc.MediaPlayer(self.song)

    def on(self):
        while True:
            if time.strftime("%H") == ALARM_TIME:
                # Turns on the music
                self.player.play()

                # Says hi
                greeting_label.config(text = "Good morning~")
                
                # Turn on the lights one by one
                GPIO.output(17, True)
                time.sleep(10)
                GPIO.output(18, True)
                time.sleep(10)
                GPIO.output(22, True)
                time.sleep(10)
                GPIO.output(23, True)

    def off(self):
        # Music bye
        self.player.stop()
        # Turn off lights
        GPIO.output(17, False)
        GPIO.output(18, False)
        GPIO.output(22, False)
        GPIO.output(23, False)
        GPIO.cleanup()
        # Change greetings again. It's in German just because I want to remember the phrase.
        greeting_label.config(text="Ich wünsche dir einen schönen Tag!")

# Call the class!
alarm = Alarm()

# A button that will stop the alarm
stop_alarm_button = tk.Button(app, font="Roboto", fg="white", bg="black", highlightcolor="white", text="Stop alarm", command=alarm.off)
stop_alarm_button.pack(side="top", anchor="center", expand=True)

threading.Thread(target=alarm.on).start()  # Just so the while True loop won't mess with the main loop

app.mainloop()

# Will put on citations
