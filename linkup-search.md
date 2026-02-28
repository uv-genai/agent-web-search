---
name: linkup-search
description: Performs deep agentic web searches using the Linkup API with superior factuality. Use when the user asks for verified information, complex research, sourced answers, or content extraction from web pages.
dependencies: python>=3.8, requests
---

# Linkup Search Skill

This skill allows you to access the web via Linkup's AI-specific search API with superior factuality (#1 on SimpleQA benchmark). Use it when you need verified information, comprehensive research, or content extraction from web pages.

All the instructions in this document **ARE MANDATORY** and must be followed at all times.

## Overview

The Linkup Search script (`linkup_search.py`) provides agentic web search capabilities designed specifically for AI applications. It offers superior factuality, deep research capabilities, and built-in content fetching.

### Key Capabilities

- ✅ **Superior Factuality**: State-of-the-art performance on factuality benchmarks
- ✅ **Agentic Search**: Deep multi-step research workflows
- ✅ **Multiple Output Types**: searchResults, sourcedAnswer, structured
- ✅ **Content Fetching**: Built-in /fetch endpoint for page extraction
- ✅ **JavaScript Rendering**: Support for dynamic content
- ✅ **Advanced Filtering**: Date ranges, domain control
- ✅ **Markdown Extraction**: Clean content from web pages

### When to Use Linkup vs Brave

| Scenario | Recommended Tool |
|----------|------------------|
| Quick factual queries | Brave Search |
| Complex research questions | **Linkup Search** |
| Need verified sources | **Linkup Search** |
| Building AI chatbots | **Linkup Search** |
| Content aggregation | **Linkup Search** |
| Fact-checking claims | **Linkup Search** |
| Privacy-focused search | Brave Search |
| Simple documentation lookup | Brave Search |

## Prerequisites

Before using this skill, ensure:

1. **API Key Configuration**: The `LINKUP_API_KEY` environment variable must be set
   ```bash
   export LINKUP_API_KEY="your-api-key-here"
   ```
   Get your free key from: https://app.linkup.so/

2. **Dependencies Installed**: Ensure the project dependencies are installed
   ```bash
   pip install -r requirements_linkup.txt
   # OR using uv
   uv run pip install -r requirements_linkup.txt
   ```

3. **Virtual Environment**: Activate the virtual environment if available
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage Instructions

### Basic Usage Pattern

When you need to perform deep research or get verified information, use the following pattern:

```python
import subprocess
import json
from typing import Optional, List, Dict

class LinkupSearchAgent:
    """Coding agent tool for Linkup Search integration."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize with optional API key override."""
        self.api_key = api_key or os.getenv('LINKUP_API_KEY')
        if not self.api_key:
            raise ValueError("LINKUP_API_KEY environment variable not set")
    
    def search(
        self, 
        query: str, 
        num_results: int = 10,
        depth: str = 'standard',
        output_type: str = 'searchResults',
        as_json: bool = True
    ) -> Dict:
        """
        Perform a deep web search.
        
        Args:
            query: The search query string
            num_results: Number of results to return (1-100)
            depth: 'standard' (fast) or 'deep' (comprehensive)
            output_type: 'searchResults', 'sourcedAnswer', or 'structured'
            as_json: If True, return structured JSON
            
        Returns:
            Dictionary containing search results
            
        Raises:
            RuntimeError: If search fails or API key is missing
        """
        if num_results < 1 or num_results > 100:
            raise ValueError("num_results must be between 1 and 100")
        
        cmd = [
            'python', 'linkup_search.py', 'search',
            query,
            '-n', str(num_results),
            '--depth', depth,
            '--output-type', output_type,
            '--json' if as_json else ''
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode != 0:
            error_msg = result.stderr.strip() or "Unknown error"
            raise RuntimeError(f"Search failed: {error_msg}")
        
        return json.loads(result.stdout)
    
    def fetch_page(self, url: str, render_js: bool = False) -> Dict:
        """
        Fetch and extract content from a web page.
        
        Args:
            url: The URL to fetch
            render_js: If True, execute JavaScript before extraction
            
        Returns:
            Dictionary containing extracted content
        """
        cmd = [
            'python', 'linkup_search.py', 'fetch',
            url,
            '--render-js' if render_js else '',
            '--json'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode != 0:
            error_msg = result.stderr.strip() or "Unknown error"
            raise RuntimeError(f"Fetch failed: {error_msg}")
        
        return json.loads(result.stdout)
```

