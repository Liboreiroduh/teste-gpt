import os
import sqlite3

from ledpanel.controller import LedPanelController


def test_controller_creates_db(tmp_path, monkeypatch):
    db_file = tmp_path / "panel.db"
    monkeypatch.setattr("database.connection.DB_FILE", db_file)

    ctrl = LedPanelController()
    assert db_file.exists()

    # Registrar uma acao e verificar se foi gravado
    ctrl.ligar()
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM log")
    count = cur.fetchone()[0]
    assert count == 1
