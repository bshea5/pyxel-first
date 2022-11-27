from typing import List
import random
import pyxel
from dataclasses import dataclass, asdict


class Drawable:
    def draw(self):
        pass


@dataclass
class PyxelSquare(Drawable):
    x: int
    y: int
    w: int
    h: int
    col: int

    def draw(self):
        pyxel.rect(**asdict(self))


@dataclass
class PyxelTriangle(Drawable):
    x1: float
    y1: float
    x2: float
    y2: float
    x3: float
    y3: float
    col: int

    def draw(self):
        return pyxel.tri(**asdict(self))


class Game:
    player: PyxelSquare | None = None
    snow: List[PyxelSquare] = []
    drawables: List[Drawable] = []

    def __init__(self):
        pyxel.init(160, 120)
        pyxel
        self.snow = [
            PyxelSquare(
                random.randint(x, 160),
                random.randint(0, 120),
                2,
                2,
                pyxel.COLOR_LIGHT_BLUE,
            )
            for x in range(50)
        ]
        clouds = [
            PyxelSquare(0, 0, 60, 10, pyxel.COLOR_GRAY),
            PyxelSquare(10, 0, 60, 20, pyxel.COLOR_GRAY),
            PyxelSquare(60, 0, 60, 10, pyxel.COLOR_GRAY),
            PyxelSquare(80, 0, 60, 20, pyxel.COLOR_GRAY),
            PyxelSquare(100, 0, 60, 10, pyxel.COLOR_GRAY),
        ]
        ground = [
            PyxelSquare(0, 110, 160, 10, pyxel.COLOR_LIGHT_BLUE),
            PyxelSquare(20, 100, 60, 20, pyxel.COLOR_LIGHT_BLUE),
            PyxelSquare(90, 100, 30, 20, pyxel.COLOR_LIGHT_BLUE),
        ]
        trees = [
            PyxelTriangle(20, 100, 30, 100, 25, 90, pyxel.COLOR_GREEN),
            PyxelTriangle(35, 100, 45, 100, 40, 90, pyxel.COLOR_GREEN),
            PyxelTriangle(70, 100, 80, 100, 75, 90, pyxel.COLOR_GREEN),
            PyxelTriangle(95, 100, 105, 100, 100, 90, pyxel.COLOR_GREEN),
        ]
        self.drawables = [
            PyxelSquare(0, 0, 160, 120, pyxel.COLOR_DARK_BLUE),
            *self.snow,
            *clouds,
            *ground,
            *trees,
        ]
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            self.exit()

        for s in self.snow:
            s.x = s.x + random.randint(-1, 1)  # % pyxel.width
            s.y = (s.y + 1) % pyxel.height

            s.x = -s.x if random.randint(0, 1) else s.x

    def draw(self):
        pyxel.cls(0)

        for e in self.drawables:
            e.draw()

    def exit(self):
        print("exiting")
        pyxel.quit()
