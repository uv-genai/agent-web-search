# Linkup Search Script - API Fixes Applied

## Issue Resolved

**Error:** `API returned status code 404 - Details: Cannot POST /api/search`

## Root Causes & Fixes

### 1. Incorrect API Endpoint Path ❌ → ✅

**Problem:** Using `/api/search` instead of `/v1/search`

**Before:**
```python
base_url = "https://api.linkup.so/api/search"
```

**After:**
```python
base_url = "https://api.linkup.so/v1/search"
```

**Fetch endpoint also fixed:**
```python
# Before
base_url = "https://api.linkup.so/api/fetch"

# After  
base_url = "https://api.linkup.so/v1/fetch"
```

### 2. Wrong Authentication Header ❌ → ✅

**Problem:** Using `X-API-Key` header instead of `Authorization: Bearer`

**Before:**
```python
headers = {
    'X-API-Key': api_key,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
```

**After:**
```python
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
```

## Why These Changes Were Necessary

### Linkup API v1 Structure

According to the official Linkup API documentation:
- Base URL: `https://api.linkup.so`
- Version prefix: `/v1`
- Endpoints: `/v1/search` and `/v1/fetch`

The `/api/` prefix was incorrect and caused 404 errors.

### Authentication Method

Linkup uses **Bearer token authentication** (not `X-API-Key`):
- Header: `Authorization: Bearer <your-api-key>`
- This is the standard OAuth 2.0 style authentication used by most modern APIs

## Updated Script Features

All features remain intact with the corrected endpoints:

### Search Mode (`/v1/search`)
- ✅ Multiple output types (searchResults, sourcedAnswer, structured)
- ✅ Search depth options (standard, deep)
- ✅ Date filtering (--from-date, --to-date)
- ✅ Domain filtering (--include-domains, --exclude-domains)
- ✅ Customizable result count (-n flag)
- ✅ JSON output mode (--json)

### Fetch Mode (`/v1/fetch`)
- ✅ Content extraction (HTML or Markdown)
- ✅ JavaScript rendering support
- ✅ Structured JSON output

## Testing the Fixed Script

```bash
# Activate virtual environment
source venv/bin/activate

# Set your API key
export LINKUP_API_KEY="your-api-key-here"

# Test search
python linkup_search.py search "python tutorials" -n 5

# Test fetch
python linkup_search.py fetch "https://docs.python.org"

# Test with JSON output
python linkup_search.py search "machine learning" --depth deep --json
```

## Verification Checklist

- [x] API endpoint paths corrected to `/v1/search` and `/v1/fetch`
- [x] Authentication header changed to `Authorization: Bearer`
- [x] Script syntax validated
- [x] All parameters maintained
- [x] Error handling preserved
- [x] JSON output format unchanged

## References

- [Linkup API Documentation](https://docs.linkup.so/pages/documentation/api-reference)
- [Authentication Guide](https://docs.linkup.so/pages/documentation/development/authentication)
- [/search Endpoint](https://docs.linkup.so/pages/documentation/api-reference/endpoint/post-search)
- [/fetch Endpoint](https://docs.linkup.so/pages/documentation/api-reference/endpoint/post-fetch)

---

**Status:** ✅ Fixed and ready to use!

*The script now correctly communicates with the Linkup API using the proper endpoints and authentication method.*
