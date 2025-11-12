import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import re, string, random, math, requests, hashlib, time

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    if len(password) >= 12:
        score += 1

    if score <= 1:
        remarks, color = "❌ Very Weak", "#ff4d4d"
    elif score == 2:
        remarks, color = "⚠️ Weak", "#ff9933"
    elif score == 3:
        remarks, color = "🟡 Medium", "#ffcc00"
    elif score == 4:
        remarks, color = "🟢 Strong", "#66ff99"
    else:
        remarks, color = "💪 Very Strong", "#00ffcc"

    return remarks, color, score


def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"\d", password): charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): charset += 32
    if charset == 0: return 0
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)


def generate_password():
    length = random.randint(10, 16)
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    entry.delete(0, tk.END)
    entry.insert(0, password)
    result_label.config(text="🔒 Generated a strong password!", fg="#00ffff")


def check_leak(password):
    try:
        sha1_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        first5, tail = sha1_pass[:5], sha1_pass[5:]
        response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}", timeout=6)
        if response.status_code != 200:
            return -1
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == tail:
                return int(count)
    except Exception:
        return -1
    return 0

def analyze_password():
    password = entry.get()
    if not password:
        messagebox.showinfo("Info", "Please enter a password to analyze.")
        return

    analyze_btn.config(state="disabled")
    generate_btn.config(state="disabled")
    view_btn.config(state="disabled")
    root.update_idletasks()

    strength, color, score = check_strength(password)
    entropy = calculate_entropy(password)
    leak_count = check_leak(password)

    if leak_count == -1:
        leak_text = "⚠️ Leak check failed (network/API error)."
    else:
        leak_text = f"🔴 Found in {leak_count} breaches!" if leak_count > 0 else "🟢 Not found in known leaks."

    result_label.config(
        text=f"Strength: {strength}\nEntropy: {entropy} bits\n{leak_text}",
        fg=color
    )

    analyze_btn.config(state="normal")
    generate_btn.config(state="normal")
    view_btn.config(state="normal")
 
def toggle_view():
    if entry.cget('show') == '':
        entry.config(show='*')
        view_btn.config(text="👁 View")
    else:
        entry.config(show='')
        view_btn.config(text="🙈 Hide")


def clear_all():
    entry.delete(0, tk.END)
    result_label.config(text="", fg="#00ffff")

root = tk.Tk()
root.title("🔐 Cyber Password Strength Checker")
root.geometry("600x480")
root.resizable(False, False)

try:
    bg_image = Image.open("background.jpg")  # change the filename if needed
    bg_image = bg_image.resize((600, 480), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception:
    root.configure(bg="#0f2027")

title = tk.Label(root, text="🔐 Cyber Password Strength Checker", fg="#00ffff", bg="#0f2027",
                 font=("Consolas", 18, "bold"))
title.place(x=80, y=40)

entry = tk.Entry(root, show="*", width=28, font=("Consolas", 14), bg="#1b1b2f", fg="#00ffcc", bd=2, relief="flat",
                 insertbackground="#00ffff", highlightbackground="#00ffff", highlightcolor="#00ffff", highlightthickness=1)
entry.place(x=140, y=120)

view_btn = tk.Button(root, text="👁 View", command=toggle_view, font=("Consolas", 10, "bold"), bg="#00ffff", fg="#000",
                     activebackground="#00ccff", relief="flat", padx=8, pady=3)
view_btn.place(x=440, y=118)

btn_style = {
    "font": ("Consolas", 11, "bold"),
    "bg": "#00ffff",
    "fg": "black",
    "activebackground": "#00ccff",
    "relief": "flat",
    "width": 20,
    "pady": 5
}

button_y = 190
spacing = 180

analyze_btn = tk.Button(root, text="🔎 Check Strength", command=analyze_password, **btn_style)
analyze_btn.place(x=60, y=button_y)

generate_btn = tk.Button(root, text="⚙️ Generate Password", command=generate_password, **btn_style)
generate_btn.place(x=60 + spacing, y=button_y)

clear_btn = tk.Button(root, text="🧹 Clear", command=clear_all, **btn_style)
clear_btn.place(x=60 + 2 * spacing, y=button_y)


result_label = tk.Label(
    root,
    text="",
    bg="#0f2027",
    fg="#00ffff",
    font=("Consolas", 12, "bold"),
    justify="center",
)
result_label.place(relx=0.5, y=310, anchor="center")
root.mainloop()