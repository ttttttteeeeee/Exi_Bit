"""Small reusable 2D rectangle-physics helpers."""
from __future__ import annotations

from dataclasses import dataclass, field
import pygame


@dataclass
class Body:
    """A movable rectangle with velocity measured in pixels per second."""

    rect: pygame.Rect
    velocity_x: float = 0.0
    velocity_y: float = 0.0
    on_ground: bool = False
    _x: float = field(init=False, repr=False)
    _y: float = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.rect = self.rect.copy()
        self._x = float(self.rect.x)
        self._y = float(self.rect.y)


class PhysicsSystem:
    """Applies gravity and resolves axis-aligned platform collisions."""

    def __init__(self, gravity: float = 1800.0) -> None:
        if gravity < 0:
            raise ValueError("Gravity must be non-negative.")
        self.gravity = gravity

    def step(self, body: Body, solids: list[pygame.Rect], dt: float) -> None:
        """Advance one fixed simulation step, resolving horizontal then vertical hits."""
        if dt < 0:
            raise ValueError("dt must be non-negative.")

        body.velocity_y = min(body.velocity_y + self.gravity * dt, 1400.0)

        # Horizontal axis: walls stop horizontal velocity.
        body._x += body.velocity_x * dt
        body.rect.x = round(body._x)
        for solid in solids:
            if body.rect.colliderect(solid):
                if body.velocity_x > 0:
                    body.rect.right = solid.left
                elif body.velocity_x < 0:
                    body.rect.left = solid.right
                body._x = float(body.rect.x)
                body.velocity_x = 0.0

        # Vertical axis: landing sets on_ground; ceilings stop upward motion.
        body._y += body.velocity_y * dt
        body.rect.y = round(body._y)
        body.on_ground = False
        for solid in solids:
            if body.rect.colliderect(solid):
                if body.velocity_y > 0:
                    body.rect.bottom = solid.top
                    body.on_ground = True
                elif body.velocity_y < 0:
                    body.rect.top = solid.bottom
                body._y = float(body.rect.y)
                body.velocity_y = 0.0
