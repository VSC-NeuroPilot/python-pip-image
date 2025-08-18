from neuro_api.api import AbstractNeuroAPI
import trio_websocket

class API(AbstractNeuroAPI):
    def __init__(self, game_title: str, connection: trio_websocket.WebSocketConnection | None = None):
        super().__init__(game_title, connection)
        self._connection = connection  # Use a private attribute for the connection
        print("INFO: " + f"Initialized with game title: {game_title}")