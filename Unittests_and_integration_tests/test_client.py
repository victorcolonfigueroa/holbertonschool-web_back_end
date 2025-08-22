#!/usr/bin/env python3
"""Unit tests for `client.GithubOrgClient`.

Focus: verify that `GithubOrgClient.org` returns the mocked payload and
calls `client.get_json` exactly once with the expected URL.
"""

from typing import Any, Dict
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, patch, PropertyMock
from fixtures import TEST_PAYLOAD

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for `client.GithubOrgClient`."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """It returns payload and calls get_json once with the correct URL."""
        expected: Dict[str, Any] = {"org": org_name}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self) -> None:
        """It returns repos_url derived from the mocked `org` property."""
        expected_repos_url = "https://api.github.com/orgs/google/repos"
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": expected_repos_url}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, expected_repos_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """It returns the list of repo names from the mocked payload."""
        payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = payload

        repos_url = "https://api.github.com/orgs/google/repos"
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_url:
            mock_url.return_value = repos_url
            client = GithubOrgClient("google")
            self.assertEqual(
                client.public_repos(), ["repo1", "repo2", "repo3"]
            )

            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Any],
                         license_key: str, expected: bool) -> None:
        """It returns True only when repo's license key matches."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected
        )


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
    for (
        org_payload,
        repos_payload,
        expected_repos,
        apache2_repos,
    ) in TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for `GithubOrgClient.public_repos`.

    Only external HTTP calls are mocked (requests.get). Internal helpers like
    `get_json` and memoized properties are exercised as in production.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """Start patcher for requests.get and set side effects.

        It returns `org_payload` for the org URL and `repos_payload` for the
        repos URL present in the org payload.
        """
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def _json_side_effect(url: str, *args: Any, **kwargs: Any) -> Mock:
            resp = Mock()
            if url == "https://api.github.com/orgs/google":
                resp.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                resp.json.return_value = cls.repos_payload
            else:
                raise ValueError(f"Unexpected URL: {url}")
            return resp

        cls.mock_get.side_effect = _json_side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop the requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """It returns all repo names from the fixture payload."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """It filters repo names by Apache 2.0 license using fixtures."""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"), self.apache2_repos
        )