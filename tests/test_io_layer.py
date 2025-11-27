from tetris.io_layer import FileReader, FileWriter

def test_file_reader(tmp_path):
    p = tmp_path / "test.txt"
    p.write_text("Hello\nworld\n", encoding = "utf-8")
    reader = FileReader(str(p))
    lines = reader.read_all()
    assert lines == ["Hello\n", "world\n"]

def test_stdout_writer(capsys):
    writer = FileWriter()
    writer.write_lines(["a", "b"])
    captured = capsys.readouterr()
    assert captured.out == "a\nb\n"

