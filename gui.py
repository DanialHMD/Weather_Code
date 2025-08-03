import tkinter as tk
from tkinter import ttk, messagebox
from weather import get_location_by_city, fetch_weather


def show_weather():
    city = city_entry.get()
    try:
        hours = int(hours_entry.get())
        if not (1 <= hours <= 48):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error",
                             "Please enter a valid number of hours (1-48).")
        return

    lat, lon = get_location_by_city(city)
    if lat is None or lon is None:
        messagebox.showerror("Error", "Could not find location.")
        return

    df = fetch_weather(lat, lon, hours)
    if df is None or df.empty:
        messagebox.showerror("Error", "Could not fetch weather data.")
        return

    for row in tree.get_children():
        tree.delete(row)
    for _, row in df.iterrows():
        # Format date for better readability
        date_str = row["date"].strftime("%Y-%m-%d %H:%M")
        temp = f"{row['temperature_2m']:.1f}"
        tree.insert("", "end", values=(date_str, temp))


root = tk.Tk()
root.title("Weather Forecast")
root.iconbitmap("WeatherForecast.ico")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="x")

ttk.Label(frame, text="City:").grid(row=0, column=0, sticky="w")
city_entry = ttk.Entry(frame)
city_entry.grid(row=0, column=1, sticky="ew")
city_entry.insert(0, "Frankfurt am Main")

ttk.Label(frame, text="Hours (1-48):").grid(row=1, column=0, sticky="w")
hours_entry = ttk.Entry(frame)
hours_entry.grid(row=1, column=1, sticky="ew")
hours_entry.insert(0, "12")

fetch_btn = ttk.Button(frame, text="Get Forecast", command=show_weather)
fetch_btn.grid(row=2, column=0, columnspan=2, pady=5)

frame.columnconfigure(1, weight=1)

tree = ttk.Treeview(root,
                    columns=("Date", "Temperature (°C)"),
                    show="headings",
                    height=15)
tree.heading("Date", text="Date")
tree.heading("Temperature (°C)", text="Temperature (°C)")
tree.column("Date", width=150)
tree.column("Temperature (°C)", width=120)
tree.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()