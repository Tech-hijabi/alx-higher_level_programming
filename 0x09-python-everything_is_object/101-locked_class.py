#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Using __slots__ to restrict attribute creation.
    Only 'first_name' is allowed as a new instance attribute.
    """

    __slots__ = ["first_name"]
