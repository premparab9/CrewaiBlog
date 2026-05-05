import os

def save_blog(content: str):
    os.makedirs("output", exist_ok=True)
    with open("output/blog.md", "w", encoding="utf-8") as f:
        f.write(content)