### Command-Line Interface

The script supports two modes: **search** and **fetch**.

#### Search Mode Options

| Option | Description | Default | Required |
|--------|-------------|---------|----------|
| `query` | Search query string | - | Yes |
| `-n`, `--num-results` | Number of results (1-100) | 10 | No |
| `--depth` | Search depth: standard or deep | standard | No |
| `--output-type` | Output type: searchResults, sourcedAnswer, structured | searchResults | No |
| `--from-date` | Filter from date (YYYY-MM-DD) | None | No |
| `--to-date` | Filter to date (YYYY-MM-DD) | None | No |
| `--include-domains` | Restrict to specific domains | None | No |
| `--exclude-domains` | Exclude specific domains | None | No |
| `--json` | Output as raw JSON | False | Optional |

#### Fetch Mode Options

| Option | Description | Default | Required |
|--------|-------------|---------|----------|
| `url` | URL to fetch | - | Yes |
| `--output-format` | Output format: html or markdown | markdown | No |
| `--render-js` | Execute JavaScript | False | No |
| `--json` | Output as raw JSON | False | Optional |

### Common Search Patterns

#### 1. Standard Search (Fast)
```bash
python linkup_search.py search "python tutorial" -n 5
```

#### 2. Deep Research (Comprehensive)
```bash
python linkup_search.py search "AI trends 2026" --depth deep -n 10
```

#### 3. Sourced Answer (Natural Language)
```bash
python linkup_search.py search "what is machine learning" --output-type sourcedAnswer
```

#### 4. With Date Filtering
```bash
python linkup_search.py search "Python updates" \
  --from-date 2026-01-01 \
  --to-date 2026-02-28 \
  -n 10
```

#### 5. With Domain Filtering
```bash
python linkup_search.py search "Python documentation" \
  --include-domains python.org docs.python.org \
  -n 5
```

#### 6. Fetch Webpage Content
```bash
python linkup_search.py fetch "https://docs.python.org"
```

#### 7. Fetch with JavaScript Rendering
```bash
python linkup_search.py fetch "https://dynamic-site.com" --render-js --json
```

## Response Formats

### 1. Search Results Output Type

#### Human-Readable Format
```
============================================================
Linkup Search Results for: open source licenses
Depth: standard, Output Type: searchResults
Showing up to 5 results
============================================================

1. Licenses - Open Source Initiative
   URL: https://opensource.org/licenses
   Content: OSI Approved Licenses Open source licenses are licenses that comply with the Open Source Definition...

2. Open source licenses grant permission for anybody to use, ...
   URL: https://choosealicense.com/licenses/
   Content: Open source licenses grant permission for anybody to use, modify, and share licensed software...

Total results displayed: 5
```

#### JSON Format
```json
{
  "mode": "search",
  "query": "open source licenses",
  "parameters": {
    "num_results_requested": 5,
    "depth": "standard",
    "output_type": "searchResults"
  },
  "results": [
    {
      "name": "Licenses - Open Source Initiative",
      "url": "https://opensource.org/licenses",
      "content": "OSI Approved Licenses...",
      "type": "source"
    }
  ],
  "error": false,
  "total_found": 5
}
```

### 2. Sourced Answer Output Type

#### Human-Readable Format
```
============================================================
Linkup Search Results for: what is machine learning
Depth: standard, Output Type: sourcedAnswer
Showing up to 10 results
============================================================

Answer:
Machine learning is a subset of artificial intelligence that focuses on developing algorithms and models that enable computers to learn from and make predictions based on data...

Sources:
  1. Stanford Encyclopedia of Philosophy (https://plato.stanford.edu/)
  2. MIT Technology Review (https://www.technologyreview.com/)
  3. Nature Machine Intelligence (https://www.nature.com/natmachintell/)
```

