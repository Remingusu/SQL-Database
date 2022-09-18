import os
import sqlite3


class DatabaseHandler:
    def __init__(self, database_name: str):
        self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        self.con.row_factory = sqlite3.Row

    def create_person(self, username: str, password: str, age: int):
        cursor = self.con.cursor()
        query = f"INSERT INTO Personnes(username, password, age) VALUES(?, ?, ?);"
        cursor.execute(query, (username, password, age))
        cursor.close()
        self.con.commit()

    def password_for(self, username: str) -> str:
        cursor = self.con.cursor()
        query = f"SELECT password FROM Personnes WHERE username = ?;"
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        cursor.close()
        return dict(result[0])["Password"]

    def user_exists_with(self, username: str) -> bool:
        cursor = self.con.cursor()
        query = f"SELECT * FROM Personnes WHERE username = ?;"
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        cursor.close()
        return len(result) == 1

    def user_list(self):
        cursor = self.con.cursor()
        query = f"SELECT username FROM Personnes;"
        cursor.execute(query)
        result = cursor.fetchall()
        result = map(dict, result)
        cursor.close()
        return result

    def change_password(self, username : str, new_password : str):
        cursor = self.con.cursor()
        query = f"UPDATE Personnes SET password = ?, nbPasswordChange = nbPasswordChange + 1 WHERE username = ?;"
        cursor.execute(query, (new_password, username))
        cursor.close()
        self.con.commit()

    def description(self, username: str) -> dict:
        cursor = self.con.cursor()
        query = f"SELECT description FROM Personnes WHERE username = ?;"
        cursor.execute(query, (username,))
        result = dict(cursor.fetchall()[0])
        cursor.close()
        return result

    def change_description(self, username: str, new_description: str):
        cursor = self.con.cursor()
        query = f"UPDATE Personnes SET description = ? WHERE username = ?;"
        cursor.execute(query, (new_description, username))
        cursor.close()
        self.con.commit()