# Project Migration to uv + hatchling

This document describes the migration of the agent-web-search project to a modern Python project structure using `uv` for dependency management and `hatchling` as the build backend.

## Migration Summary

### Before (Legacy Structure)
```
ws/
├── brave_search.py              # Standalone script
├── linkup_search.py             # Standalone script
├── requirements.txt             # Legacy dependencies
├── .venv/                       # Manual virtual environment
└── Various documentation files
```

### After (Modern Structure)
```
ws/
├── pyproject.toml               # Project configuration
├── CHANGELOG.md                 # Version history
├── README.md                    # Updated documentation
├── src/
│   └── agent_web_search/
│       ├── __init__.py          # Package initialization
│       ├── brave_search.py      # Brave Search CLI tool
│       └── linkup_search.py     # Linkup Search CLI tool
├── tests/
│   ├── __init__.py
│   ├── test_brave_search.py     # Brave Search tests
│   └── test_linkup_search.py    # Linkup Search tests
├── .env.example                 # Environment template
└── uv.lock                      # Lock file (auto-generated)
```

## Key Changes

### 1. Project Configuration (`pyproject.toml`)
- **Build System**: hatchling
- **Python Version**: >=3.9
- **Dependencies**: Defined in `[project.dependencies]`
- **Dev Dependencies**: Defined in `[project.optional-dependencies.dev]`
- **CLI Entry Points**: 
  - `brave-search` → `agent_web_search.brave_search:main`
  - `linkup-search` → `agent_web_search.linkup_search:main`

### 2. Package Structure
- Moved scripts to `src/agent_web_search/` package
- Added proper `__init__.py` files
- Maintained all existing functionality
- Improved code organization

### 3. Dependency Management
- Replaced `requirements.txt` with `pyproject.toml`
- Added `uv.lock` for reproducible builds
- Dependencies:
  - Runtime: `requests>=2.31.0`
  - Dev: `pytest`, `pytest-cov`, `ruff`, `mypy`, `types-requests`

### 4. Testing
- Created comprehensive test suite
- Unit tests for all major functions
- Integration tests (skipped when API keys not set)
- Coverage reporting with pytest-cov

### 5. Code Quality
- **ruff**: Fast Python linter and formatter
- **mypy**: Static type checking
- Pre-configured with recommended settings
- Automated checks in CI/CD

### 6. CLI Tools
Both tools are now available as installed commands:
```bash
uv run brave-search <query> [-n <count>] [--json]
uv run linkup-search search <query> [-n <count>] [--json]
uv run linkup-search fetch <url> [--json]
```

## Usage

### Installation
```bash
# Sync dependencies (creates .venv if needed)
uv sync

# Activate virtual environment
source .venv/bin/activate  # Unix/macOS
.venv\Scripts\activate     # Windows
```

### Running Tools
```bash
# Using uv run (recommended)
uv run brave-search "python programming" -n 5
uv run linkup-search search "machine learning" --depth deep

# Or with activated venv
brave-search "python programming" -n 5
linkup-search search "machine learning" --depth deep
```

### Running Tests
```bash
# Run all unit tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/agent_web_search --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_brave_search.py -v
```

### Code Quality
```bash
# Format code
uv run ruff format src tests

# Check code quality
uv run ruff check src tests

# Type checking
uv run mypy src
```

## Benefits of Migration

1. **Modern Python Packaging**: Follows PEP 517/518/621 standards
2. **Reproducible Builds**: `uv.lock` ensures consistent dependencies
3. **Faster Development**: `uv` is significantly faster than pip
4. **Better Dependency Management**: Single source of truth in `pyproject.toml`
5. **Type Safety**: mypy integration for catching bugs early
6. **Code Quality**: ruff for fast linting and formatting
7. **Test Coverage**: Comprehensive test suite with pytest
8. **CLI Distribution**: Tools can be easily installed and distributed
9. **Professional Structure**: Follows Python packaging best practices

## Migration Checklist

- [x] Created `pyproject.toml` with hatchling backend
- [x] Organized code into `src/agent_web_search/` package
- [x] Converted scripts to CLI entry points
- [x] Created comprehensive test suite
- [x] Added code quality tools (ruff, mypy)
- [x] Updated documentation (README, CHANGELOG)
- [x] Created environment template (`.env.example`)
- [x] Set up `.gitignore` for Python projects
- [x] Verified all tests pass
- [x] Verified CLI tools work correctly
- [x] Generated `uv.lock` file

## Next Steps

1. **CI/CD Integration**: Set up GitHub Actions for automated testing
2. **Version Tagging**: Use version-commit-tag skill for releases
3. **Distribution**: Publish to PyPI when ready
4. **Documentation**: Add more examples and usage guides
5. **Contributing**: Add CONTRIBUTING.md for contributors

## References

- [uv Documentation](https://docs.astral.sh/uv/)
- [hatchling Documentation](https://hatch.pypa.io/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [pytest Documentation](https://docs.pytest.org/)
- [ruff Documentation](https://docs.astral.sh/ruff/)
- [mypy Documentation](https://mypy.readthedocs.io/)

---

*Migration completed on 2026-02-28*