#### JSON Format
```json
{
  "mode": "search",
  "query": "what is machine learning",
  "parameters": {
    "num_results_requested": 10,
    "depth": "standard",
    "output_type": "sourcedAnswer"
  },
  "answer": "Machine learning is a subset of artificial intelligence...",
  "sources": [
    {
      "name": "Stanford Encyclopedia of Philosophy",
      "url": "https://plato.stanford.edu/",
      "content": "..."
    }
  ],
  "error": false
}
```

### 3. Structured Output Type

#### JSON Format (Custom Schema)
```json
{
  "mode": "search",
  "query": "latest Python versions",
  "parameters": {
    "num_results_requested": 5,
    "depth": "standard",
    "output_type": "structured"
  },
  "structured_data": {
    "versions": [
      {"version": "3.12", "release_date": "2023-10-02"},
      {"version": "3.13", "release_date": "2024-10-07"}
    ]
  },
  "error": false
}
```

### 4. Fetch Output

#### Human-Readable Format
```
============================================================
Fetching: https://docs.python.org
Format: markdown, Render JS: False
============================================================

URL: https://docs.python.org
Format: markdown
Timestamp: 2026-02-28T10:30:00Z

------------------------------------------------------------

Welcome to Python's Official Documentation
==========================================

Python is an interpreted, high-level programming language...

[Full content extracted...]

------------------------------------------------------------
```

#### JSON Format
```json
{
  "mode": "fetch",
  "url": "https://docs.python.org",
  "parameters": {
    "output_format": "markdown",
    "render_js": false
  },
  "content": "Welcome to Python's Official Documentation...\n\n[Full content]",
  "output_format": "markdown",
  "timestamp": "2026-02-28T10:30:00Z",
  "error": false
}
```

## Integration Examples

### Python Integration

#### Advanced Search Agent
```python
import subprocess
import json
from typing import Optional, List, Dict, Any
from datetime import datetime

class LinkupResearchAgent:
    """Advanced agent for comprehensive web research."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize with optional API key override."""
        self.api_key = api_key or os.getenv('LINKUP_API_KEY')
        if not self.api_key:
            raise ValueError("LINKUP_API_KEY environment variable not set")
    
    def research(
        self, 
        topic: str,
        depth: str = 'deep',
        max_results: int = 20
    ) -> Dict[str, Any]:
        """
        Perform comprehensive research on a topic.
        
        Uses deep search with multiple output types for thorough coverage.
        """
        # Step 1: Get broad overview
        overview = self.search(
            f"{topic} overview",
            num_results=5,
            depth='standard',
            output_type='sourcedAnswer'
        )
        
        # Step 2: Get detailed results
        details = self.search(
            f"{topic} detailed analysis",
            num_results=max_results,
            depth=depth,
            output_type='searchResults'
        )
        
        # Step 3: Extract key sources
        key_sources = self._extract_key_sources(details['results'])
        
        return {
            'topic': topic,
            'overview': overview.get('answer', ''),
            'detailed_results': details['results'],
            'key_sources': key_sources,
            'research_timestamp': datetime.now().isoformat()
        }
    
    def _extract_key_sources(self, results: List[Dict]) -> List[Dict]:
        """Extract most relevant sources from results."""
        # Sort by relevance (you can implement custom logic here)
        sorted_results = sorted(
            results,
            key=lambda x: len(x.get('content', '')),
            reverse=True
        )
        return sorted_results[:10]
    
    def verify_claim(self, claim: str) -> Dict[str, Any]:
        """Verify a claim using deep search."""
        verification_query = f"{claim} verified fact check"
        
        result = self.search(
            verification_query,
            num_results=10,
            depth='deep',
            output_type='sourcedAnswer'
        )
        
        return {
            'claim': claim,
            'verification': result.get('answer', ''),
            'supporting_sources': result.get('sources', []),
            'confidence': self._calculate_confidence(result)
        }
    
    def _calculate_confidence(self, result: Dict) -> float:
        """Calculate confidence score based on sources."""
        sources = result.get('sources', [])
        if not sources:
            return 0.0
        
        # Simple confidence calculation based on source quality
        high_quality_domains = ['.edu', '.gov', '.org']
        high_quality_count = sum(
            1 for s in sources
            if any(domain in s.get('url', '').lower() for domain in high_quality_domains)
        )
        
        return min(1.0, high_quality_count / len(sources))
```

