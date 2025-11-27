from unittest.mock import Mock
from tetris.app import run

def test_run_success():
    reader = Mock()
    writer = Mock()
    reader.read_all.return_value = [
        "5 6\n",
        "..p...\n",
        "##p.##\n",
        "##pp##\n",
        "##..##\n",
        "##..##\n",
        ]
    code = run(reader, writer, print_steps = False)
    assert code == 0
    writer.write_lines.assert_called_once()
    args = writer.write_lines.call_args[0][0]
    assert args == [
        "......",
        "##..##",
        "##p.##",
        "##p.##",
        "##pp##",
        ]
    
def test_run_invalid_input():
    reader = Mock()
    writer = Mock()
    reader.read_all.return_value = [
        "2 2\n",
        "##\n",
        "..\n",
        ]
    code = run(reader, writer, print_steps = False)
    assert code == 1
    writer.write_lines.assert_called_once_with(["Error: No piece points found in the input"])

def test_run_all_steps():
    reader = Mock()
    writer = Mock()
    reader.read_all.return_value = [
        "3 3\n",
        "..p\n",
        "...\n",
        "..#\n",  
    ]
    code = run(reader, writer, print_steps = True)
    assert code == 0
    calls = writer.write_lines.call_args_list
    assert calls[0][0][0] == ["STEP 0"]
    assert calls[1][0][0] == ["..p", "...", "..#"]
    assert calls[2][0][0] == ["STEP 1"]
    assert calls[3][0][0] == ["...", "..p", "..#"]

def test_run_invalid_input_with_steps():
    reader = Mock()
    writer = Mock()
    reader.read_all.return_value = [
        "2 2\n",
        "##\n",
        "..\n",
        ]
    code = run(reader, writer, print_steps = True)
    assert code == 1
    writer.write_lines.assert_called_once_with(["Error: No piece points found in the input"])
