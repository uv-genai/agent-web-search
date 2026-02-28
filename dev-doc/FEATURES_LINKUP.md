# Linkup Search Script - Feature Summary

## Overview

Linkup is specifically designed for AI applications, providing superior factuality and grounded responses. This script mirrors the functionality of `search.py` but leverages Linkup's advanced agentic search capabilities.

---

## 🎯 Key Differences from Brave Search

| Feature | Brave Search | Linkup Search |
|---------|-------------|---------------|
| **Purpose** | General privacy-focused search | AI-specific agentic search |
| **Factuality** | Good | ⭐ State-of-the-art (SOTA) |
| **Search Depth** | Standard only | Standard + Deep (multi-step research) |
| **Output Types** | Basic results | searchResults, sourcedAnswer, structured |
| **Content Fetching** | ❌ No | ✅ Built-in /fetch endpoint |
| **Date Filtering** | ✅ Yes | ✅ Yes |
| **Domain Filtering** | ✅ Yes | ✅ Yes |
| **JavaScript Rendering** | ❌ No | ✅ Yes (via /fetch) |
| **Markdown Extraction** | ❌ No | ✅ Yes |

---

## 🔍 Search Capabilities

### 1. Multiple Output Types

#### searchResults (Default)
Returns raw sources with URLs and snippets:
```json
{
  "sources": [
    {
      "name": "Real Python",
      "url": "https://realpython.com",
      "content": "Python tutorial content..."
    }
  ]
}
```

#### sourcedAnswer
Returns natural language answer with citations:
```json
{
  "answer": "Python is a high-level programming language...",
  "sources": [...]
}
```

#### structured
Custom JSON schema output (for data extraction):
```json
{
  "products": [
    {"name": "Product A", "price": 99}
  ]
}
```

### 2. Search Depth Options

- **standard**: Fast basic search (~1-2 seconds)
- **deep**: Comprehensive multi-step research (~5-10 seconds)

Deep search performs:
- Multi-source verification
- Cross-referencing
- Fact-checking
- Synthesis of information

### 3. Advanced Filtering

#### Date Range
```bash
--from-date 2026-01-01 --to-date 2026-02-28
```

#### Domain Control
```bash
# Only specific domains
--include-domains python.org realpython.com

# Exclude domains
--exclude-domains medium.com reddit.com
```

---

## 📄 Content Fetching

The `/fetch` endpoint extracts webpage content:

### Features
- ✅ Markdown or HTML output
- ✅ JavaScript rendering support
- ✅ Clean content extraction
- ✅ Timestamp tracking

### Usage
```bash
python linkup_search.py fetch "https://example.com" --output-format markdown
python linkup_search.py fetch "https://example.com" --render-js --json
```

---

## 🤖 AI Agent Integration

### Why Linkup for AI Agents?

1. **Superior Factuality**: #1 in world for factuality on SimpleQA benchmark
2. **Grounded Responses**: Reduces hallucinations with cited sources
3. **Agentic Search**: Understands complex queries naturally
4. **Structured Data**: Easy to parse and integrate

### Example: LangChain Tool

```python
from langchain.tools import BaseTool
import subprocess
import json

class LinkupSearchTool(BaseTool):
    name = "linkup_search"
    description = "Search the web using Linkup's agentic search"
    
    def _run(self, query: str, depth: str = "standard"):
        cmd = [
            'python', 'linkup_search.py', 'search',
            query, '--depth', depth, '--json'
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
```

### Example: CrewAI Task

```python
from crewai import Agent, Task, Process

search_agent = Agent(
    role='Research Analyst',
    goal='Use Linkup to find factual information',
    backstory='Expert at using agentic search tools',
    verbose=True
)

task = Task(
    description='Research latest AI developments using deep search',
    agent=search_agent,
    expected_output='Comprehensive report with sources'
)
```

---

## 📊 Performance Comparison