### LangChain Tool Integration

```python
from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class LinkupSearchInput(BaseModel):
    """Input for Linkup Search tool."""
    query: str = Field(..., description="Search query string")
    depth: str = Field(default='standard', description="Search depth: standard or deep")
    num_results: int = Field(default=5, description="Number of results (1-100)")
    use_sourced_answer: bool = Field(default=False, description="Return natural language answer")

class LinkupSearchTool(BaseTool):
    """Tool for performing deep web searches with Linkup."""
    
    name: str = "linkup_deep_search"
    description: str = "Perform deep, factual web searches with verified sources"
    args_schema: Type[BaseModel] = LinkupSearchInput
    
    def _run(self, query: str, depth: str = 'standard', num_results: int = 5, use_sourced_answer: bool = False) -> str:
        """Execute the search and return formatted results."""
        try:
            output_type = 'sourcedAnswer' if use_sourced_answer else 'searchResults'
            
            cmd = [
                'python', 'linkup_search.py', 'search',
                query,
                '-n', str(num_results),
                '--depth', depth,
                '--output-type', output_type,
                '--json'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode != 0:
                return f"Search failed: {result.stderr}"
            
            data = json.loads(result.stdout)
            
            if use_sourced_answer:
                answer = data.get('answer', 'No answer found.')
                sources = data.get('sources', [])
                
                output = f"Answer:\n{answer}\n\nSources:\n"
                for i, source in enumerate(sources[:5], 1):
                    output += f"{i}. {source['name']} ({source['url']})\n"
                
                return output
            else:
                results = data.get('results', [])
                if not results:
                    return "No results found."
                
                output = []
                for i, result in enumerate(results[:5], 1):
                    output.append(f"{i}. {result['name']}\n   {result['url']}\n   {result['content'][:200]}...")
                
                return "\n\n".join(output)
                
        except Exception as e:
            return f"Search error: {str(e)}"
```

### CrewAI Task Integration

```python
from crewai import Agent, Task, Process
from your_module import LinkupSearchTool

# Create research agent with Linkup
research_agent = Agent(
    role='Deep Research Specialist',
    goal='Conduct comprehensive, factually accurate web research',
    backstory='Expert at using Linkup\'s deep search to find verified information',
    verbose=True,
    tools=[LinkupSearchTool()]
)

# Create research task with deep search
research_task = Task(
    description="""
    Research {topic} thoroughly using deep search.
    Find official documentation, recent developments, and expert opinions.
    Verify all claims with multiple sources.
    Return a comprehensive report with citations.
    """,
    agent=research_agent,
    expected_output="Comprehensive research report with verified sources",
    tools=[LinkupSearchTool()]
)

# Execute with deep research
from crewai import Project

project = Project(
    tasks=[research_task],
    process=Process.sequential
)

results = project.execute()
```

### RAG Pipeline Integration

```python
from typing import List, Dict
import chromadb
from chromadb.config import Settings

class LinkupRAGPipeline:
    """RAG pipeline using Linkup for retrieval."""
    
    def __init__(self, collection_name: str = "web_research"):
        """Initialize RAG pipeline with ChromaDB."""
        self.client = chromadb.Client(Settings(anonymized_telemetry=False))
        self.collection = self.client.get_or_create_collection(collection_name)
        self.searcher = LinkupSearchAgent()
    
    def index_web_content(self, query: str, num_results: int = 10) -> int:
        """Index web search results into vector database."""
        results = self.searcher.search(query, num_results=num_results)
        
        documents = []
        metadatas = []
        ids = []
        
        for i, result in enumerate(results['results']):
            documents.append(result.get('content', ''))
            metadatas.append({
                'title': result.get('name', ''),
                'url': result.get('url', ''),
                'source': 'linkup_search',
                'query': query
            })
            ids.append(f"{query}_{i}")
        
        if documents:
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
        
        return len(documents)
    
    def retrieve_relevant(self, query: str, n_results: int = 5) -> List[Dict]:
        """Retrieve relevant web content for a query."""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            include=['documents', 'metadatas']
        )
        
        return list(zip(
            results['documents'][0],
            results['metadatas'][0]
        ))
```

