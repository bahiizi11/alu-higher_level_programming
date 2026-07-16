# python-inheritance

This project covers class inheritance in Python: introspection with
`dir()`, inheriting from built-in types, checking class relationships
(`type()` vs. `isinstance()`), and building a small geometry hierarchy
(`BaseGeometry` → `Rectangle` → `Square`).

## Learning Objectives

- Why Python programming is awesome
- How to list all attributes/methods of a class or instance
- First-class everything, and inheriting from `list`
- The difference between `type(obj) is a_class`, `isinstance()`, and
  strict subclass inheritance
- Building a small validated class hierarchy with `super()`
- Name mangling and how private attributes behave in subclasses

## Files

| File | Description |
|------|-------------|
| `0-lookup.py` | Lists available attributes and methods of an object |
| `1-my_list.py` | `MyList`, a `list` subclass with `print_sorted()` |
| `2-is_same_class.py` | Checks exact class membership |
| `3-is_kind_of_class.py` | Checks class or subclass membership |
| `4-inherits_from.py` | Checks strict (non-exact) inheritance |
| `5-base_geometry.py` | Empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry` with an unimplemented `area()` |
| `7-base_geometry.py` | `BaseGeometry` with `integer_validator()` |
| `8-rectangle.py` | `Rectangle` inheriting from `BaseGeometry` |
| `9-rectangle.py` | Full `Rectangle` with `area()` and `__str__` |
| `10-square.py` | `Square` inheriting from `Rectangle` |
| `11-square.py` | `Square` with its own `__str__` |

## Author

bahiizi11
