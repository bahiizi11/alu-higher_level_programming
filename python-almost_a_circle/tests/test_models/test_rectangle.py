#!/usr/bin/python3
"""Unittest module for the Rectangle class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_is_base(self):
        """Test that Rectangle is a subclass of Base."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)

    def test_two_args(self):
        """Test instantiation with only width and height."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, r1.id + 1)

    def test_width_height(self):
        """Test that width and height are correctly assigned."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_all_args(self):
        """Test instantiation with all arguments given."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_no_args(self):
        """Test that instantiation without args raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle()


class TestRectangle_validation(unittest.TestCase):
    """Unittests for testing attribute validation of Rectangle."""

    def test_width_not_int(self):
        """Test that a non-integer width raises TypeError."""
        with self.assertRaisesRegex(
                TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_height_not_int(self):
        """Test that a non-integer height raises TypeError."""
        with self.assertRaisesRegex(
                TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_x_not_int(self):
        """Test that a non-integer x raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_y_not_int(self):
        """Test that a non-integer y raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, {})

    def test_width_zero(self):
        """Test that a width of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        """Test that a negative width raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_height_zero(self):
        """Test that a height of 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_height_negative(self):
        """Test that a negative height raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -1)

    def test_x_negative(self):
        """Test that a negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)

    def test_y_negative(self):
        """Test that a negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -1)

    def test_width_setter(self):
        """Test width setter validation after instantiation."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_x_setter(self):
        """Test x setter validation after instantiation."""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.x = {}


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of Rectangle."""

    def test_area_1(self):
        """Test area calculation for a simple rectangle."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_2(self):
        """Test area calculation for another rectangle."""
        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)

    def test_area_with_id(self):
        """Test area calculation when id is also set."""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_area_no_args(self):
        """Test that area() raises TypeError with extra arguments."""
        r = Rectangle(2, 2)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_display(unittest.TestCase):
    """Unittests for testing the display method of Rectangle."""

    def test_display_basic(self):
        """Test display output without x/y offset."""
        r = Rectangle(4, 6)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        expected = "####\n" * 6
        self.assertEqual(captured.getvalue(), expected)

    def test_display_with_offset(self):
        """Test display output with x and y offsets."""
        r = Rectangle(3, 2, 1, 0)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        expected = " ###\n ###\n"
        self.assertEqual(captured.getvalue(), expected)

    def test_display_with_y_offset(self):
        """Test display output with a y offset produces blank lines."""
        r = Rectangle(2, 3, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        expected = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(captured.getvalue(), expected)


class TestRectangle_str(unittest.TestCase):
    """Unittests for testing the __str__ method of Rectangle."""

    def test_str(self):
        """Test the string representation with id and offsets."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default_id(self):
        """Test the string representation with an auto-assigned id."""
        r = Rectangle(5, 5, 1)
        self.assertEqual(
            str(r), "[Rectangle] ({}) 1/0 - 5/5".format(r.id))


class TestRectangle_update(unittest.TestCase):
    """Unittests for testing the update method of Rectangle."""

    def test_update_args_id(self):
        """Test updating id via args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_args_all(self):
        """Test updating all attributes via args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(
            str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test updating attributes via kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(
            str(r), "[Rectangle] (1) 1/3 - 4/2")

    def test_update_no_args(self):
        """Test that update with no arguments changes nothing."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_args_priority_over_kwargs(self):
        """Test that args take priority over kwargs when both given."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(2, width=99)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 10)


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing the to_dictionary method of Rectangle."""

    def test_to_dictionary_keys(self):
        """Test that the dictionary has the correct keys."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(
            set(d.keys()), {"id", "width", "height", "x", "y"})

    def test_to_dictionary_values(self):
        """Test that the dictionary has the correct values."""
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertEqual(
            d, {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_type(self):
        """Test that to_dictionary returns a dict."""
        r = Rectangle(10, 2)
        self.assertEqual(type(r.to_dictionary()), dict)

    def test_to_dictionary_update_roundtrip(self):
        """Test that update(**to_dictionary()) reproduces the object."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
