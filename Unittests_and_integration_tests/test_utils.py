#!/usr/bin/env python3
"""Unit tests for utilities in `utils.py`.

This module currently tests `utils.access_nested_map` to ensure it returns
expected values for valid nested paths.
"""

from typing import Any, Mapping, Sequence
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for `utils.access_nested_map`."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping[str, Any],
        path: Sequence[str],
        expected: Any,
    ) -> None:
        """It returns the value at `path` inside `nested_map`."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping[str, Any],
        path: Sequence[str],
        missing_key: str,
    ) -> None:
        """It raises KeyError and the message contains the missing key."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], missing_key)


class TestGetJson(unittest.TestCase):
    """Tests for `utils.get_json` that avoid real HTTP calls."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """It returns payload from the mocked requests.get().json()."""
        with patch("utils.requests.get") as mock_get:
            mock_resp: Mock = Mock()
            mock_resp.json.return_value = test_payload
            mock_get.return_value = mock_resp

            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests for `utils.memoize` decorator caching behavior."""

    def test_memoize(self) -> None:
        """It calls the underlying method only once and caches the value."""

        class TestClass:
            """Helper class exposing a memoized property for testing."""

            def a_method(self) -> int:
                """Return a constant used to verify memoization."""
                return 42

            @memoize
            def a_property(self) -> int:
                """Return value from `a_method`, but memoized as a property."""
                return self.a_method()

        with patch.object(
            TestClass, "a_method", return_value=42
        ) as mock_method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_method.assert_called_once()