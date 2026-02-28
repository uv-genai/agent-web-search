# Quick Start Guide

## Installation

```bash
# Navigate to project directory
cd /Users/ugo/tmp/ws

# Install dependencies (creates virtual environment)
uv sync
```

## Setup API Keys

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API keys
# Get Brave Search API key: https://api-dashboard.search.brave.com/
# Get Linkup API key: https://app.linkup.so/
```

Or set environment variables directly:

```bash
export BRAVE_API_KEY="your-brave-api-key-here"
export LINKUP_API_KEY="your-linkup-api-key-here"
```

## Usage

### Brave Search

```bash
# Basic search
uv run brave-search "python programming" -n 5

# JSON output
uv run brave-search "machine learning" --json

# With specific count
uv run brave-search "web development" -n 10 --json
```

### Linkup Search

```bash
# Basic search
uv run linkup-search search "open source licenses" -n 5

# Deep research
uv run linkup-search search "AI trends 2026" --depth deep -n 10

# JSON output
uv run linkup-search search "python tutorials" -n 5 --json

# Fetch webpage content
uv run linkup-search fetch "https://docs.python.org"

# With filters
uv run linkup-search search "machine learning" \
  --from-date 2026-01-01 \
  --include-domains arxiv.org \
  -n 10
```

## Development

```bash
# Run tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/agent_web_search --cov-report=term-missing

# Format code
uv run ruff format src tests

# Check code quality
uv run ruff check src tests

# Type checking
uv run mypy src
```

## Project Structure

```
ws/
├── pyproject.toml              # Project configuration
├── README.md                   # Main documentation
├── CHANGELOG.md                # Version history
├── QUICKSTART.md               # This file
├── src/
│   └── agent_web_search/
│       ├── __init__.py
│       ├── brave_search.py     # Brave Search CLI tool
│       └── linkup_search.py    # Linkup Search CLI tool
├── tests/
│   ├── __init__.py
│   ├── test_brave_search.py
│   └── test_linkup_search.py
└── .env.example                # Environment template
```

## CLI Help

```bash
# Brave Search help
uv run brave-search --help

# Linkup Search help
uv run linkup-search --help

# Linkup Search subcommands
uv run linkup-search search --help
uv run linkup-search fetch --help
```

## Next Steps

1. **Get API Keys**: Sign up for Brave Search and Linkup API keys
2. **Test the Tools**: Run sample searches to verify everything works
3. **Explore Features**: Try different options and output formats
4. **Read Documentation**: Check README.md for detailed information
5. **Contribute**: See CONTRIBUTING.md (if exists) for contribution guidelines

---

*For more details, see [README.md](README.md)*