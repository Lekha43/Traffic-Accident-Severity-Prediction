import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from sklearn.tree import DecisionTreeClassifier

# 1. Create dataset
data = {
    "Weather": ["Clear", "Rainy", "Foggy", "Clear", "Rainy",
               "Foggy", "Clear", "Rainy", "Clear", "Foggy",
               "Rainy", "Clear", "Foggy", "Rainy", "Clear"],

    "Road": ["Urban", "Highway", "Rural", "Highway", "Urban",
             "Rural", "Urban", "Highway", "Rural", "Urban",
             "Highway", "Urban", "Rural", "Highway", "Urban"],

    "Time": ["Morning", "Night", "Evening", "Afternoon", "Night",
             "Morning", "Evening", "Afternoon", "Morning", "Night",
             "Evening", "Morning", "Night", "Night", "Afternoon"],

    "History": ["Low", "High", "Medium", "Low", "High",
                "Medium", "Low", "High", "Medium", "High",
                "High", "Low", "Medium", "High", "Low"],

    "Severity": ["Minor", "Severe", "Moderate", "Minor", "Severe",
                 "Moderate", "Minor", "Severe", "Moderate", "Severe",
                 "Severe", "Minor", "Moderate", "Severe", "Minor"]
}

df = pd.DataFrame(data)

# 2. Train prediction model
X = pd.get_dummies(df[["Weather", "Road", "Time", "History"]])
y = df["Severity"]

model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X, y)

# 3. Create dashboard window
root = tk.Tk()
root.title("Traffic Accident Severity Dashboard")
root.geometry("900x700")
root.configure(bg="#eef2f7")

# Dashboard title
tk.Label(
    root,
    text="TRAFFIC ACCIDENT DASHBOARD",
    font=("Arial", 20, "bold"),
    bg="#1f3a5f",
    fg="white",
    pady=15
).pack(fill="x")

# 4. Summary cards
summary = tk.Frame(root, bg="#eef2f7")
summary.pack(pady=20)

def make_card(text, value, color):
    card = tk.Frame(summary, bg=color, padx=25, pady=15)
    card.pack(side="left", padx=10)

    tk.Label(
        card, text=text,
        font=("Arial", 11),
        bg=color, fg="white"
    ).pack()

    tk.Label(
        card, text=str(value),
        font=("Arial", 22, "bold"),
        bg=color, fg="white"
    ).pack()

make_card("Total Accidents", len(df), "#1f3a5f")
make_card("Minor", (y == "Minor").sum(), "#27966b")
make_card("Moderate", (y == "Moderate").sum(), "#d99a20")
make_card("Severe", (y == "Severe").sum(), "#c0392b")

# 5. Prediction form
frame = tk.LabelFrame(
    root,
    text="Predict Accident Severity",
    font=("Arial", 12, "bold"),
    bg="#eef2f7",
    padx=20,
    pady=15
)
frame.pack(pady=10)

def add_dropdown(label, options, row):
    tk.Label(
        frame, text=label,
        bg="#eef2f7",
        font=("Arial", 11)
    ).grid(row=row, column=0, padx=10, pady=8)

    combo = ttk.Combobox(
        frame,
        values=options,
        state="readonly",
        width=18
    )
    combo.current(0)
    combo.grid(row=row, column=1, padx=10, pady=8)

    return combo

weather = add_dropdown(
    "Weather", ["Clear", "Rainy", "Foggy"], 0
)

road = add_dropdown(
    "Road Type", ["Urban", "Highway", "Rural"], 1
)

time = add_dropdown(
    "Time", ["Morning", "Afternoon", "Evening", "Night"], 2
)

history = add_dropdown(
    "Accident History", ["Low", "Medium", "High"], 3
)

# 6. Prediction function
def predict():
    sample = pd.DataFrame([{
        "Weather": weather.get(),
        "Road": road.get(),
        "Time": time.get(),
        "History": history.get()
    }])

    sample = pd.get_dummies(sample)
    sample = sample.reindex(columns=X.columns, fill_value=0)

    result = model.predict(sample)[0]

    messagebox.showinfo(
        "Prediction Result",
        "Weather: " + weather.get() +
        "\nRoad Type: " + road.get() +
        "\nTime: " + time.get() +
        "\nAccident History: " + history.get() +
        "\n\nPredicted Severity: " + result
    )

tk.Button(
    frame,
    text="Predict Severity",
    command=predict,
    bg="#1f3a5f",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8
).grid(row=4, column=0, columnspan=2, pady=15)

# 7. Graph 1 - Severity distribution
def show_severity():
    counts = df["Severity"].value_counts().reindex(
        ["Minor", "Moderate", "Severe"], fill_value=0
    )

    plt.figure(figsize=(6, 4))
    counts.plot(kind="bar", color=["green", "orange", "red"])

    plt.title("Accident Severity Distribution")
    plt.xlabel("Severity")
    plt.ylabel("Number of Accidents")
    plt.tight_layout()
    plt.show()

# 8. Graph 2 - Weather analysis
def show_weather():
    table = pd.crosstab(df["Weather"], df["Severity"])

    table.plot(kind="bar")
    plt.title("Weather vs Accident Severity")
    plt.xlabel("Weather")
    plt.ylabel("Number of Accidents")
    plt.tight_layout()
    plt.show()

# 9. Graph 3 - Road type analysis
def show_road():
    table = pd.crosstab(df["Road"], df["Severity"])

    table.plot(kind="bar")
    plt.title("Road Type vs Accident Severity")
    plt.xlabel("Road Type")
    plt.ylabel("Number of Accidents")
    plt.tight_layout()
    plt.show()

# 10. Graph buttons
graphs = tk.Frame(root, bg="#eef2f7")
graphs.pack(pady=20)

tk.Button(
    graphs,
    text="Severity Graph",
    command=show_severity,
    width=18
).grid(row=0, column=0, padx=10, pady=10)

tk.Button(
    graphs,
    text="Weather Graph",
    command=show_weather,
    width=18
).grid(row=0, column=1, padx=10, pady=10)

tk.Button(
    graphs,
    text="Road Type Graph",
    command=show_road,
    width=18
).grid(row=0, column=2, padx=10, pady=10)

# 11. Display dataset
def show_data():
    window = tk.Toplevel(root)
    window.title("Accident Dataset")
    window.geometry("700x350")

    table = ttk.Treeview(
        window,
        columns=list(df.columns),
        show="headings"
    )

    for col in df.columns:
        table.heading(col, text=col)
        table.column(col, width=120)

    for _, row in df.iterrows():
        table.insert("", "end", values=list(row))

    table.pack(fill="both", expand=True)

tk.Button(
    root,
    text="View Dataset",
    command=show_data,
    font=("Arial", 11),
    padx=15,
    pady=8
).pack(pady=10)

# 12. Start dashboard
root.mainloop()
