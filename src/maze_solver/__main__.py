# __main__.py

import argparse
import pathlib

from maze_solver.graphs.solver import solve_all, solve
from maze_solver.models.maze import Maze
from maze_solver.view.renderer import SVGRenderer


def main() -> None:
    maze = Maze.load(parse_path())
    renderer = SVGRenderer()
    # for solution in solve_all(maze):
    #     renderer.render(maze, solution).preview()
    # else:
    #     print("No solution found")
    if solution := solve(maze):
        renderer.render(maze, solution).preview()


def parse_path() -> pathlib.Path:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=pathlib.Path)
    return parser.parse_args().path


if __name__ == "__main__":
    main()
