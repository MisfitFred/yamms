"""Minimal DatabaseManager with optional SQLCipher support.

This provides a very small abstraction for the MVP: create tables,
insert and query a student and a grade.

The API is intentionally tiny to keep the surface area small for the
first implementation.
"""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

import pysqlcipher3 as DBAPI


class DatabaseManager:
    def __init__(self, path: str | Path, password: str | None = None):
        self.path = str(path)
        self.password = password

    @contextmanager
    def connect(self) -> Iterator[DBAPI.Connection]:
        conn = DBAPI.connect(self.path)
        conn.row_factory = DBAPI.Row
        if self.password:
            conn.executescript(f"PRAGMA key = '{self.password}';")
        try:
            yield conn
        finally:
            conn.commit()
            conn.close()

    def create_tables(self) -> None:
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                    id TEXT PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    class TEXT
                )
                """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    value REAL NOT NULL,
                    date TEXT NOT NULL,
                    FOREIGN KEY(student_id) REFERENCES students(id)
                )
                """
            )

    def insert_student(
        self,
        student_id: str,
        first_name: str,
        last_name: str,
        class_name: str | None = None,
    ) -> None:
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO students (id, first_name, last_name, class) VALUES (?, ?, ?, ?)",
                (student_id, first_name, last_name, class_name),
            )

    def get_student(self, student_id: str) -> dict[str, object] | None:
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT id, first_name, last_name, class FROM students WHERE id = ?",
                (student_id,),
            )
            row = cur.fetchone()
            if not row:
                return None
            return dict(row)

    def insert_grade(
        self, student_id: str, subject: str, value: float, date: str
    ) -> None:
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO grades (student_id, subject, value, date) VALUES (?, ?, ?, ?)",
                (student_id, subject, value, date),
            )

    def get_grades_for_student(self, student_id: str) -> list[dict[str, object]]:
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT id, subject, value, date FROM grades WHERE student_id = ?",
                (student_id,),
            )
            rows = cur.fetchall()
            return [dict(r) for r in rows]
