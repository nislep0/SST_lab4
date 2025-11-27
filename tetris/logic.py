from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Point:
    row: int
    col: int

@dataclass
class Field:
    height: int
    width: int
    piece: List[Point]
    landscape: List[Point]

class InvalidInputError(Exception):
    pass

def parse_field_from_lines(lines: List[str]) -> Field:
    if not lines:
        raise InvalidInputError("Input lines are empty")
    try:
        first = lines[0].strip().split()
        if len(first) != 2:
            raise InvalidInputError("First line must contain exactly two integers")
        height = int(first[0])
        width = int(first[1])
    except Exception:
        raise InvalidInputError("Invalid height and width specification")

    if len(lines) != height + 1:
        raise InvalidInputError("Number of lines does not match specified height")
    
    piece: List[Point] = []
    landscape: List[Point] = []

    for row in range(height):
        row_str = lines[row + 1].rstrip('\n')
        if len(row_str) != width:
            raise InvalidInputError(f"Line {row + 2} does not match specified width")
        for col, char in enumerate(row_str):
            if char == 'p':
                piece.append(Point(row, col))
            elif char == '#':
                landscape.append(Point(row, col))
            elif char == '.':
                continue
            else:
                raise InvalidInputError(f"Invalid character '{char}' at line {row + 2}, column {col + 1}")
    if not piece:
        raise InvalidInputError("No piece points found in the input")
    return Field(height, width, piece, landscape)

def field_to_lines(field: Field) -> List[str]:
    grid = [['.' for _ in range(field.width)] for _ in range(field.height)]
    for point in field.landscape:
        grid[point.row][point.col] = '#'

    for point in field.piece:
        if grid[point.row][point.col] == '#':
            grid[point.row][point.col] = '#'
        else: 
            grid[point.row][point.col] = 'p'

    return [''.join(row) for row in grid]

def move_piece_down_once(field: Field) -> Field:
    new_positions: List[Point] = []
    landscape_set = {(p.row, p.col) for p in field.landscape}
    for point in field.piece:
        new_row = point.row + 1
        new_col = point.col
        if new_row >= field.height or (new_row, new_col) in landscape_set:
            return field
        new_positions.append(Point(new_row, new_col))

    new_field = Field(
        height=field.height,
        width=field.width,
        piece=new_positions,
        landscape=list(field.landscape)
    )

    return new_field

def drop_piece(field: Field) -> Field:
    while True:
        new_field = move_piece_down_once(field)
        if new_field.piece == field.piece:
            return field
        field = new_field

def drop_piece_with_steps(field: Field) -> List[Field]:
    steps = [field]
    current = field
    while True:
        next_field = move_piece_down_once(current)
        if next_field.piece == current.piece:
            return steps
        steps.append(next_field)
        current = next_field
        
