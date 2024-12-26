import smtplib
from email.mime.text import MIMEText
import os
import random
import sqlite3


def send_mail(content):
    msg = MIMEText(content)
    msg["From"] = "xxy668@foxmail.com"
    msg["To"] = "xxy668@foxmail.com"
    msg["Subject"] = "recall_mail"
    with smtplib.SMTP("smtp.qq.com", 587) as smtp:
        smtp.starttls()
        smtp.login("xxy668@foxmail.com", "kmqmrakrpovibhhe")
        smtp.send_message(msg)


def create_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE has_read (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        path TEXT
        );"""
    )
    conn.commit()
    conn.close()


def notes_path_from_os(note_path):
    notes = []
    for root, dirs, files in os.walk(note_path):
        for filename in files:
            if ".md" in filename:
                file_path = os.path.join(root, filename)
                notes.append(file_path)

    return notes


def notes_path_from_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""select path from has_read;""")
    rows = cursor.fetchall()
    has_read_notes = []
    for row in rows:
        has_read_notes.append(row[0])

    conn.commit()
    conn.close()
    return has_read_notes


def init_db(db_path):
    if not os.path.exists(db_path):
        create_db(db_path)


def remove_has_read(os_notes_path, has_read_notes_path):
    notes_without_has_read = set(os_notes_path) - set(has_read_notes_path)
    if len(notes_without_has_read) == 0:
        notes_without_has_read = os_notes_path

    return notes_without_has_read


def get_random_notes_content(notes_has_not_read):
    random_notes_path = []
    random_notes_content = ""
    while len(random_notes_content) < 5000 and len(list(notes_has_not_read))>0:
        random_note = random.choice(list(notes_has_not_read))
        random_notes_path.append(random_note)
        notes_has_not_read.remove(random_note)
        with open(random_note, "r") as f:
            content = f.read()
            if len(content) > 0:
                random_notes_content = random_notes_content + content + "\n"

    return random_notes_path, random_notes_content


def record_send(db_path, send_paths):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for path in send_paths:
        cursor.execute("insert into has_read (path) values(?)", [path])

    conn.commit()
    conn.close()


def clear_has_read_if_need(db_path, notes_has_not_read):
    if len(notes_has_not_read) == 0:
        print('clear has read')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("delete from has_read")
        conn.commit()
        conn.close()

def get_total_characters(os_notes_path):
    total_chars = 0
    for file_path in os_notes_path:
        with open(file_path, 'r') as f:
            content = f.read()
            total_chars += len(content)

    return total_chars

def main():
    note_path = "/Users/xixiaoyong/code/wiki/99-日志"
    db_path = "/Users/xixiaoyong/Downloads/note.db"
    init_db(db_path)
    os_notes_path = notes_path_from_os(note_path)
    total_characters = get_total_characters(os_notes_path)
    has_read_notes_path = notes_path_from_db(db_path)
    notes_has_not_read = remove_has_read(os_notes_path[:], has_read_notes_path)
    random_paths, random_content = get_random_notes_content(notes_has_not_read)
    send_mail(
        "total:"
        + str(len(os_notes_path))
        + ",character:"
        + str("{:,d}".format(total_characters))
        + ",\n has read:"
        + str(len(has_read_notes_path))
        + ",current:"
        + str(len(random_paths))
        + " \n"
        + random_content
    )
    clear_has_read_if_need(db_path, notes_has_not_read)
    record_send(db_path, random_paths)


if __name__ == "__main__":
    main()
