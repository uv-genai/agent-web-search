"""Tests for Linkup Search script."""

from unittest.mock import MagicMock, patch

import pytest


class TestLinkupSearch:
    """Test cases for Linkup Search functionality."""

    @patch("agent_web_search.linkup_search.parse_arguments")
    @patch("agent_web_search.linkup_search.linkup_search")
    @patch("agent_web_search.linkup_search.linkup_fetch")
    def test_main_calls_linkup_search(self, mock_fetch, mock_search, mock_parse):
        """Test that main() calls linkup_search with correct arguments."""
        mock_parse.return_value = MagicMock(
            mode="search",
            query=["test", "query"],
            num_results=10,
            depth="standard",
            output_type="searchResults",
            from_date=None,
            to_date=None,
            include_domains=None,
            exclude_domains=None,
            json=False,
        )

        from agent_web_search.linkup_search import main

        main()

        mock_search.assert_called_once()

    @patch("agent_web_search.linkup_search.parse_arguments")
    @patch("agent_web_search.linkup_search.linkup_search")
    @patch("agent_web_search.linkup_search.linkup_fetch")
    def test_main_calls_linkup_fetch(self, mock_fetch, mock_search, mock_parse):
        """Test that main() calls linkup_fetch for fetch mode."""
        mock_parse.return_value = MagicMock(
            mode="fetch",
            url="https://example.com",
            output_format="markdown",
            render_js=False,
            json=False,
        )

        from agent_web_search.linkup_search import main

        main()

        mock_fetch.assert_called_once()

    @patch("agent_web_search.linkup_search.os.environ")
    def test_get_linkup_api_key_success(self, mock_environ):
        """Test getting API key from environment variable."""
        mock_environ.get.return_value = "test-api-key"

        from agent_web_search.linkup_search import get_linkup_api_key

        result = get_linkup_api_key()
        assert result == "test-api-key"

    @patch("agent_web_search.linkup_search.os")
    def test_get_linkup_api_key_missing(self, mock_os):
        """Test that missing API key causes exit."""
        mock_os.environ.get.return_value = None

        from agent_web_search.linkup_search import get_linkup_api_key

        with pytest.raises(SystemExit) as exc_info:
            get_linkup_api_key()

        assert exc_info.value.code == 1

    def test_parse_arguments_search_mode(self):
        """Test argument parsing for search mode."""
        from agent_web_search.linkup_search import parse_arguments

        with patch("sys.argv", ["linkup-search", "search", "test", "query", "-n", "5"]):
            args = parse_arguments()
            assert args.mode == "search"
            assert args.num_results == 5
            assert args.query == ["test", "query"]

    def test_parse_arguments_fetch_mode(self):
        """Test argument parsing for fetch mode."""
        from agent_web_search.linkup_search import parse_arguments

        with patch("sys.argv", ["linkup-search", "fetch", "https://example.com"]):
            args = parse_arguments()
            assert args.mode == "fetch"
            assert args.url == "https://example.com"

    def test_parse_arguments_missing_mode(self):
        """Test that missing mode causes error."""
        from agent_web_search.linkup_search import parse_arguments

        with patch("sys.argv", ["linkup-search"]):
            with pytest.raises(SystemExit):
                parse_arguments()

    def test_parse_arguments_date_validation(self):
        """Test date format validation."""
        from agent_web_search.linkup_search import parse_arguments

        # Valid date format
        with patch("sys.argv", ["linkup-search", "search", "test", "--from-date", "2024-01-01"]):
            args = parse_arguments()
            assert args.from_date == "2024-01-01"

        # Invalid date format
        with patch("sys.argv", ["linkup-search", "search", "test", "--from-date", "01-01-2024"]):
            with pytest.raises(SystemExit):
                parse_arguments()

    @patch("agent_web_search.linkup_search.requests.post")
    @patch("agent_web_search.linkup_search.get_linkup_api_key")
    def test_linkup_search_api_call(self, mock_get_key, mock_post):
        """Test that linkup_search makes correct API call."""
        mock_get_key.return_value = "test-key"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "results": [
                {"name": "Test Result", "url": "https://example.com", "content": "Test content"}
            ]
        }
        mock_post.return_value = mock_response

        from agent_web_search.linkup_search import linkup_search

        linkup_search("test query", 5, json_output=False)

        mock_post.assert_called_once()
        call_data = mock_post.call_args[1]["json"]
        assert call_data["q"] == "test query"
        assert call_data["maxResults"] == 5


class TestLinkupSearchIntegration:
    """Integration tests for Linkup Search."""

    @pytest.mark.integration
    def test_linkup_search_with_real_api(self):
        """Test Linkup Search with real API (requires LINKUP_API_KEY)."""
        # Skip if no API key
        import os

        if not os.environ.get("LINKUP_API_KEY"):
            pytest.skip("LINKUP_API_KEY not set")

        from agent_web_search.linkup_search import linkup_search

        # This will make a real API call
        linkup_search("python programming", 3, json_output=True)
