import json
import os
from datetime import datetime

from typing import Final

FILE_PATH: Final = "./HW_02_NOURI_1/Notebook.json"


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


def check_notebook_file() -> None:
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'a') as file:
            file.write("")


def add_notebook_entry(notebook) -> None:
    notebooks = get_notebooks()
    notebooks.append(notebook.to_dict())
    add_all_to_file(notebooks)


def add_all_to_file(notebooks) -> None:
    with open(FILE_PATH, 'w') as file:
        json.dump(notebooks, file, ensure_ascii=False, indent=4)


def get_notebooks() -> list:
    if is_file_exist():
        return get_notebooks_from_file()
    else:
        check_notebook_file()
        return []


def is_file_exist() -> bool:
    return os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0


def get_notebooks_from_file() -> list:
    if is_file_exist():
        with open(FILE_PATH, 'r') as file:
            notebooks = json.load(file)
        return notebooks
    else:
        check_notebook_file()
        return []


def print_notebook(nb_dict) -> None:
    notebook = Notebook(
        nb_dict['title'],
        nb_dict['content'],
        datetime.fromisoformat(nb_dict['creation_datetime'])
    )
    print(notebook)
    print("\t\t****************************************************\n")


def create():
    title = input("Text title: ")
    content = input("Content: ")
    creation_datetime = datetime.now()
    notebook = Notebook(title, content, creation_datetime)
    add_notebook_entry(notebook)


def show():
    note_books = get_notebooks_from_file()
    for nb in note_books:
        print_notebook(nb)


def search():
    part_of_title = input("Enter a part of title: ").lower()
    notebooks = get_notebooks_from_file()

    results = [nb for nb in notebooks if part_of_title in nb['title'].lower()]

    if results:
        for nb in results:
            print_notebook(nb)
    else:
        print("No matching notes found.")


def remove():
    title_to_remove = input("enter title for remove: ").lower()
    notebooks = get_notebooks()
    removed = None

    for nb_dict in notebooks:
        if title_to_remove == nb_dict['title'].lower():
            removed = nb_dict.copy()
            notebooks.remove(nb_dict)
            break

    if removed:
        print("\t\tRemoved note:")
        print_notebook(removed)
    else:
        print("\t\tNo matching notes found.")

    add_all_to_file(notebooks)
