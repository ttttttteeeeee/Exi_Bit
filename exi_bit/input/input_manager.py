"""Translate raw Pygame events into game actions."""
from __future__ import annotations

import pygame


class InputManager:
    """Tracks held and newly pressed actions.

    New presses stay available until a fixed update consumes them, so a short
    key press is not lost when a rendered frame performs zero physics steps.
    """

    def __init__(self) -> None:
        self._held: set[str] = set()
        self._pressed: set[str] = set()
        self._quit_requested = False

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self._quit_requested = True
        elif event.type == pygame.KEYDOWN:
            action = self._key_to_action(event.key)
            if action and action not in self._held:
                self._pressed.add(action)
                self._held.add(action)
            if event.key == pygame.K_ESCAPE:
                self._quit_requested = True
        elif event.type == pygame.KEYUP:
            action = self._key_to_action(event.key)
            if action:
                self._held.discard(action)

    @staticmethod
    def _key_to_action(key: int) -> str | None:
        mapping = {
            pygame.K_LEFT: "left",
            pygame.K_a: "left",
            pygame.K_RIGHT: "right",
            pygame.K_d: "right",
            pygame.K_SPACE: "jump",
            pygame.K_UP: "jump",
            pygame.K_w: "jump",
        }
        return mapping.get(key)

    def is_held(self, action: str) -> bool:
        return action in self._held

    def was_pressed(self, action: str) -> bool:
        return action in self._pressed

    @property
    def quit_requested(self) -> bool:
        return self._quit_requested

    def end_fixed_update(self) -> None:
        """Clear one-shot actions after a simulation step."""
        self._pressed.clear()
