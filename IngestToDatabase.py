import sqlite3
import os
from idlelib.iomenu import encoding

from bs4 import BeautifulSoup
from charset_normalizer.cd import characters_popularity_compare


# from ReadDataForLLM import information


# import fitz


# Reading Text from HTML Files
def extract_text_from_html(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        soup = BeautifulSoup(file, 'html.parser')
        text = soup.get_text()
    return text


def clean_html_content(content):
    # strip unwanted characters
    clean_content = ' '.join(content.split())  # removes extra whitespace
    return clean_content


# Reading Text from PDF file
""" 
def extract_text_from_pdf(file_path):
    text=""
    pdf_document = fitz.open(file_path)
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
    pdf_document.close()
    return text
"""


def store_in_database(file_name, content):
    conn = sqlite3.connect("./DocumentDatabase/document.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO documents (file_name, content) VALUES(?,?)

    ''', (file_name, content))
    conn.commit()
    conn.close()


def fetch_file_content_by_name(db_path, file_name):
    # Coonect  to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query to select content where the file name matches  the specified name

    cursor.execute("SELECT content FROM documents WHERE file_name =?", (file_name,))

    # Fetch the result

    row = cursor.fetchone()

    # Close the database connection
    conn.close()

    # if a file with a given name was found, store its content in the variable 'information'

    if row:
        information = row[0]  # store the content in the information
        print(f"Content of {file_name} : {information[:200]}....")  # print the first 200 characters as a preview
        return information
    else:
        print(f"No file found with the name '{file_name}'.")
        return None


if __name__ == "__main__":
    file_paths = ["./store-docs/Executive summary.htm", "./store-docs/Psoriasis Area and Severity Index response.htm"]

    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        if file_path.endswith('.htm'):
            content = extract_text_from_html(file_path)
            print(content)
            # clean the content
            clean_content = clean_html_content(content)
        # elif file_path.endswith('.pdf'):
        # content = extract_text_from_pdf(file_path)
        else:
            print(f"Unsopported file format for {file_path}")

        # get clean content

        store_in_database(file_name, clean_content)
        print(f"stored{file_name} in database.")

        print(clean_content)




