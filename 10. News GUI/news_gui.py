import tkinter as tk
from tkinter import ttk
import requests

def fetch_news(api_key, category):
    url = f"https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "category": category,
        "country": "us",
        "pageSize": 50  # Limit to 50 articles
    }
    response = requests.get(url, params=params)
    data = response.json()

    articles = data.get("articles", [])

    for idx, article in enumerate(articles, 1):
        title = article.get('title', '')
        if title:
            label = tk.Label(scrollable_frame, text=title, wraplength=600, anchor="w")
            label.grid(row=idx, column=0, padx=10, pady=10, sticky="w")

def fetch_specific_category(category):
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    fetch_news(api_key, category)

if __name__ == "__main__":
    api_key = "your_api_key"  # Replace "your_api_key" with your actual API key

    root = tk.Tk()
    root.title("Top News")

    categories = ["technology", "sports", "general", "gaming"]

    # Create a frame for the scrollable news articles
    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    scrollable_frame = tk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Fetch news for each category and display buttons
    for idx, category in enumerate(categories, 1):
        button = ttk.Button(root, text=category.capitalize(), command=lambda category=category: fetch_specific_category(category))
        button.pack(side=tk.TOP, padx=10, pady=5)

        fetch_news(api_key, category)

    root.mainloop()