### Shell Script Integration

```bash
#!/bin/bash
# Quick Linkup search wrapper with filtering

TOPIC="$1"
DEPTH="${2:-standard}"
NUM_RESULTS="${3:-5}"

if [ -z "$TOPIC" ]; then
    echo "Usage: $0 <topic> [depth] [num_results]"
    echo "  depth: standard or deep (default: standard)"
    echo "  num_results: 1-100 (default: 5)"
    exit 1
fi

# Search and extract URLs
python linkup_search.py search "$TOPIC" \
  --depth "$DEPTH" \
  -n "$NUM_RESULTS" \
  --json | jq -r '.results[] | "\(.name): \(.url)"'
```

## Error Handling

### Common Errors and Solutions

#### 1. API Key Not Set
```
Error: LINKUP_API_KEY environment variable not set.
Get your free API key from: https://app.linkup.so/
Set it with: export LINKUP_API_KEY='your-api-key-here'
```

**Solution**: Set the environment variable before running the script.

#### 2. Request Timed Out
```
Error: Request timed out.
```

**Solution**: 
- Check internet connection
- Reduce number of results with `-n`
- Use `--depth standard` instead of `deep`
- Try again later

#### 3. Invalid API Key
```
Error: API returned status code 401
Details: Invalid API key
```

**Solution**: Verify your API key at the Linkup dashboard and ensure no extra spaces.

#### 4. No Results Found
```
No results found.
```

**Solution**: 
- Try different search terms
- Increase result count with `-n`
- Check spelling and query format
- Try `--depth deep` for complex queries

### Robust Error Handling Pattern

```python
import subprocess
import json
from typing import Optional, Tuple, Dict, Any
from functools import wraps

def linkup_search_with_retry(
    query: str,
    num_results: int = 10,
    depth: str = 'standard',
    max_retries: int = 3,
    backoff_factor: float = 2.0
) -> Tuple[bool, Optional[Dict], Optional[str]]:
    """
    Perform Linkup search with robust error handling and retry logic.
    
    Args:
        query: Search query string
        num_results: Number of results to return
        depth: Search depth (standard or deep)
        max_retries: Maximum number of retry attempts
        backoff_factor: Backoff multiplier for retries
        
    Returns:
        Tuple of (success, results_dict, error_message)
    """
    last_error = None
    
    for attempt in range(max_retries):
        try:
            cmd = [
                'python', 'linkup_search.py', 'search',
                query,
                '-n', str(num_results),
                '--depth', depth,
                '--json'
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode != 0:
                error_msg = result.stderr.strip()
                last_error = error_msg
                
                if attempt < max_retries - 1:
                    sleep_time = backoff_factor ** attempt
                    time.sleep(sleep_time)
                    continue
                
                return False, None, f"Search failed after {max_retries} attempts: {error_msg}"
            
            data = json.loads(result.stdout)
            
            # Check for errors in response
            if data.get('error'):
                error_msg = data.get('error_message', 'Unknown error')
                last_error = error_msg
                
                if attempt < max_retries - 1:
                    sleep_time = backoff_factor ** attempt
                    time.sleep(sleep_time)
                    continue
                
                return False, None, error_msg
            
            return True, data, None
            
        except subprocess.TimeoutExpired:
            last_error = "Request timed out"
            if attempt < max_retries - 1:
                sleep_time = backoff_factor ** attempt
                time.sleep(sleep_time)
                continue
            return False, None, f"Search timed out after {max_retries} attempts"
            
        except json.JSONDecodeError as e:
            last_error = f"Invalid JSON response: {e}"
            if attempt < max_retries - 1:
                time.sleep(backoff_factor ** attempt)
                continue
            return False, None, "Invalid JSON response"
            
        except Exception as e:
            last_error = f"Unexpected error: {str(e)}"
            if attempt < max_retries - 1:
                time.sleep(backoff_factor ** attempt)
                continue
            return False, None, f"Unexpected error: {str(e)}"
    
    return False, None, f"Max retries exceeded. Last error: {last_error}"

# Decorator for retry logic
def retry_on_failure(max_retries: int = 3):
    """Decorator to add retry logic to functions."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)
                        continue
                    raise last_error
            
            raise last_error
        return wrapper
    return decorator
```

