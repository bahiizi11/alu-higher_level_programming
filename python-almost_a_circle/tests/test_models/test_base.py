#!/usr/bin/python3
"""Unittest module for the Base class."""
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        """Test that id is auto-assigned when no argument is given."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_public(self):
        """Test that id is a public attribute."""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_id_none(self):
        """Test that id auto-increments when None is passed."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b2.id, b1.id + 1)

    def test_two_args(self):
        """Test that Base raises TypeError with too many arguments."""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of the Base class."""

    def test_list_dict(self):
        """Test conversion of a list of dictionaries."""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(json.loads(json_dictionary), [dictionary])

    def test_empty_list(self):
        """Test conversion of an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_none(self):
        """Test conversion of None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_return_type(self):
        """Test that the return type is a string."""
        self.assertEqual(type(Base.to_json_string([])), str)

    def test_multiple_dicts(self):
        """Test conversion of multiple dictionaries."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json.loads(json_str), list_dicts)

    def test_too_many_args(self):
        """Test that too many arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of the Base class."""

    @classmethod
    def tearDownClass(cls):
        """Remove created files after all tests in this class."""
        for fname in ("Rectangle.json", "Square.json", "Base.json"):
            if os.path.exists(fname):
                os.remove(fname)

    def tearDown(self):
        """Remove created files after each test."""
        for fname in ("Rectangle.json", "Square.json", "Base.json"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_one_rectangle(self):
        """Test saving one Rectangle to a file."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_content_rectangle(self):
        """Test the content saved matches the Rectangle dictionary."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(json.loads(content), [r1.to_dictionary()])

    def test_empty_list(self):
        """Test saving an empty list of instances."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_none(self):
        """Test saving None saves an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_overwrite(self):
        """Test that save_to_file overwrites an existing file."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(content, [r2.to_dictionary()])

    def test_square(self):
        """Test saving Square instances to Square.json."""
        s1 = Square(5)
        Square.save_to_file([s1])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(json.loads(content), [s1.to_dictionary()])


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of the Base class."""

    def test_none(self):
        """Test conversion of None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """Test conversion of an empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_string(self):
        """Test conversion of a valid JSON string."""
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_str = Base.to_json_string(list_input)
        self.assertEqual(Base.from_json_string(json_str), list_input)

    def test_return_type(self):
        """Test that the return type is a list."""
        self.assertEqual(type(Base.from_json_string("[]")), list)

    def test_too_many_args(self):
        """Test that too many arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Base.from_json_string("[]", "[]")


class TestBase_create(unittest.TestCase):
    """Unittests for testing the create method of the Base class."""

    def test_create_rectangle(self):
        """Test creating a Rectangle instance from a dictionary."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test creating a Square instance from a dictionary."""
        s1 = Square(5, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_create_returns_correct_type(self):
        """Test that create returns an instance of the correct class."""
        s1 = Square(5)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsInstance(s2, Square)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing the load_from_file method of Base."""

    def tearDown(self):
        """Remove created files after each test."""
        for fname in ("Rectangle.json", "Square.json"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_no_file(self):
        """Test that a missing file returns an empty list."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rectangle_round_trip(self):
        """Test that saved and loaded Rectangles match."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_output = Rectangle.load_from_file()
        self.assertEqual(len(list_output), 2)
        self.assertEqual(str(list_output[0]), str(r1))
        self.assertEqual(str(list_output[1]), str(r2))

    def test_square_round_trip(self):
        """Test that saved and loaded Squares match."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        list_output = Square.load_from_file()
        self.assertEqual(len(list_output), 2)
        self.assertIsInstance(list_output[0], Square)
        self.assertEqual(str(list_output[0]), str(s1))
        self.assertEqual(str(list_output[1]), str(s2))

    def test_load_returns_list(self):
        """Test that load_from_file returns a list type."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        self.assertEqual(type(Rectangle.load_from_file()), list)


if __name__ == "__main__":
    unittest.main()
