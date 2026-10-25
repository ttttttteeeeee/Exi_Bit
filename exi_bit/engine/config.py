"""Central runtime settings for Exi_Bit."""
from dataclasses import dataclass


@dataclass(frozen=True)
class EngineConfig:
    """Settings shared by the engine runtime."""

    title: str = "Exi_Bit"
    width: int = 960
    height: int = 540
    target_fps: int = 60
    fixed_update_hz: int = 60
    background_color: tuple[int, int, int] = (18, 28, 45)
    max_frame_time: float = 0.25

    def __post_init__(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Window dimensions must be positive.")
        if self.target_fps <= 0 or self.fixed_update_hz <= 0:
            raise ValueError("FPS and fixed update rate must be positive.")
        if self.max_frame_time <= 0:
            raise ValueError("max_frame_time must be positive.")