## Best Practices

### For Coding Agents

1. **Choose Appropriate Depth**: Use `standard` for quick queries, `deep` for complex research.

2. **Select Right Output Type**: 
   - `searchResults` for raw data processing
   - `sourcedAnswer` for natural language responses
   - `structured` for custom schema extraction

3. **Validate Input**: Ensure queries don't contain special characters that could cause issues.

4. **Handle Rate Limits**: Respect API limits (check your plan's quota).

5. **Cache Results**: Store frequently searched queries to avoid redundant API calls.

6. **Timeout Protection**: Always set reasonable timeouts (60 seconds recommended for deep search).

7. **Error Recovery**: Implement retry logic for transient failures.

8. **Result Processing**: Post-process results to filter irrelevant content and prioritize quality sources.

### Query Optimization

#### Good Queries
```python
# Specific and focused
"Python 3.12 new features documentation"
"machine learning frameworks comparison 2026"
"React hooks best practices official guide"

# With context
"quantum computing breakthroughs 2026 verified"
"Docker container security best practices"
"kubernetes deployment strategies enterprise"
```

#### Poor Queries
```python
# Too vague
"stuff about programming"
"how to do things"
"technology news"

# Too long
"can you please search for me the best tutorials about how to learn python programming language step by step with examples and video courses"
```

### When to Use Each Output Type

#### searchResults
- ✅ Need raw data for processing
- ✅ Building custom aggregators
- ✅ Data extraction pipelines
- ✅ Competitive analysis

#### sourcedAnswer
- ✅ Need natural language answers
- ✅ Building chatbots/responses
- ✅ Quick summaries with citations
- ✅ Fact-checking support

#### structured
- ✅ Custom schema requirements
- ✅ Data extraction from specific formats
- ✅ Database population
- ✅ API response generation

## Performance Considerations

### Response Times
- **Standard search**: ~1-3 seconds
- **Deep search**: ~5-10 seconds
- **Sourced answer**: ~3-5 seconds
- **Page fetch**: ~2-5 seconds
- **Fetch with JS**: ~5-10 seconds

### Optimization Tips

1. **Minimize Result Count**: Only request what you need (default 10 is usually sufficient).

2. **Use Appropriate Depth**: Don't use `deep` unless necessary for complex queries.

3. **Specific Queries**: More specific queries return better results faster.

4. **Batch Processing**: If searching multiple topics, consider batching requests.

5. **Parallel Execution**: For independent searches, run them in parallel (with rate limit awareness).

6. **Caching Strategy**: Implement intelligent caching for repeated queries.

## Testing Your Setup

### Verification Script

```python
#!/usr/bin/env python3
"""Test script to verify Linkup Search integration."""

import subprocess
import json
import sys
from typing import List, Dict

def test_linkup_search():
    """Test basic search functionality."""
    print("Testing Linkup Search integration...")
    
    tests_passed = 0
    tests_total = 0
    
    # Test 1: Basic search
    tests_total += 1
    print("\n1. Testing basic search...")
    cmd = ['python', 'linkup_search.py', 'search', 'python tutorial', '-n', '3', '--json']
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    
    if result.returncode != 0:
        print(f"❌ Failed: {result.stderr}")
        return False
    
    try:
        data = json.loads(result.stdout)
        if not data.get('results'):
            print("❌ No results found")
            return False
        
        print(f"✅ Success! Found {len(data['results'])} results")
        tests_passed += 1
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False
    
    # Test 2: Deep search
    tests_total += 1
    print("\n2. Testing deep search...")
    cmd = ['python', 'linkup_search.py', 'search', 'machine learning', '--depth', 'deep', '-n', '2', '--json']
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    
    if result.returncode == 0:
        data = json.loads(result.stdout)
        if data.get('results'):
            print(f"✅ Deep search successful!")
            tests_passed += 1
        else:
            print("⚠️  Deep search completed but no results")
            tests_passed += 1  # Still counts as success
    else:
        print(f"⚠️  Deep search timeout or error: {result.stderr[:100]}")
    
    # Test 3: Fetch
    tests_total += 1
    print("\n3. Testing page fetch...")
    cmd = ['python', 'linkup_search.py', 'fetch', 'https://docs.python.org', '--json']
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    
    if result.returncode == 0:
        data = json.loads(result.stdout)
        if data.get('content'):
            print(f"✅ Fetch successful! Content length: {len(data['content'])} chars")
            tests_passed += 1
        else:
            print("⚠️  Fetch completed but no content")
    else:
        print(f"⚠️  Fetch error: {result.stderr[:100]}")
    
    print(f"\n{'='*60}")
    print(f"Tests passed: {tests_passed}/{tests_total}")
    print(f"{'='*60}")
    
    return tests_passed == tests_total

if __name__ == '__main__':
    success = test_linkup_search()
    sys.exit(0 if success else 1)
```

## Additional Resources

- [Linkup API Documentation](https://docs.linkup.so/pages/documentation/api-reference)
- [Linkup Dashboard](https://app.linkup.so/)
- [Python SDK Documentation](https://docs.linkup.so/pages/sdk/python/python)
- [Authentication Guide](https://docs.linkup.so/pages/documentation/development/authentication)
- [Feature Summary](./FEATURES_LINKUP.md)
- [Project Summary](./PROJECT_SUMMARY.md)

## Troubleshooting Checklist

- [ ] `LINKUP_API_KEY` environment variable is set
- [ ] Dependencies are installed (`pip install -r requirements_linkup.txt`)
- [ ] Virtual environment is activated
- [ ] Internet connection is working
- [ ] API key is valid (check dashboard)
- [ ] Query doesn't contain problematic characters
- [ ] Result count is within bounds (1-100)
- [ ] Timeout is set appropriately (60s for deep search)
- [ ] Correct output type selected for use case
- [ ] Appropriate depth chosen (standard vs deep)

## Common Use Cases

### 1. AI Chatbot Enhancement
```python
# Provide grounded, factual responses with citations
def answer_user_question(question: str) -> str:
    result = linkup_agent.search(
        question,
        depth='deep',
        output_type='sourcedAnswer'
    )
    
    answer = result.get('answer', '')
    sources = result.get('sources', [])
    
    response = f"Based on my research:\n\n{answer}\n\n"
    response += "Sources:\n"
    for i, source in enumerate(sources[:5], 1):
        response += f"{i}. {source['name']}: {source['url']}\n"
    
    return response
```

### 2. Research Assistant
```python
# Gather comprehensive information on complex topics
def research_topic(topic: str) -> Dict:
    # Broad overview
    overview = linkup_agent.search(
        f"{topic} overview",
        depth='deep',
        output_type='sourcedAnswer'
    )
    
    # Detailed results
    details = linkup_agent.search(
        f"{topic} detailed analysis",
        depth='deep',
        num_results=20
    )
    
    return {
        'overview': overview.get('answer'),
        'sources': details.get('results', []),
        'key_points': extract_key_points(details)
    }
```

### 3. Content Aggregation
```python
# Fetch and process multiple web pages
def aggregate_content(urls: List[str]) -> List[Dict]:
    contents = []
    for url in urls:
        try:
            result = linkup_agent.fetch_page(url)
            contents.append({
                'url': url,
                'content': result.get('content', ''),
                'format': result.get('output_format', 'markdown')
            })
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
    
    return contents
```

### 4. Fact-Checking
```python
# Verify claims with current, sourced information
def verify_claim(claim: str) -> Dict:
    verification = linkup_agent.search(
        f"{claim} verified fact check",
        depth='deep',
        output_type='sourcedAnswer'
    )
    
    return {
        'claim': claim,
        'verification': verification.get('answer', ''),
        'sources': verification.get('sources', []),
        'confidence': calculate_confidence(verification)
    }
```

---

*Generated by linkup-search skill on 2026-02-28*
