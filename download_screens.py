import urllib.request
import os

screens = {
    "5ab49cc6fe034acf9e8f93f1e9855708": "Events",
    "4b58174c8d0b4ffeb526cca2cafc2a26": "Private_Dining",
    "9a535f2d7d5e4317af03284a7161db5d": "Gift_Cards",
    "a72bcba7db6546789c0bc904ac079b5a": "Home_Screen",
    "dbd4b14b3541448b8aa3c7f6425ea759": "Sunday_Brunch",
    "6b55e65d852c4729841c4d2e3f537790": "Splash_Screen",
    "6776556ead48487fb8faf85251967ff4": "Reservations",
    "a258b9bda9ed4944808d36a5cd7c3486": "Loyalty_Rewards",
    "c5db11f44a5d49c1aec68bf517e824ff": "Menu_Screen"
}

urls = {
    "Events": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NTVlMTJlOTZjNzQwMzgzOWY4NDZhMWFjNjM3EgsSBxCi9YrErBUYAZIBIwoKcHJvamVjdF9pZBIVQhM4ODIxODE3OTcyNTE3MDU1NTky&filename=&opi=89354086",
    "Private_Dining": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NTVlMTMxNTNlNDEwMzM4NDcyZGZkMTZiYWMzEgsSBxCi9YrErBUYAZIBIwoKcHJvamVjdF9pZBIVQhM4ODIxODE3OTcyNTE3MDU1NTky&filename=&opi=89354086",
    "Gift_Cards": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NTVlMTI1NjZhM2IwN2M0ZDIyMDQ1MjhlZWEyEgsSBxCi9YrErBUYAZIBIwoKcHJvamVjdF9pZBIVQhM4ODIxODE3OTcyNTE3MDU1NTky&filename=&opi=89354086",
    "Home_Screen": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NTVlMTcwNTg0MTQwNmMyNzc1ZWUwMmJjZjljEgsSBxCi9YrErBUYAZIBIwoKcHJvamVjdF9pZBIVQhM4ODIxODE3OTcyNTE3MDU1NTky&filename=&opi=89354086",
    "Sunday_Brunch": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NTVlMTJiZmM4YTUwMzgzOWY4NDZhMWFjNjM3EgsSBxCi9YrErBUYAZIBIwoKcHJvamVjdF9pZBIVQhM4ODIxODE3OTcyNTE3MDU1NTky&filename=&opi=89354086",
    "Splash_Screen": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NTVlMTQ0Mzc0ODgwOTI1ZDNiZDBiMGZkNzYwEgsSBxCi9YrErBUYAZIBIwoKcHJvamVjdF9pZBIVQhM4ODIxODE3OTcyNTE3MDU1NTky&filename=&opi=89354086",
    "Reservations": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NTVlMTJkOGUwZGQwMzRhNGUxODZlMzJkYjU0EgsSBxCi9YrErBUYAZIBIwoKcHJvamVjdF9pZBIVQhM4ODIxODE3OTcyNTE3MDU1NTky&filename=&opi=89354086",
    "Loyalty_Rewards": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NTVlMTJmZTA2NjkwMmQzYzI4YjczMTg0NmRhEgsSBxCi9YrErBUYAZIBIwoKcHJvamVjdF9pZBIVQhM4ODIxODE3OTcyNTE3MDU1NTky&filename=&opi=89354086",
    "Menu_Screen": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NTVlMTMzZjg4NzIwMmQzY2FlYTA5MzM3NjFlEgsSBxCi9YrErBUYAZIBIwoKcHJvamVjdF9pZBIVQhM4ODIxODE3OTcyNTE3MDU1NTky&filename=&opi=89354086"
}

os.makedirs("downloaded_screens", exist_ok=True)

for name, url in urls.items():
    print(f"Downloading {name}...")
    try:
        urllib.request.urlretrieve(url, f"downloaded_screens/{name}.html")
        print(f"Success: {name}")
    except Exception as e:
        print(f"Error downloading {name}: {e}")
