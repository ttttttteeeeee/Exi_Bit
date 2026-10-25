"""Base interface for game worlds/scenes."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from exi_bit.input.input_manager import InputManager
    from exi_bit.rendering.renderer import Renderer


class World(ABC):
    """A scene that can be updated by the engine and drawn by a renderer."""

    @abstractmethod
    def update(self, dt: float, inputs: "InputManager") -> None:
        """Advance simulation by one fixed time step."""

    @abstractmethod
    def render(self, renderer: "Renderer") -> None:
        """Draw the current scene; do not mutate simulation state here."""
