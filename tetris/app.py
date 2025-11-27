from typing import List
from .logic import parse_field_from_lines, field_to_lines, drop_piece, drop_piece_with_steps, InvalidInputError
from .io_layer import Reader, Writer

def run(reader: Reader, writer: Writer, print_steps: bool) -> int:
    try:
        lines: List[str] = reader.read_all()
        field = parse_field_from_lines(lines)
        if print_steps:
            steps = drop_piece_with_steps(field)
            for i, step in enumerate(steps):
                writer.write_lines([f"STEP {i}"])
                writer.write_lines(field_to_lines(step))
            return 0
        else:
            new_field = drop_piece(field)
            output_lines = field_to_lines(new_field)
            writer.write_lines(output_lines)
            return 0
    except InvalidInputError as e:
        writer.write_lines([f"Error: {str(e)}"])
        return 1