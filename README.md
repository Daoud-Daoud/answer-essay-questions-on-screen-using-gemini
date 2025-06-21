📌 Answer Multiple Choice Questions on Screen Using Gemini
(Excluding complex math questions due to limited math symbol and notation detection)

This Python script captures your Windows screen, extracts visible text using OCR (Tesseract), sends it to Google's Gemini AI, and displays the answer as an on-screen overlay notification.

🎯 Ideal for instantly solving MCQs that appear on your screen—just hit a hotkey!

🚀 Features
  ✅ Screen Capture Grabs the visible area of your screen (excluding the taskbar/header).

  ✅ OCR (Optical Character Recognition) Uses Tesseract to extract text from the screenshot.

  ✅ Gemini AI IntegrationSends the extracted text to Gemini AI and fetches a likely answer.

  ✅ Overlay Notification Pops up the answer on your screen for a few seconds.

  ✅ Hotkey Trigger Press Ctrl + Shift + Q anytime to activate.

🛠️ Setup
  1️⃣ Install Tesseract OCR Download and install from tesseract-ocr/tesseract

    Default install path: C:\Program Files\Tesseract-OCR\tesseract.exe

  If installed elsewhere, edit the TESSERACT_PATH in main.py.

2️⃣ Install Python Dependencies

  pip install -r requirements.txt

3️⃣ Set Up Gemini API Get your Gemini API Key from Google.

  Set it as an environment variable before running:

  set GEMINI_API_KEY=your_actual_api_key_here python main.py
  🔒 Or replace "YOUR_GEMINI_API_KEY" directly in the code (not recommended for security).

4️⃣ Run The Script
  python main.py
  Press Ctrl + Shift + Q
  ➤ Captures screen → Extracts text → Gets answer → Displays overlay!

🔐 Security Tips
  ❗ Never commit your real API key to GitHub
  ✅ Use environment variables or secrets management tools instead.

💻 Requirements
  Windows OS
  Uses ImageGrab, win10toast, and other Windows-specific tools.

Python 3.7+

Tesseract OCR installed

💡 Inspiration
Built to blend speed, automation, and the power of AI for smarter screen interaction.
