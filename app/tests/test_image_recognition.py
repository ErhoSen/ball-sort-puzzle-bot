from pathlib import Path

import numpy as np
import pytest
from image import ImageParser
from modules import color
from solver import BallSortPuzzle

FILE_PATH = Path(__file__)


def test_image1():
    file_path = FILE_PATH.parent / "img/lvl_725.jpg"
    with open(file_path, 'rb') as f:
        file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
        image_parser = ImageParser(file_bytes, debug=False)
        colors = image_parser.to_colors()

    assert colors == [
        [color.L_BLUE, color.L_BLUE, color.GREEN, color.L_GREEN],
        [color.PINK, color.PINK, color.BLUE, color.BROWN],
        [color.LIME, color.L_GREEN, color.VIOLET, color.VIOLET],
        [color.VIOLET, color.L_GREEN, color.GRAY, color.ORANGE],
        [color.RED, color.GREEN, color.BROWN, color.ORANGE],
        [color.PINK, color.LIME, color.VIOLET, color.BLUE],
        [color.ORANGE, color.LIME, color.YELLOW, color.L_BLUE],
        [color.LIME, color.GREEN, color.RED, color.L_GREEN],
        [color.GREEN, color.YELLOW, color.GRAY, color.BLUE],
        [color.L_BLUE, color.RED, color.GRAY, color.BROWN],
        [color.ORANGE, color.YELLOW, color.PINK, color.GRAY],
        [color.YELLOW, color.RED, color.BROWN, color.BLUE],
        [],
        [],
    ]


def test_image2():
    file_path = FILE_PATH.parent / "img/lvl_863.jpg"
    with open(file_path, 'rb') as f:
        file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
        image_parser = ImageParser(file_bytes)
        colors = image_parser.to_colors()

    assert colors

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is True


def test_image3():
    file_path = FILE_PATH.parent / "img/lvl_1051.jpg"
    with open(file_path, 'rb') as f:
        file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
        image_parser = ImageParser(file_bytes)
        colors = image_parser.to_colors()

    assert colors

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is True


@pytest.mark.parametrize(
    'filename',
    [
        'img/lvl_5462.jpg',
        'img/lvl_10300.jpg',
        'img/lvl_5461.jpg',
    ],
)
def test_image_android(filename):
    file_path = FILE_PATH.parent / filename
    with open(file_path, 'rb') as f:
        file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
        image_parser = ImageParser(file_bytes, debug=False)
        colors = image_parser.to_colors()

    assert colors

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is True


@pytest.mark.parametrize(
    'filename',
    [
        'img/lvl_6071.jpg',
        'img/lvl_4091.jpg',
    ],
)
def test_no_solution(filename):
    file_path = FILE_PATH.parent / filename
    with open(file_path, 'rb') as f:
        file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
        image_parser = ImageParser(file_bytes, debug=False)
        colors = image_parser.to_colors()

    assert colors

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is False


def test_nine_flasks():
    file_path = FILE_PATH.parent / "img/lvl_1056.jpg"
    with open(file_path, 'rb') as f:
        file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
        image_parser = ImageParser(file_bytes)
        colors = image_parser.to_colors()

    assert colors

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is True


def test_image_and_solve():
    file_path = FILE_PATH.parent / "img/lvl_725.jpg"
    with open(file_path, 'rb') as f:
        file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
        image_parser = ImageParser(file_bytes)
        colors = image_parser.to_colors()

    puzzle = BallSortPuzzle(colors)
    result = puzzle.solve()
    assert result is True
    assert (
        str(puzzle.moves)
        == "[Ball(0 -> 12), Ball(1 -> 13), Ball(7 -> 12), Ball(11 -> 1), Ball(13 -> 11), Ball(3 -> 13), "
        "Ball(4 -> 13), Ball(9 -> 4), Ball(3 -> 9), Ball(12 -> 3), Ball(12 -> 3), Ball(4 -> 12), "
        "Ball(4 -> 12), Ball(0 -> 4), Ball(6 -> 0), Ball(11 -> 12), Ball(11 -> 12), Ball(7 -> 11), "
        "Ball(4 -> 7), Ball(4 -> 7), Ball(4 -> 11), Ball(1 -> 4), Ball(1 -> 4), Ball(5 -> 4), Ball(2 -> "
        "5), Ball(8 -> 4), Ball(5 -> 2), Ball(9 -> 8), Ball(2 -> 5), Ball(10 -> 9), Ball(1 -> 10), "
        "Ball(5 -> 2), Ball(10 -> 1), Ball(10 -> 1), Ball(2 -> 5), Ball(10 -> 6), Ball(5 -> 2), "
        "Ball(10 -> 13), Ball(2 -> 5), Ball(3 -> 10), Ball(3 -> 10), Ball(3 -> 10), Ball(2 -> 3), "
        "Ball(2 -> 10), Ball(5 -> 3), Ball(5 -> 3), Ball(2 -> 5), Ball(6 -> 2), Ball(6 -> 2), Ball(5 -> "
        "6), Ball(5 -> 6), Ball(5 -> 1), Ball(2 -> 5), Ball(2 -> 5), Ball(6 -> 2), Ball(6 -> 2), "
        "Ball(6 -> 2), Ball(6 -> 13), Ball(5 -> 6), Ball(5 -> 6), Ball(7 -> 5), Ball(7 -> 5), Ball(7 -> "
        "5), Ball(7 -> 2), Ball(6 -> 7), Ball(6 -> 7), Ball(8 -> 6), Ball(8 -> 6), Ball(7 -> 8), "
        "Ball(7 -> 8), Ball(6 -> 7), Ball(6 -> 7), Ball(8 -> 6), Ball(8 -> 6), Ball(8 -> 6), Ball(8 -> "
        "5), Ball(7 -> 8), Ball(7 -> 8), Ball(9 -> 7), Ball(7 -> 8), Ball(9 -> 7), Ball(7 -> 8), "
        "Ball(9 -> 7), Ball(9 -> 0), Ball(7 -> 9), Ball(11 -> 7), Ball(7 -> 9), Ball(11 -> 7), "
        "Ball(7 -> 9), Ball(11 -> 7), Ball(7 -> 9), Ball(11 -> 6)]"
    )
