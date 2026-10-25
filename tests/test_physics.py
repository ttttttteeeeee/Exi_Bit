"""Unit tests for the basic rectangle physics system."""
import unittest

import pygame

from exi_bit.physics import Body, PhysicsSystem


class PhysicsSystemTests(unittest.TestCase):
    def test_body_lands_on_platform(self) -> None:
        body = Body(pygame.Rect(10, 40, 20, 20))
        floor = pygame.Rect(0, 100, 200, 20)
        physics = PhysicsSystem(gravity=900)

        for _ in range(120):
            physics.step(body, [floor], 1 / 60)

        self.assertTrue(body.on_ground)
        self.assertEqual(body.rect.bottom, floor.top)
        self.assertEqual(body.velocity_y, 0)

    def test_horizontal_collision_stops_body(self) -> None:
        body = Body(pygame.Rect(0, 10, 20, 20), velocity_x=200)
        wall = pygame.Rect(30, 0, 20, 80)
        physics = PhysicsSystem(gravity=0)

        physics.step(body, [wall], 0.2)

        self.assertEqual(body.rect.right, wall.left)
        self.assertEqual(body.velocity_x, 0)

    def test_negative_delta_is_rejected(self) -> None:
        body = Body(pygame.Rect(0, 0, 10, 10))
        physics = PhysicsSystem()

        with self.assertRaises(ValueError):
            physics.step(body, [], -0.01)


if __name__ == "__main__":
    unittest.main()
