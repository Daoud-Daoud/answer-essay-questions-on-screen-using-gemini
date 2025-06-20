import keyboard
import pyautogui
import pytesseract
import threading
import time
import requests
import cv2
import numpy as np
from PIL import ImageGrab, Image
import tempfile
import os
import ctypes
from win10toast import ToastNotifier

# Configuration
API_KEY = os.environ.get("GEMINI_API_KEY") # Set your Gemini API key as an environment variable
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
TESSERACT_PATH = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"     #change this to your Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

toaster = ToastNotifier()

def capture_screen():
    screenshot = ImageGrab.grab()
    width, height = screenshot.size

    # Estimate taskbar and header sizes
    header_height = 40   # e.g., top Windows bar
    footer_height = 40   # e.g., Windows taskbar

    cropped = screenshot.crop((0, header_height, width, height - footer_height))
    return cropped

def extract_text_from_image(image):
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        image.save(tmp.name)
        text = pytesseract.image_to_string(Image.open(tmp.name))
    os.remove(tmp.name)
    return text.strip()

def ask_ai(text):
    prompt = f"Solve the following question and only generate the correct answer: {text}"
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    try:
        return data['candidates'][0]['content']['parts'][0]['text'].strip()
    except (KeyError, IndexError):
        return "No valid response received from Gemini AI."

def process_flow():
    try:
        image = capture_screen()
        extracted_text = extract_text_from_image(image)
        print("Extracted Text:", extracted_text)
        if extracted_text:
            answer = ask_ai(extracted_text)
            print("Gemini:", answer)
            show_custom_overlay(answer)
        else:
            print("No text detected.")
    except Exception as e:
        print("Error:", e)

def show_custom_overlay(message):
    import tkinter as tk
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.configure(background='black')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width, height = 400, 100
    x = (screen_width // 2) - (width // 2)
    y = 50  # top center

    root.geometry(f"{width}x{height}+{x}+{y}")
    label = tk.Label(root, text=message, bg="black", fg="white", font=("Segoe UI", 14), wraplength=380)
    label.pack(expand=True, fill='both')

    def close_overlay():
        root.destroy()

    root.after(8000, close_overlay)  # Auto-close after 8 sec
    root.mainloop()

def listen_shortcut():
    keyboard.add_hotkey("ctrl+shift+q", lambda: threading.Thread(target=process_flow).start())
    print("Listening for Ctrl+Shift+Q...")
    keyboard.wait()

if __name__ == "__main__":
    listen_shortcut()