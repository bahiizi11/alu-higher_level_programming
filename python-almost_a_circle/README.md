# python-almost_a_circle

This project builds an OOP class hierarchy in Python: a `Base` class
that manages object `id`s and JSON serialization/deserialization, a
`Rectangle` class with fully validated private attributes (getters
and setters), and a `Square` class that inherits from `Rectangle`.
The project also covers unit testing every class and method with
`unittest`, and keeping all code PEP 8 compliant.

## Learning Objectives

- Object-oriented programming: inheritance, private attributes
- `property`, getters and setters
- Args and kwargs (`*args`, `**kwargs`)
- Serializing and deserializing a Python object to/from JSON
- Reading and writing files in Python
- Unit testing with `unittest`, including `unittest.mock` techniques
  like capturing stdout

## Files

| File | Description |
|------|-------------|
| `models/base.py` | `Base` class: id management, `to_json_string`, `save_to_file`, `from_json_string`, `create`, `load_from_file` |
| `models/rectangle.py` | `Rectangle` class: validated `width`/`height`/`x`/`y`, `area`, `display`, `__str__`, `update`, `to_dictionary` |
| `models/square.py` | `Square` class (inherits `Rectangle`): `size` property, `__str__`, `update`, `to_dictionary` |
| `tests/test_models/test_base.py` | Unit tests for `Base` |
| `tests/test_models/test_rectangle.py` | Unit tests for `Rectangle` |
| `tests/test_models/test_square.py` | Unit tests for `Square` |

## Usage
## Author

bahiizi11
