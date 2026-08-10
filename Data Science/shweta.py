import customtkinter as ctk
from datetime import datetime, timedelta
import json, os

ctk.set_appearance_mode("dark")

# ---------------- CONFIG ----------------
target_date = datetime(2026, 6, 27)
today = datetime.today()
file = "shweta_pro.json"

# Load data
if os.path.exists(file):
    data = json.load(open(file))
else:
    data = {}

# App
app = ctk.CTk()
app.title("💖 Shweta  Study Tracker Pro")
app.geometry("750x800")

# ---------------- HEADER ----------------
title = ctk.CTkLabel(app, text="💖 Shweta  Study Tracker 💖", font=("Arial", 26, "bold"))
title.pack(pady=10)

days_left = (target_date - today).days
countdown = ctk.CTkLabel(app, text=f"⏳ {days_left} Days Left", font=("Arial", 18))
countdown.pack()

# ---------------- TARGET ----------------
target_var = ctk.StringVar(value="5")

target_frame = ctk.CTkFrame(app)
target_frame.pack(pady=5)

ctk.CTkLabel(target_frame, text="🎯 Daily Target (hrs):").pack(side="left", padx=5)
target_entry = ctk.CTkEntry(target_frame, textvariable=target_var, width=60)
target_entry.pack(side="left")

# ---------------- PROGRESS ----------------
progress = ctk.CTkProgressBar(app, width=400)
progress.pack(pady=10)

progress_label = ctk.CTkLabel(app, text="")
progress_label.pack()

# ---------------- SCROLL ----------------
frame = ctk.CTkScrollableFrame(app, width=700, height=450)
frame.pack(pady=10)

entries = {}

# ---------------- CALENDAR ----------------
for i in range(days_left + 1):
    day = today + timedelta(days=i)
    d = day.strftime("%Y-%m-%d")

    row = ctk.CTkFrame(frame)
    row.pack(pady=4, fill="x")

    label = ctk.CTkLabel(row, text=d, width=120)
    label.pack(side="left")

    entry = ctk.CTkEntry(row, placeholder_text="Hours", width=80)
    entry.pack(side="left", padx=5)

    var = ctk.BooleanVar()

    def toggle_color(v=var, r=row):
        if v.get():
            r.configure(fg_color="#14532d")
        else:
            r.configure(fg_color="#2a2a2a")

    cb = ctk.CTkCheckBox(row, text="Done", variable=var, command=toggle_color)
    cb.pack(side="left", padx=10)

    if d in data:
        entry.insert(0, data[d]["hours"])
        var.set(data[d]["done"])
        toggle_color()

    entries[d] = (entry, var)

# ---------------- FUNCTIONS ----------------

def save():
    for d, (e, v) in entries.items():
        data[d] = {"hours": e.get(), "done": v.get()}

    json.dump(data, open(file, "w"))
    status.configure(text="💾 Saved!", text_color="green")
    update_stats()

def calculate_total():
    total = 0
    for e, _ in entries.values():
        try:
            total += float(e.get())
        except:
            pass
    return total

def calculate_done():
    done = sum(v.get() for _, v in entries.values())
    return done

def update_stats():
    total_days = len(entries)
    done_days = calculate_done()
    percent = done_days / total_days if total_days else 0

    progress.set(percent)
    progress_label.configure(text=f"📊 Progress: {int(percent*100)}%")

    total_hours = calculate_total()
    stats.configure(text=f"⏱ Total Hours: {total_hours}")

    show_streak()
    show_motivation()

def reset():
    for e, v in entries.values():
        e.delete(0, "end")
        v.set(False)
    status.configure(text="🗑 Reset Done!", text_color="red")
    update_stats()

def show_streak():
    streak = 0
    for d in sorted(entries.keys()):
        if entries[d][1].get():
            streak += 1
        else:
            break
    streak_label.configure(text=f"🔥 Streak: {streak} days")

def show_motivation():
    percent = progress.get()
    if percent < 0.3:
        msg = "🚨 Start Seriously!"
    elif percent < 0.7:
        msg = "💪 Keep Going!"
    else:
        msg = "🏆 You’re Crushing It!"

    motivation.configure(text=msg)

def toggle_mode():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

def search_date():
    q = search_var.get()
    for d, (e, v) in entries.items():
        if q in d:
            e.focus()
            break

# ---------------- UI BUTTONS ----------------
btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

ctk.CTkButton(btn_frame, text="💾 Save", command=save).pack(side="left", padx=5)
ctk.CTkButton(btn_frame, text="🗑 Reset", command=reset).pack(side="left", padx=5)
ctk.CTkButton(btn_frame, text="🌗 Mode", command=toggle_mode).pack(side="left", padx=5)

# Search
search_var = ctk.StringVar()
search_entry = ctk.CTkEntry(btn_frame, textvariable=search_var, placeholder_text="Search Date")
search_entry.pack(side="left", padx=5)

ctk.CTkButton(btn_frame, text="🔍", command=search_date).pack(side="left")

# ---------------- STATS ----------------
stats = ctk.CTkLabel(app, text="⏱ Total Hours: 0")
stats.pack()

streak_label = ctk.CTkLabel(app, text="🔥 Streak: 0")
streak_label.pack()

motivation = ctk.CTkLabel(app, text="")
motivation.pack()

status = ctk.CTkLabel(app, text="")
status.pack()

update_stats()

app.mainloop()