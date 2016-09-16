#!/usr/bin/env python3

from load_into_database import convert, bool_yes_no
import pytest

# Test the convert function
def test_convert():
    convert_vals = (
        # Pass through
        ("9", None, None, "9"),
        ("a", None, None, "a"),
        ("1.", None, None, "1."),
        # Standard dtypes
        ("9", int, None, 9),
        ("a", str, None, "a"),
        ("1", float, None, 1.),
        # With spaces
        ("9 ", int, None, 9),
        ("a ", str, None, "a"),
        ("1 ", float, None, 1.),
        (" 9", int, None, 9),
        (" a", str, None, "a"),
        (" 1", float, None, 1.),
        # Nulls that do nothing
        ("9", int, [""], 9),
        ("a", str, [""], "a"),
        ("1", float, [""], 1.),
        # Nulls that return None
        ("9", int, ["9"], None),
        ("a", str, ["a"], None),
        ("1.", float, ["1."], None),
        ("9", None, ["9"], None),
        ("a", None, ["a"], None),
        ("1.", None, ["1."], None),
        # Conversion failure
        ("a", int, None, None),
    )
    for val, dtype, nulls, res in convert_vals:
        assert convert(val, dtype, nulls) == res


# Test the bool_yes_no function
def test_bools():
    bools = (
        ("Y", True),
        ("y", True),
        ("N", False),
        ("n", False),
    )
    for val, res in bools:
        assert bool_yes_no(val) == res

def test_nulls():
    nones = (
        ("Y", ["Y"]),
        ("y", ["y"]),
        ("N", ["N"]),
        ("n", ["n"]),
        ("", [""]),
        ("1", ["1"]),
    )
    for val, nulls in nones:
        assert bool_yes_no(val, nulls) is None
