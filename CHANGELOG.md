# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.2] - 2026-04-27

### Fixed
- 🐛 **Email inconsistency** — corrected `__email__` in `__init__.py` from `ugo@example.com` to `ugovaretto@gmail.com`
- 🐛 **README project structure diagram** — updated from old `ws/` layout to actual `agent-web-search/` structure

---

## [2.1.0] - 2026-04-27

### Added
- ✅ **HTML output for linkup fetch mode** — added `includeRawHtml` API parameter and response parsing to return raw HTML when `--output-format html` is specified

---

## [2.0.1] - 2026-04-27

### Fixed
- 🐛 **Linkup fetch mode returning empty content** — API response key is `"markdown"` not `"content"`; updated `linkup_fetch()` to read the correct key

---

## [2.0.0] - 2026-02-28

### Added
- ✅ **Modern Python project structure** with hatchling build backend
- ✅ **uv package manager** integration for dependency management
- ✅ **CLI tools** with proper entry points (`brave-search`, `linkup-search`)
- ✅ **Comprehensive test suite** with pytest
- ✅ **Code quality tools** (ruff, mypy)
- ✅ **Documentation** with proper README and CHANGELOG
- ✅ **Environment template** (`.env.example`)
- ✅ **Tests** for both Brave Search and Linkup Search

### Changed
- 🔄 **Reorganized codebase** into proper package structure (`src/agent_web_search/`)
- 🔄 **Updated scripts** to use proper CLI entry points
- 🔄 **Updated dependencies** to use `pyproject.toml` instead of `requirements.txt`
- 🔄 **Improved error handling** and type safety

### Removed
- ❌ **Old requirements.txt** (replaced by pyproject.toml)
- ❌ **Legacy file structure** (moved to proper src/ layout)

### Fixed
- 🐛 **Import organization** with ruff
- 🐛 **Type checking** with mypy
- 🐛 **Test coverage** for all major functions

---

## [1.0.0] - 2026-02-28

### Added
- ✅ Brave Search API integration
- ✅ Linkup Search API integration
- ✅ Command-line interfaces
- ✅ JSON output modes
- ✅ Comprehensive error handling
- ✅ Input validation
- ✅ Timeout protection
- ✅ Multi-word query support
- ✅ Environment variable authentication
- ✅ Full documentation

---

[Unreleased]:
- Planned features and improvements

[2.0.0]: https://github.com/ugo/agent-web-search/releases/tag/v2.0.0
[1.0.0]: https://github.com/ugo/agent-web-search/releases/tag/v1.0.0