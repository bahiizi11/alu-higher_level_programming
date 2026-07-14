# python-more_classes

This project goes deeper into Object-Oriented Programming in Python:
properties, magic/dunder methods (`__str__`, `__repr__`, `__del__`),
class attributes, static methods, and class methods — all built
incrementally through a `Rectangle` class.

## Learning Objectives

- Properties with type/value validation
- `__str__` vs `__repr__` and how `eval(repr(obj))` can rebuild an object
- `__del__` for cleanup/instance-deletion hooks
- Class attributes shared across instances (`number_of_instances`,
  `print_symbol`)
- `@staticmethod` and `@classmethod`

## Files

| File | Description |
|------|-------------|
| `0-rectangle.py` | Empty class `Rectangle` |
| `1-rectangle.py` | `Rectangle` with `width`/`height` properties |
| `2-rectangle.py` | `Rectangle` with `area()` and `perimeter()` |
| `3-rectangle.py` | `Rectangle` with `__str__` |
| `4-rectangle.py` | `Rectangle` with an eval-able `__repr__` |
| `5-rectangle.py` | `Rectangle` with `__del__` |
| `6-rectangle.py` | `Rectangle` with `number_of_instances` |
| `7-rectangle.py` | `Rectangle` with `print_symbol` |
| `8-rectangle.py` | `Rectangle` with `bigger_or_equal()` |
| `9-rectangle.py` | `Rectangle` with `square()` class method |

## Author

bahiizi11
