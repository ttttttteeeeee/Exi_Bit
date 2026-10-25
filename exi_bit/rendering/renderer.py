"""Pygame drawing backend with a simple horizontal camera."""
from __future__ import annotations

import pygame

from exi_bit.engine.config import EngineConfig


class Renderer:
    def __init__(self, screen: pygame.Surface, config: EngineConfig) -> None:
        self.screen = screen
        self.config = config
        self.camera_x = 0.0

    def clear(self) -> None:
        self.screen.fill(self.config.background_color)

    def set_camera_x(self, x: float, world_width: int) -> None:
        max_x = max(0, world_width - self.config.width)
        self.camera_x = max(0.0, min(float(x), float(max_x)))

    def draw_rect(
        self,
        rect: pygame.Rect,
        color: tuple[int, int, int],
        *,
        world_space: bool = True,
        border_radius: int = 0,
    ) -> None:
        screen_rect = rect.copy()
        if world_space:
            screen_rect.x = round(screen_rect.x - self.camera_x)
        if screen_rect.right < 0 or screen_rect.left > self.config.width:
            return
        pygame.draw.rect(self.screen, color, screen_rect, border_radius=border_radius)

    def draw_text(
        self,
        text: str,
        x: int,
        y: int,
        color: tuple[int, int, int] = (240, 245, 255),
        size: int = 22,
    ) -> None:
        font = pygame.font.Font(None, size)
        self.screen.blit(font.render(text, True, color), (x, y))

    def present(self) -> None:
        pygame.display.flip()