| Metric | Brave Search | Linkup Search |
|--------|-------------|---------------|
| Response Time (standard) | ~1-2s | ~1-3s |
| Response Time (deep) | N/A | ~5-10s |
| Factuality Score | Good | SOTA (#1) |
| Citation Quality | Good | Excellent |
| Complex Query Handling | Moderate | Excellent |
| Content Extraction | None | Full page fetch |

---

## 🎨 Use Cases

### 1. AI Chatbot Enhancement
Provide factual answers with citations to reduce hallucinations.

```python
query = "What are the latest Python features?"
results = linkup_search(query, depth="deep")
answer = results['answer']
sources = results['sources']
# Use answer in chatbot response with source links
```

### 2. Research Assistant
Gather comprehensive information on complex topics.

```bash
python linkup_search.py search "quantum computing 2026" --depth deep -n 20
```

### 3. Content Aggregation
Fetch and process multiple web pages.

```python
urls = ["https://docs.python.org", "https://realpython.com"]
for url in urls:
    content = linkup_fetch(url, output_format="markdown")
    process_content(content)
```

### 4. Competitive Analysis
Monitor specific domains for updates.

```bash
python linkup_search.py search "machine learning" \
  --include-domains arxiv.org jupyter.org \
  --from-date 2026-02-01 --json
```

### 5. Fact-Checking
Verify claims with current, sourced information.

```python
claim = "Python 3.12 improved performance by 10%"
verification = linkup_search(f"{claim} verified", depth="deep")
print(verification['answer'])
```

---

## 🔧 Advanced Features

### 1. Prompt Optimization
Use Linkup's Prompt Optimizer for better results:
- Visit: https://prompt.linkup.so
- Optimize your query before searching

### 2. Structured Output Schema
Define custom JSON schemas for data extraction:
```python
schema = {
  "type": "object",
  "properties": {
    "articles": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {"type": "string"},
          "date": {"type": "string"}
        }
      }
    }
  }
}
```

### 3. Batch Processing
Process multiple queries efficiently:
```python
queries = [
    "Python tutorials",
    "Machine learning basics",
    "Web development frameworks"
]

for query in queries:
    results = linkup_search(query, num_results=5)
    save_results(results)
```

---

## 💡 Best Practices

### For Better Search Results

1. **Be Specific**: Detailed prompts yield better results
2. **Use Deep Search**: For complex or ambiguous queries
3. **Filter by Date**: Get recent, relevant information
4. **Specify Domains**: Focus on trusted sources
5. **Choose Output Type**: Match to your use case

### For Efficient API Usage

1. **Cache Results**: Store frequently searched queries
2. **Batch Requests**: Group related searches when possible
3. **Use Standard Depth**: Unless deep research needed
4. **Monitor Quotas**: Track API usage limits
5. **Error Handling**: Implement retry logic

### For AI Integration

1. **Citation Tracking**: Always include source links
2. **Confidence Scoring**: Weight results by source reliability
3. **Cross-Reference**: Verify important claims
4. **Update Frequency**: Refresh cached results periodically
5. **User Feedback**: Learn from user corrections

---

## 🚀 Quick Start Comparison

### Brave Search
```bash
export BRAVE_API_KEY="key"
python search.py "query" -n 5
```

### Linkup Search
```bash
export LINKUP_API_KEY="key"
python linkup_search.py search "query" -n 5 --depth standard
python linkup_search.py search "complex query" --depth deep
python linkup_search.py fetch "https://example.com"
```

---

## 📈 When to Use Each

### Use Brave Search When:
- Privacy is the primary concern
- Simple, straightforward queries
- No API key available (free tier)
- Need fast, basic results

### Use Linkup Search When:
- Building AI applications
- Need highly factual responses
- Complex research questions
- Want sourced answers
- Need to fetch webpage content
- Require structured data extraction

---

## 🎉 Summary

Linkup Search Script provides:
- ✅ Agentic search with deep research capability
- ✅ Superior factuality for AI applications
- ✅ Multiple output formats (searchResults, sourcedAnswer, structured)
- ✅ Built-in content fetching with /fetch endpoint
- ✅ Advanced filtering (dates, domains)
- ✅ JavaScript rendering support
- ✅ JSON output for automation
- ✅ Mirror functionality to search.py with enhanced features

Perfect for AI agents, research assistants, and any application requiring high-quality, grounded web search capabilities.
