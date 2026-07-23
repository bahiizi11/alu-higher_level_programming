#!/usr/bin/python3
"""Unittest module for the Square class."""
import unittest
import io
import os
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_rectangle(self):
        """Test that Square is a subclass of Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_is_base(self):
        """Test that Square is a subclass of Base."""
        s = Square(5)
        self.assertIsInstance(s, Base)

    def test_size_only(self):
        """Test instantiation with only size given."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_size_x(self):
        """Test instantiation with size and x given."""
        s = Square(2, 2)
        self.assertEqual(s.width, 2)
        self.assertEqual(s.height, 2)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 0)

    def test_size_x_y(self):
        """Test instantiation with size, x, and y given."""
        s = Square(3, 1, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_no_new_attributes(self):
        """Test that Square doesn't add new attributes."""
        s = Square(5)
        self.assertFalse(hasattr(s, "size_"))

    def test_no_args(self):
        """Test that instantiation without args raises TypeError."""
        with self.assertRaises(TypeError):
            Square()

    def test_id(self):
        """Test that id auto-increments as with other Base subclasses."""
        s1 = Square(5)
        s2 = Square(5)
        self.assertEqual(s2.id, s1.id + 1)


class TestSquare_validation(unittest.TestCase):
    """Unittests for testing validation of Square attributes."""

    def test_size_not_int(self):
        """Test that a non-integer size raises TypeError."""
        with self.assertRaisesRegex(
                TypeError, "width must be an integer"):
            Square("5")

    def test_size_negative(self):
        """Test that a negative size raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_size_zero(self):
        """Test that a size of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_negative(self):
        """Test that a negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)

    def test_x_not_int(self):
        """Test that a non-integer x raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_y_negative(self):
        """Test that a negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 0, -1)

    def test_y_not_int(self):
        """Test that a non-integer y raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")


class TestSquare_size(unittest.TestCase):
    """Unittests for testing the size getter/setter of Square."""

    def test_size_getter(self):
        """Test that the size getter returns the width."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test that the size setter updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.size, 10)

    def test_size_setter_invalid_type(self):
        """Test that setting size to a non-integer raises TypeError."""
        s = Square(5)
        with self.assertRaisesRegex(
                TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_setter_invalid_value(self):
        """Test that setting size to <= 0 raises ValueError."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0


class TestSquare_str(unittest.TestCase):
    """Unittests for testing the __str__ method of Square."""

    def test_str(self):
        """Test the string representation of a Square."""
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_str_with_offset(self):
        """Test the string representation with x and y offsets."""
        s = Square(2, 2, 0, 2)
        self.assertEqual(str(s), "[Square] (2) 2/0 - 2")


class TestSquare_display(unittest.TestCase):
    """Unittests for testing the display method of Square."""

    def test_display(self):
        """Test the display output of a Square."""
        s = Square(2)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_offset(self):
        """Test the display output of a Square with x/y offset."""
        s = Square(2, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n  ##\n  ##\n")


class TestSquare_update(unittest.TestCase):
    """Unittests for testing the update method of Square."""

    def test_update_args_id(self):
        """Test updating id via args."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_args_all(self):
        """Test updating all attributes via args."""
        s = Square(5, 0, 0, 1)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Test updating attributes via kwargs."""
        s = Square(5, 0, 0, 1)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_update_no_args(self):
        """Test that update with no arguments changes nothing."""
        s = Square(5, 0, 0, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")


class TestSquare_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of the Square class."""

    def tearDown(self):
        """Remove created files after each test."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file_none(self):
        """Test that save_to_file(None) saves an empty list."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test that save_to_file([]) saves an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing the to_dictionary method of Square."""

    def test_to_dictionary_keys(self):
        """Test that the dictionary has the correct keys."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(set(d.keys()), {"id", "size", "x", "y"})

    def test_to_dictionary_values(self):
        """Test that the dictionary has the correct values."""
        s = Square(10, 2, 1, 5)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 5, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_update_roundtrip(self):
        """Test that update(**to_dictionary()) reproduces the object."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
