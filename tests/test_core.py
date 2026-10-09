import tempfile, unittest
from pathlib import Path
from filetidy import make_plan, organize, undo, category
class Tests(unittest.TestCase):
    def test_categories(self):
        self.assertEqual(category("photo.JPG"),"Images")
        self.assertEqual(category("archive.abc"),"Other")
    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/"a.mp3").write_bytes(b"A");(p/"a.jpg").write_bytes(b"B")
            self.assertEqual(organize(p,make_plan(p)),2)
            self.assertTrue((p/"Audio"/"a.mp3").exists())
            self.assertEqual(undo(p),2)
            self.assertTrue((p/"a.mp3").exists())
