"""Trivial version test."""

import unittest

from {{cookiecutter.package_name}}.version import get_version


class TestVersion(unittest.TestCase):
    """Trivially test a version."""

    def test_version_type(self) -> None:
        """Test the version is a string.

        This is only meant to be an example test.
        """
        version = get_version()
        self.assertIsInstance(version, str)
