# exercises/hello-fastapi/main.py
# L1 — Hello FastAPI
#
# Your task: Build a simple FastAPI app with several endpoints demonstrating
# core concepts: decorators, path parameters, and automatic documentation.
#
# Run with: uvicorn main:app --reload
# Docs at:  http://127.0.0.1:8000/docs
#python3 -m uvicorn main:app --reload

# TODO: Import FastAPI from the fastapi package
from fastapi import FastAPI

# TODO: Create a FastAPI app instance
# Hint: app = FastAPI()
app = FastAPI()


# TODO: Define a root endpoint at GET /
# It should return a welcome message as a dictionary, e.g.:


# Key concept: The @app.get("/") decorator tells FastAPI to call this
# function whenever a GET request is made to the "/" path.
@app.get("/")
def root():
    """
    Root endpoint — returns a welcome message.
"""
    return {"message": "Welcome to Hello FastAPI!"}


# TODO: Define GET /hello that returns a plain string greeting
@app.get("/hello")
def say_hello():
    """
    Returns a simple string greeting.

    TODO: Return a string like "Hello, FastAPI!"
    """
    return "Hello, FastAPI!"


# TODO: Define GET /info that returns a dictionary with app metadata
# Include keys like "name", "version", and "description"
@app.get("/info")
def get_info():
    """
    Returns app metadata as a dict.

    TODO: Return a dict with at least "name", "version", "description".
    """
    return {
        "name": "Hello FastAPI",
        "version": "0.1.0",
        "description": "A simple FastAPI app for learning purposes."
    }


# TODO: Define GET /items that returns a list of example items
# Each item should be a dict with at least "id" and "name"
@app.get("/items")
def list_items():
    """
    Returns a list of example items.

    TODO: Return a list of dicts, e.g. [{"id": 1, "name": "Widget"}, ...]
    """
    return [
        {"id": 1, "name": "Widget"},
        {"id": 2, "name": "Gadget"},
        {"id": 3, "name": " contraption"}
    ]


# TODO: Define GET /items/{item_id} that accepts a path parameter
# Return a dict that includes the item_id you received
#
# Key concept: Path parameters are defined with {curly_braces} in the path
# and appear as function arguments with matching names.
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """
    Returns a single item by ID.

    Args:
        item_id: The integer ID from the URL path.

    TODO: Return a dict like {"id": item_id, "name": "...", "description": "..."}
    """
    return {"id": item_id, "name": f"Item {item_id}", "description": f"This is item {item_id}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)