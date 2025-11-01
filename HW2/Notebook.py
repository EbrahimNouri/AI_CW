import json
import os
from datetime import datetime

___file_path___ = "notebook.json"

from pprint import pprint


# my_class.py
class Notebook:
    def __init__(self, title, content, creation_datetime):
        self.title = title
        self.content = content
        self.creation_datetime = creation_datetime

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "creation_datetime": self.creation_datetime.isoformat()
        }

    def __str__(self):
        formatted_date = self.creation_datetime.strftime("%A, %B %d, %Y %H:%M:%S")
        return f"""
        Title: {self.title}
        Content: {self.content}
        Created at: {formatted_date}
        """


def check_notebook_file():
    if not os.path.exists(___file_path___):
        with open(___file_path___, 'a') as file:
            file.write("")


def add_notebook_entry(notebook):
    notebooks = []

    notebooks = get_notebooks(notebook, notebooks)

    with open(___file_path___, 'w') as file:
        json.dump(notebooks, file, ensure_ascii=False, indent=4)


def get_notebooks(notebook, notebooks):
    if os.path.exists(___file_path___) and os.path.getsize(___file_path___) > 0:
        notebooks = get_notebooks_from_file(___file_path___)

    notebooks.append(notebook.to_dict())
    return notebooks


def get_notebooks_from_file(file_path: str):
    with open(file_path, 'r') as file:
        notebooks = json.load(file)
    return notebooks


def create():
    title = input("Text title: ")
    content = input("Content: ")
    creation_datetime = datetime.now()
    notebook = Notebook(title, content, creation_datetime)
    add_notebook_entry(notebook)


def show():
    note_books = get_notebooks_from_file(___file_path___)
    for nb_dict in note_books:
        notebook = Notebook(
            nb_dict['title'],
            nb_dict['content'],
            datetime.fromisoformat(nb_dict["creation_datetime"])
        )
        print(notebook)
        print("*****************************************************\n")


def search():
    part_of_title = input("Enter a part of title: ").lower()
    notebooks = get_notebooks_from_file(___file_path___)

    results = [nb for nb in notebooks if part_of_title in nb['title'].lower()]

    if results:
        print("*****************************************************")
        for nb in results:
            dt = datetime.fromisoformat(nb['creation_datetime'])
            formatted_date = dt.strftime("%A, %B %d, %Y %H:%M:%S")
            print(f"""
                          Title: {nb['title']}
                          Content: {nb['content']}
                          Created at: {formatted_date}
                          """)
            print("*****************************************************")
        else:
            print("No matching notes found.")

        def remove():
            title_to_remove = input("enter title for remove: ").lower()
            notebooks = []

            notebooks = get_notebooks(notebook, notebooks)

            with open(___file_path___, 'w') as file:
                json.dump(notebooks, file, ensure_ascii=False, indent=4)

        # def exit():
