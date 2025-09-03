"""Package Name Title."""

from __future__ import annotations

import os
import traceback
from typing import TYPE_CHECKING, Final

import trio
import trio_websocket
from neuro_api.trio_ws import TrioNeuroAPI
from neuro_api.command import Action

if TYPE_CHECKING:
    from neuro_api.api import NeuroAction


WEBSOCKET_ENV_VAR: Final = "NEURO_SDK_WS_URL"
DEFAULT_WEBSOCKET: Final = "ws://localhost:8000"
WEBSOCKET_CONNECTION_WAIT_TIME: Final = 0.1


class API(TrioNeuroAPI):
    """API."""

    __slots__ = ("running",)

    def __init__(
        self,
        game_title: str,
        connection: trio_websocket.WebSocketConnection | None = None,
    ) -> None:
        """Initialize API."""
        super().__init__(game_title, connection)
        print("INFO: " + f"Initialized with game title: {game_title!r}")

        self.running = True

    async def startup(self) -> None:
        """Send startup command and start game."""
        await self.send_startup_command()
        await self.register_actions(
            [
                Action("set_name", "Set name", {"type": "string"}),
            ]
        )
        await self.send_context(f"You are currently playing {self.game_title}.")
        await self.send_force_action(
            "startup_state",
            "Please set up the game",
            ["set_name"],
            ephemeral_context=False,
        )

    async def handle_action(self, action: NeuroAction) -> None:
        """Handle an Action from Neuro."""
        print(f'INFO: Received {action = }')

        success = True
        message = f"Action {action.name!r} is not currently implemented."
        print(f'INFO: {message}')
        await self.send_action_result(action.id_, success, message)

        # Close game
        self.running = False


async def main_async() -> None:
    """Main asynchronous function to run the app."""
    websocket_url = os.environ.get(WEBSOCKET_ENV_VAR, DEFAULT_WEBSOCKET)

    async with trio.open_nursery() as nursery:
        async with await trio_websocket.connect_websocket_url(nursery, websocket_url) as websocket:
            api = API("title", websocket)
            await api.startup()

            running = True
            try:
                while api.running:
                    await api.read_message()
            except Exception as exc:
                traceback.print_exc()
                await websocket.aclose(reason=f"Internal Server Error: {exc}")
            else:
                await api.send_context("Game shutting down")
                await websocket.aclose(reason="Game shutting down")


def cli_run() -> None:
    """Main function."""
    try:
        trio.run(main_async)
    except Exception:
        traceback.print_exc()


if __name__ == "__main__":
    cli_run()
