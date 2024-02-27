import tkinter as tk
import win32com.client

def pronounce_text():
    text_to_pronounce = text_entry.get("1.0", tk.END).strip()
    voice = "Microsoft David Desktop - English (United States)" if voice_var.get() == 0 else "Microsoft Zira Desktop - English (United States)"
    
    if text_to_pronounce:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        voices = speaker.GetVoices()
        for i in range(voices.Count):
            if voices.Item(i).GetDescription() == voice:
                speaker.Voice = voices.Item(i)
                break
        speaker.Speak(text_to_pronounce)

# Create the main window
app = tk.Tk()
app.title("Text to Speech")

# Create GUI components
text_label = tk.Label(app, text="Enter text:")
text_entry = tk.Text(app, height=5, width=50)
pronounce_button = tk.Button(app, text="Pronounce", command=pronounce_text)

# Voice selection
voice_var = tk.IntVar()
male_radio = tk.Radiobutton(app, text="Male", variable=voice_var, value=0)
female_radio = tk.Radiobutton(app, text="Female", variable=voice_var, value=1)

# Place GUI components
text_label.pack(pady=10)
text_entry.pack(pady=5)
male_radio.pack()
female_radio.pack()
pronounce_button.pack(pady=5)

# Start the GUI application
app.mainloop()
