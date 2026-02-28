"""Tests for Brave Search script."""

from unittest.mock import MagicMock, patch

import pytest


class TestBraveSearch:
    """Test cases for Brave Search functionality."""

    @patch("agent_web_search.brave_search.parse_arguments")
    @patch("agent_web_search.brave_search.brave_search")
    def test_main_calls_brave_search(self, mock_brave_search, mock_parse):
        """Test that main() calls brave_search with correct arguments."""
        mock_parse.return_value = MagicMock(query=["test", "query"], num_results=10, json=False)

        from agent_web_search.brave_search import main

        main()

        mock_brave_search.assert_called_once_with("test query", 10, json_output=False)

    @patch("agent_web_search.brave_search.parse_arguments")
    @patch("agent_web_search.brave_search.brave_search")
    def test_main_with_json_output(self, mock_brave_search, mock_parse):
        """Test that main() calls brave_search with json_output=True."""
        mock_parse.return_value = MagicMock(query=["test", "query"], num_results=5, json=True)

        from agent_web_search.brave_search import main

        main()

        mock_brave_search.assert_called_once_with("test query", 5, json_output=True)

    @patch("agent_web_search.brave_search.os.environ")
    def test_get_brave_api_key_success(self, mock_environ):
        """Test getting API key from environment variable."""
        mock_environ.get.return_value = "test-api-key"

        from agent_web_search.brave_search import get_brave_api_key

        result = get_brave_api_key()
        assert result == "test-api-key"

    @patch("agent_web_search.brave_search.os")
    def test_get_brave_api_key_missing(self, mock_os):
        """Test that missing API key causes exit."""
        mock_os.environ.get.return_value = None

        from agent_web_search.brave_search import get_brave_api_key

        with pytest.raises(SystemExit) as exc_info:
            get_brave_api_key()

        assert exc_info.value.code == 1

    def test_parse_arguments_validation(self):
        """Test argument parsing validation."""
        from agent_web_search.brave_search import parse_arguments

        # Test valid arguments
        with patch("sys.argv", ["brave-search", "test", "-n", "5"]):
            args = parse_arguments()
            assert args.num_results == 5
            assert args.query == ["test"]

        # Test invalid num_results (too low)
        with patch("sys.argv", ["brave-search", "test", "-n", "0"]):
            with pytest.raises(SystemExit):
                parse_arguments()

        # Test invalid num_results (too high)
        with patch("sys.argv", ["brave-search", "test", "-n", "101"]):
            with pytest.raises(SystemExit):
                parse_arguments()

    @patch("agent_web_search.brave_search.requests.get")
    @patch("agent_web_search.brave_search.get_brave_api_key")
    def test_brave_search_api_call(self, mock_get_key, mock_get):
        """Test that brave_search makes correct API call."""
        mock_get_key.return_value = "test-key"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "web": {
                "results": [
                    {
                        "title": "Test Result",
                        "url": "https://example.com",
                        "description": "Test description",
                    }
                ]
            }
        }
        mock_get.return_value = mock_response

        from agent_web_search.brave_search import brave_search

        brave_search("test query", 5, json_output=False)

        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert call_args[1]["params"]["q"] == "test query"
        assert call_args[1]["params"]["count"] == 5


class TestBraveSearchIntegration:
    """Integration tests for Brave Search."""

    @pytest.mark.integration
    def test_brave_search_with_real_api(self):
        """Test Brave Search with real API (requires BRAVE_API_KEY)."""
        # Skip if no API key
        import os

        if not os.environ.get("BRAVE_API_KEY"):
            pytest.skip("BRAVE_API_KEY not set")

        from agent_web_search.brave_search import brave_search

        # This will make a real API call
        brave_search("python programming", 3, json_output=True)
