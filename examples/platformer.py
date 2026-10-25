"""A minimal playable platformer demonstrating the Exi_Bit Python engine.

Run from the repository root with: python -m examples.platformer
"""
from __future__ import annotations

import pygame

from exi_bit.engine import EngineConfig, ExiBitEngine
from exi_bit.input import InputManager
from exi_bit.physics import Body, PhysicsSystem
from exi_bit.rendering import Renderer
from exi_bit.world import World


class PlatformerWorld(World):
    WORLD_WIDTH = 2800

    def __init__(self) -> None:
        self.physics = PhysicsSystem(gravity=1800)
        self.player = Body(pygame.Rect(80, 380, 32, 44))
        self.platforms = [
            pygame.Rect(0, 470, 540, 100),
            pygame.Rect(630, 430, 210, 30),
            pygame.Rect(920, 370, 180, 30),
            pygame.Rect(1170, 445, 260, 30),
            pygame.Rect(1510, 390, 180, 30),
            pygame.Rect(1760, 330, 210, 30),
            pygame.Rect(2040, 430, 240, 30),
            pygame.Rect(2350, 370, 190, 30),
            pygame.Rect(2600, 310, 200, 30),
        ]
        self.goal = pygame.Rect(2700, 225, 18, 85)
        self.won = False

    def update(self, dt: float, inputs: InputManager) -> None:
        if self.won:
            return

        direction = int(inputs.is_held("right")) - int(inputs.is_held("left"))
        self.player.velocity_x = direction * 280.0

        if inputs.was_pressed("jump") and self.player.on_ground:
            self.player.velocity_y = -680.0
            self.player.on_ground = False

        self.physics.step(self.player, self.platforms, dt)

        # Keep the player inside the world bounds.
        if self.player.rect.left < 0:
            self.player.set_position(0, self.player.rect.y)
            self.player.velocity_x = 0.0
        if self.player.rect.right > self.WORLD_WIDTH:
            self.player.set_position(self.WORLD_WIDTH - self.player.rect.width, self.player.rect.y)
            self.player.velocity_x = 0.0

        if self.player.rect.colliderect(self.goal):
            self.won = True

        # A fall below the level respawns the player at the start.
        if self.player.rect.top > 700:
            self.player.set_position(80, 380)
            self.player.velocity_x = 0.0
            self.player.velocity_y = 0.0
            self.player.on_ground = False

    def render(self, renderer: Renderer) -> None:
        renderer.set_camera_x(
            self.player.rect.centerx - renderer.config.width * 0.42,
            self.WORLD_WIDTH,
        )

        # Background hills are simple shapes; all platform/player geometry is world-space.
        renderer.draw_rect(pygame.Rect(0, 0, self.WORLD_WIDTH, 900), (18, 28, 45))
        for platform in self.platforms:
            renderer.draw_rect(platform, (91, 161, 94))
            top = pygame.Rect(platform.x, platform.y, platform.width, 9)
            renderer.draw_rect(top, (148, 220, 117))

        renderer.draw_rect(self.goal, (255, 92, 112))
        renderer.draw_rect(self.player.rect, (106, 128, 255), border_radius=7)

        renderer.draw_text("Exi_Bit Python Platformer", 18, 16, size=30)
        renderer.draw_text(
            "A/D or arrows: move     Space/W/Up: jump     Esc: quit",
            18,
            48,
            color=(195, 211, 232),
            size=22,
        )
        if self.won:
            renderer.draw_text(
                "LEVEL COMPLETE!",
                renderer.config.width // 2 - 95,
                100,
                color=(167, 243, 107),
                size=34,
            )


def main() -> None:
    config = EngineConfig(title="Exi_Bit - Python Platformer")
    ExiBitEngine(world=PlatformerWorld(), config=config).run()


if __name__ == "__main__":
    main()
