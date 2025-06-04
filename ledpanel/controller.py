"""Controlador basico do painel de LED."""

from database import connection, models


class LedPanelController:
    """Classe para controlar o painel de LED."""

    def __init__(self):
        self.conn = connection.get_connection()
        self._ensure_tables()

    def _ensure_tables(self):
        cur = self.conn.cursor()
        cur.execute(models.CREATE_TABLE_CONFIG)
        cur.execute(models.CREATE_TABLE_LOG)
        self.conn.commit()

    def ligar(self):
        """Aciona o painel."""
        self._registrar_log("painel ligado")

    def desligar(self):
        """Desliga o painel."""
        self._registrar_log("painel desligado")

    def atualizar_mensagem(self, mensagem: str):
        """Atualiza o texto exibido no painel."""
        self._registrar_log(f"mensagem atualizada: {mensagem}")

    def _registrar_log(self, mensagem: str):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO log (mensagem) VALUES (?)", (mensagem,))
        self.conn.commit()
