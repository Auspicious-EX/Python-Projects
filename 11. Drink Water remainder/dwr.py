import time
import winsound
import pyttsx3
import tkinter as tk

class DrinkWaterReminderApp:
    def __init__(self, master):
        self.master = master
        master.title("Drink Water Reminder")

        self.reminder_count = 0

        self.label = tk.Label(master, text="Enter reminder interval (in minutes):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.reminder_count_label = tk.Label(master, text="")
        self.reminder_count_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_reminder)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_reminder, state=tk.DISABLED)
        self.stop_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def remind(self, interval):
        reminder_message = "Drink water buddy, it's important. I'll remind you again in one hour."
        while True:
            self.speak(reminder_message)
            winsound.Beep(1000, 500)  # Frequency = 1000Hz, Duration = 500ms
            self.reminder_count += 1
            self.reminder_count_label.config(text=f"Reminder count: {self.reminder_count}")
            self.master.update()  # Update the GUI to reflect the count change
            time.sleep(interval * 60)

    def start_reminder(self):
        interval = int(self.entry.get())
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.remind(interval)

    def stop_reminder(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = DrinkWaterReminderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
