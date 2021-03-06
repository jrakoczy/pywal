"""Test imagemagick functions."""
import unittest

from pywal import colors


class TestGenColors(unittest.TestCase):
    """Test the gen_colors functions."""

    def test_gen_colors_fail(self):
        """> Generate a colorscheme and fail."""
        with self.assertRaises(SystemExit):
            colors.get("tests/test_files/test.png")

    def test_color_import(self):
        """> Read colors from a file."""
        result = colors.file("tests/test_files/test_file.json")
        self.assertEqual(result["colors"]["color0"], "#1F211E")

    def test_color_import_no_wallpaper(self):
        """> Read colors from a file without a wallpaper."""
        result = colors.file("tests/test_files/test_file2.json")
        self.assertEqual(result["wallpaper"], "None")


if __name__ == "__main__":
    unittest.main()
