"""A complete, dependency-free Bubble Shooter game using tkinter.

Run with: python bubble_shooter.py
"""

from __future__ import annotations

import math
import random
import tkinter as tk
from collections import deque


WIDTH, HEIGHT = 700, 800
RADIUS = 22
DIAMETER = RADIUS * 2
COLS = 13
TOP = 72
ROW_HEIGHT = 38
SHOOTER_X, SHOOTER_Y = WIDTH // 2, 690
LEFT_WALL, RIGHT_WALL = 28, WIDTH - 28
MAX_ROWS = 15
MISS_LIMIT = 3
COLORS = ("#ff4350", "#2be04d", "#79f3ff", "#ffe200", "#ff03d6")
BG = "#fab1f3"


class BubbleShooter:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("Bubble Shooter")
        root.resizable(False, False)
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG, highlightthickness=0)
        self.canvas.pack()
        self.root.bind("<Motion>", self.aim)
        self.root.bind("<Button-1>", self.shoot)
        self.root.bind("<space>", self.shoot)
        self.root.bind("r", lambda _event: self.new_game())
        self.after_id: str | None = None
        self.mouse_x, self.mouse_y = SHOOTER_X, 300
        self.new_game()

    def new_game(self) -> None:
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.grid: dict[tuple[int, int], str] = {}
        for row in range(5):
            for col in range(COLS):
                self.grid[(row, col)] = random.choice(COLORS)
        self.score = 0
        self.misses = 0
        self.level = 1
        self.game_over = False
        self.projectile: dict[str, float | str] | None = None
        self.current = self.available_color()
        self.next_color = self.available_color()
        self.message = "Match 3 or more bubbles"
        self.draw()

    @staticmethod
    def cell_xy(row: int, col: int) -> tuple[float, float]:
        offset = RADIUS if row % 2 else 0
        return LEFT_WALL + RADIUS + offset + col * DIAMETER, TOP + RADIUS + row * ROW_HEIGHT

    @staticmethod
    def valid_cell(row: int, col: int) -> bool:
        return 0 <= row < MAX_ROWS + 2 and 0 <= col < COLS

    def neighbors(self, cell: tuple[int, int]) -> list[tuple[int, int]]:
        row, col = cell
        if row % 2 == 0:
            offsets = ((0, -1), (0, 1), (-1, -1), (-1, 0), (1, -1), (1, 0))
        else:
            offsets = ((0, -1), (0, 1), (-1, 0), (-1, 1), (1, 0), (1, 1))
        return [(row + dr, col + dc) for dr, dc in offsets if self.valid_cell(row + dr, col + dc)]

    def component(self, start: tuple[int, int], same_color: bool) -> set[tuple[int, int]]:
        wanted = self.grid.get(start)
        found, queue = {start}, deque([start])
        while queue:
            cell = queue.popleft()
            for neighbor in self.neighbors(cell):
                if neighbor in found or neighbor not in self.grid:
                    continue
                if same_color and self.grid[neighbor] != wanted:
                    continue
                found.add(neighbor)
                queue.append(neighbor)
        return found

    def available_color(self) -> str:
        choices = sorted(set(self.grid.values())) or list(COLORS)
        return random.choice(choices)

    def aim(self, event: tk.Event) -> None:
        self.mouse_x, self.mouse_y = event.x, min(event.y, SHOOTER_Y - 15)
        if not self.projectile:
            self.draw()

    def shoot(self, event: tk.Event | None = None) -> None:
        if self.game_over:
            self.new_game()
            return
        if self.projectile:
            return
        if event is not None and hasattr(event, "x"):
            self.mouse_x, self.mouse_y = event.x, min(event.y, SHOOTER_Y - 15)
        dx, dy = self.mouse_x - SHOOTER_X, self.mouse_y - SHOOTER_Y
        length = math.hypot(dx, dy)
        if length < 1:
            return
        # Upward shots only; keep enough horizontal movement for reliable wall bounces.
        dy = min(dy, -20)
        length = math.hypot(dx, dy)
        speed = 12
        self.projectile = {
            "x": float(SHOOTER_X), "y": float(SHOOTER_Y - 28),
            "vx": speed * dx / length, "vy": speed * dy / length,
            "color": self.current,
        }
        self.message = ""
        self.tick()

    def tick(self) -> None:
        if not self.projectile or self.game_over:
            return
        p = self.projectile
        p["x"] = float(p["x"]) + float(p["vx"])
        p["y"] = float(p["y"]) + float(p["vy"])
        if float(p["x"]) - RADIUS <= LEFT_WALL or float(p["x"]) + RADIUS >= RIGHT_WALL:
            p["vx"] = -float(p["vx"])
            p["x"] = max(LEFT_WALL + RADIUS, min(RIGHT_WALL - RADIUS, float(p["x"])))
        hit = float(p["y"]) - RADIUS <= TOP
        if not hit:
            for cell in self.grid:
                x, y = self.cell_xy(*cell)
                if math.hypot(float(p["x"]) - x, float(p["y"]) - y) <= DIAMETER - 3:
                    hit = True
                    break
        if hit:
            self.attach_projectile()
        self.draw()
        if self.projectile:
            self.after_id = self.root.after(16, self.tick)

    def nearest_open_cell(self, x: float, y: float) -> tuple[int, int] | None:
        approx_row = max(0, min(MAX_ROWS, round((y - TOP - RADIUS) / ROW_HEIGHT)))
        candidates: list[tuple[float, tuple[int, int]]] = []
        for row in range(max(0, approx_row - 2), min(MAX_ROWS + 1, approx_row + 3)):
            for col in range(COLS):
                cell = (row, col)
                if cell not in self.grid:
                    cx, cy = self.cell_xy(row, col)
                    candidates.append((math.hypot(x - cx, y - cy), cell))
        return min(candidates, default=(0, None), key=lambda item: item[0])[1]

    def attach_projectile(self) -> None:
        assert self.projectile
        p = self.projectile
        cell = self.nearest_open_cell(float(p["x"]), float(p["y"]))
        color = str(p["color"])
        self.projectile = None
        if cell is None:
            self.end_game(False)
            return
        self.grid[cell] = color
        group = self.component(cell, same_color=True)
        popped = 0
        dropped = 0
        if len(group) >= 3:
            popped = len(group)
            for bubble in group:
                self.grid.pop(bubble, None)
            connected: set[tuple[int, int]] = set()
            for top_cell in [c for c in self.grid if c[0] == 0]:
                connected |= self.component(top_cell, same_color=False)
            floating = set(self.grid) - connected
            dropped = len(floating)
            for bubble in floating:
                self.grid.pop(bubble, None)
            self.score += popped * 10 + dropped * 20
            self.misses = max(0, self.misses - 1)
            self.message = f"Popped {popped}" + (f" + dropped {dropped}!" if dropped else "!")
        else:
            self.misses += 1
            self.message = "No match"
            if self.misses >= MISS_LIMIT:
                self.add_row()
                self.misses = 0
                self.message = "New row added!"
        if not self.grid:
            self.end_game(True)
            return
        if any(self.cell_xy(*c)[1] + RADIUS >= SHOOTER_Y - 45 for c in self.grid):
            self.end_game(False)
            return
        self.current, self.next_color = self.next_color, self.available_color()

    def add_row(self) -> None:
        shifted: dict[tuple[int, int], str] = {}
        for (row, col), color in self.grid.items():
            new_row = row + 1
            # Preserve approximate horizontal position as the row parity changes.
            x, _ = self.cell_xy(row, col)
            best = min(range(COLS), key=lambda c: abs(self.cell_xy(new_row, c)[0] - x))
            shifted[(new_row, best)] = color
        for col in range(COLS):
            shifted[(0, col)] = random.choice(COLORS)
        self.grid = shifted
        self.level += 1

    def end_game(self, won: bool) -> None:
        self.game_over = True
        self.projectile = None
        self.message = "YOU WIN!" if won else "GAME OVER"

    def bubble(self, x: float, y: float, color: str, radius: int = RADIUS) -> None:
        c = self.canvas
        c.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color, outline="#6b205f", width=2)
        c.create_oval(x-radius*.48, y-radius*.55, x-radius*.08, y-radius*.15,
                      fill="#ffffff", outline="", stipple="gray50")

    def draw(self) -> None:
        c = self.canvas
        c.delete("all")
        c.create_rectangle(LEFT_WALL, 48, RIGHT_WALL, SHOOTER_Y + 30, fill="#ffd1f8", outline="#811578", width=4)
        c.create_text(35, 24, text=f"SCORE  {self.score}", anchor="w", fill="#5a164f", font=("Arial", 17, "bold"))
        c.create_text(WIDTH//2, 24, text=self.message, fill="#811578", font=("Arial", 15, "bold"))
        c.create_text(WIDTH-35, 24, text=f"LEVEL  {self.level}", anchor="e", fill="#5a164f", font=("Arial", 17, "bold"))
        for cell, color in self.grid.items():
            self.bubble(*self.cell_xy(*cell), color)
        # Dotted aim guide, capped to avoid aiming downward.
        dx, dy = self.mouse_x - SHOOTER_X, min(self.mouse_y, SHOOTER_Y - 20) - SHOOTER_Y
        length = max(1, math.hypot(dx, dy))
        for distance in range(45, 165, 24):
            x = SHOOTER_X + dx / length * distance
            y = SHOOTER_Y + dy / length * distance
            c.create_oval(x-3, y-3, x+3, y+3, fill="#811578", outline="")
        c.create_rectangle(245, 720, 455, 765, fill="#811578", outline="")
        self.bubble(SHOOTER_X, SHOOTER_Y, self.current)
        self.bubble(510, 743, self.next_color, 15)
        c.create_text(535, 743, text="NEXT", anchor="w", fill="#811578", font=("Arial", 12, "bold"))
        hearts = MISS_LIMIT - self.misses
        c.create_text(32, 743, text="♥" * hearts + "♡" * self.misses, anchor="w", fill="#f03f3f", font=("Arial", 25, "bold"))
        c.create_text(WIDTH//2, 786, text="Mouse to aim • Click/Space to shoot • R to restart", fill="#5a164f", font=("Arial", 12))
        if self.projectile:
            self.bubble(float(self.projectile["x"]), float(self.projectile["y"]), str(self.projectile["color"]))
        if self.game_over:
            c.create_rectangle(150, 315, 550, 455, fill="#fff0fd", outline="#811578", width=4)
            c.create_text(WIDTH//2, 355, text=self.message, fill="#811578", font=("Arial", 32, "bold"))
            c.create_text(WIDTH//2, 400, text=f"Final score: {self.score}", fill="#5a164f", font=("Arial", 18, "bold"))
            c.create_text(WIDTH//2, 430, text="Click or press R to play again", fill="#5a164f", font=("Arial", 13))


def main() -> None:
    root = tk.Tk()
    BubbleShooter(root)
    root.mainloop()


if __name__ == "__main__":
    main()
