"""Engine lifecycle and fixed-timestep game loop."""
from __future__ import annotations

import pygame

from exi_bit.engine.config import EngineConfig
from exi_bit.input.input_manager import InputManager
from exi_bit.rendering.renderer import Renderer
from exi_bit.world.world import World


class ExiBitEngine:
    """Owns the Pygame runtime and coordinates the engine systems."""

    def __init__(self, world: World, config: EngineConfig | None = None) -> None:
        self.config = config or EngineConfig()
        self.world = world
        self.inputs = InputManager()
        self._running = False

    def run(self) -> None:
        """Run until the user closes the window or presses Escape."""
        pygame.init()
        screen = pygame.display.set_mode((self.config.width, self.config.height))
        pygame.display.set_caption(self.config.title)
        renderer = Renderer(screen, self.config)
        clock = pygame.time.Clock()
        fixed_dt = 1.0 / self.config.fixed_update_hz
        accumulator = 0.0
        self._running = True

        try:
            while self._running:
                # 1. Collect events before simulation updates.
                frame_dt = min(
                    clock.tick(self.config.target_fps) / 1000.0,
                    self.config.max_frame_time,
                )
                for event in pygame.event.get():
                    self.inputs.process_event(event)
                if self.inputs.quit_requested:
                    self._running = False
                    break

                # 2. Update simulation in fixed-size steps for stable physics.
                accumulator += frame_dt
                while accumulator >= fixed_dt:
                    self.world.update(fixed_dt, self.inputs)
                    self.inputs.end_fixed_update()
                    accumulator -= fixed_dt

                # 3. Render the latest state, then present the frame.
                renderer.clear()
                self.world.render(renderer)
                renderer.present()
        finally:
            self._running = False
            pygame.quit()
