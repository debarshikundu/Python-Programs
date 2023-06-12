"""Making a shirt"""

def make_shirt(size = "large", message="I love Python."):
    print(f"Big {size}, {message}")

make_shirt(8, "yoyoyo...")

make_shirt(size=5, message="small")

make_shirt()

make_shirt("medium")

make_shirt("small", "Hello World!")