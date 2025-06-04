"""Modulo de conexao com banco de dados SQLite."""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent / "panel.db"


def get_connection():
    """Retorna uma conexao SQLite para o arquivo padrao."""
    conn = sqlite3.connect(DB_FILE)
    return conn
