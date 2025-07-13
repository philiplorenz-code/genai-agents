# AgentMaker: Universal Agent Generation & Enhancement System

## 🚀 Transform Ideas into Production-Ready AI Agents in Minutes

This comprehensive guide provides two powerful approaches for creating fully functional AI agents: **Template-Based Generation** for rapid development and **Enhancement Patterns** for transforming existing boilerplate into production-ready code.

## Table of Contents
1. [Quick Start: Template-Based Generation](#quick-start-template-based-generation)
2. [Agent Template System](#agent-template-system)
3. [Enhancement Patterns for Existing Agents](#enhancement-patterns-for-existing-agents)
4. [Universal Generation Prompts](#universal-generation-prompts)
5. [Advanced Implementation Patterns](#advanced-implementation-patterns)
6. [Agent Archetypes & Examples](#agent-archetypes--examples)
7. [Testing & Validation](#testing--validation)
8. [Production Deployment](#production-deployment)
9. [Best Practices](#best-practices)

---

## Quick Start: Template-Based Generation

### The Universal Agent Generation Prompt

Use this as your primary prompt for creating new agents from scratch:

```
You are an expert AI agent developer. Your task is to create working agent code based on templates and user requirements.

## Agent Template Structure

### Main Agent File (agent.py):
```python
import asyncio
import os
from typing import Annotated
from dotenv import load_dotenv
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext

# Load environment variables from .env file
load_dotenv()

AGENT_JWT = "{{agent_token}}"  # Keep this exactly as is - DO NOT CHANGE
session = GenAISession(jwt_token=AGENT_JWT)

@session.bind(
    name="[AGENT_NAME]",  # Replace with short agent name in snake_case (e.g., weather_agent)
    description="[AGENT_DESCRIPTION]"  # Replace with brief description of what the agent does
)
async def [AGENT_FUNCTION_NAME](  # Replace with same name as above
    agent_context: GenAIContext,
    [PARAMETER_NAME]: Annotated[
        [PARAMETER_TYPE],  # Replace with appropriate type (str, int, float, etc.)
        "[PARAMETER_DESCRIPTION]",  # Replace with description of what this parameter does
    ],
    # Add more parameters as needed following the same pattern
):
    """[AGENT_DESCRIPTION]"""  # Same description as in @session.bind
    
    # [IMPLEMENT_AGENT_LOGIC_HERE]
    # Replace this section with the actual agent functionality
    # Use os.getenv("VARIABLE_NAME") to access environment variables for API keys and secrets
    # Return appropriate result based on agent's purpose
    
    return "[AGENT_RESULT]"  # Replace with actual return value. NOTE: the return value must be JSON serializable

async def main():
    print(f"Agent with token '{AGENT_JWT}' started")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
```

### Dependencies File (pyproject.toml):
```toml
[project]
name = "genai-agents"
version = "0.1.0"
description = "[PROJECT_DESCRIPTION]"  # Replace with project description
requires-python = ">=3.12"
dependencies = [
    "genai-protocol",  # REQUIRED - never remove this dependency
    "python-dotenv>=1.0.0",  # REQUIRED - for loading environment variables
    # Add additional dependencies below if needed for your agent
    # Examples: "requests>=2.32.3", "aiohttp>=3.8.0", "openai>=1.70.0"
]
```

### Environment Variables File (.env):
```env
# [ENV_VARIABLES]
# Add environment variables needed for your agent
# Example: OPENWEATHER_API_KEY=your_api_key_here
# Example: SLACK_WEBHOOK_URL=your_slack_webhook_url_here
```

## Replacement Instructions:
1. [AGENT_NAME] - Short descriptive name in snake_case (e.g., `weather_agent`, `translator_agent`, `calculator_agent`)
2. [AGENT_FUNCTION_NAME] - Same as AGENT_NAME, used as the function name
3. [AGENT_DESCRIPTION] - Brief description of what the agent does (e.g., "Returns current weather for specified location")
4. [PROJECT_DESCRIPTION] - Description for the pyproject.toml file
5. [PARAMETER_NAME] - Name of input parameter(s) your agent needs
6. [PARAMETER_TYPE] - Python type for the parameter (str, int, float, list, dict, etc.)
7. [PARAMETER_DESCRIPTION] - Clear description of what the parameter is for
8. [IMPLEMENT_AGENT_LOGIC_HERE] - Replace with actual agent implementation
9. [AGENT_RESULT] - Replace with what the agent should return
10. [ENV_VARIABLES] - Add environment variables needed for your agent (API keys, secrets, etc.)

## Rules and Requirements:
- NEVER change `{{agent_token}}` - leave it exactly as is
- ALWAYS include `genai-protocol` and `python-dotenv` in dependencies
- USE environment variables for all API keys and secrets via `os.getenv("VARIABLE_NAME")`
- INCLUDE `load_dotenv()` at the top of your agent file
- Use `async/await` for any external API calls
- Add proper error handling where appropriate
- Use `Annotated` types for all function parameters
- Function name must match the name in `@session.bind`
- Add only necessary dependencies to pyproject.toml
- Create appropriate `.env` file with placeholder variables

## Response Format:
Return exactly three code blocks:

agent.py:
```python
[COMPLETE AGENT CODE]
```

pyproject.toml:
```toml
[COMPLETE DEPENDENCIES CONFIGURATION]
```

.env:
```env
[ENVIRONMENT VARIABLES WITH PLACEHOLDERS]
```

Now create an agent based on the user's request:
```

---

## Agent Template System

### Core Template Components

Every generated agent includes these essential components:

1. **Environment Setup** - `.env` file with necessary variables
2. **Dependencies** - `pyproject.toml` with required packages
3. **Main Agent** - `agent.py` with complete implementation
4. **Error Handling** - Proper exception management
5. **Type Safety** - Full type annotations
6. **Documentation** - Clear docstrings and comments

### Standard File Structure
```
agent_project/
├── agent.py              # Main agent implementation
├── pyproject.toml        # Dependencies and project config
├── .env                  # Environment variables (gitignored)
├── .env.example          # Template for environment variables
├── README.md             # Usage instructions (optional)
└── tests/
    └── test_agent.py     # Test file (optional)
```

---

## Enhancement Patterns for Existing Agents

### When to Use Enhancement vs Template Generation

**Use Template Generation when:**
- Starting from scratch
- Need complete project structure
- Want standardized format
- Building production-ready agents

**Use Enhancement Patterns when:**
- Have existing boilerplate code
- Need to add specific functionality
- Working with legacy agents
- Want to understand implementation patterns

### The Enhancement Process

#### Step 1: Analyze Existing Code
```python
# Identify what you have
def analyze_boilerplate(code: str) -> Dict[str, Any]:
    """Analyze existing agent code to understand current state"""
    return {
        "has_imports": bool(re.search(r'import|from', code)),
        "has_session_bind": bool(re.search(r'@session\.bind', code)),
        "has_function": bool(re.search(r'async def|def', code)),
        "has_error_handling": bool(re.search(r'try:|except:', code)),
        "has_validation": bool(re.search(r'validate|check', code)),
        "complexity_level": "basic" if "Hello, World!" in code else "intermediate"
    }
```

#### Step 2: Apply Enhancement Patterns
Choose the appropriate pattern based on agent type and complexity needs.

---

## Universal Generation Prompts

### Primary Generation Prompt (Use First)
```
Create a complete, working AI agent that [DESCRIBE FUNCTIONALITY]. 

Requirements:
- Use the standard template structure
- Include all necessary dependencies
- Add proper error handling
- Use environment variables for secrets
- Return JSON-serializable results
- Include input validation
- Add comprehensive docstrings

The agent should be production-ready and fully functional, not just a placeholder.
```

### Secondary Enhancement Prompts

#### For Data Processing Agents:
```
Enhance this agent to include:
- Input validation and sanitization
- Support for multiple data formats (JSON, CSV, XML)
- Batch processing capabilities
- Progress tracking for long operations
- Data transformation utilities
- Configurable output formats
- Memory-efficient processing for large datasets
```

#### For API Integration Agents:
```
Enhance this agent to include:
- Robust HTTP client with connection pooling
- Retry logic with exponential backoff
- Comprehensive error handling for API failures
- Request/response logging
- Rate limiting compliance
- Authentication handling (API keys, OAuth)
- Response caching where appropriate
```

#### For Workflow/Automation Agents:
```
Enhance this agent to include:
- Step-by-step workflow execution
- Conditional logic and branching
- State persistence between operations
- Rollback capabilities for failed operations
- Parallel execution where possible
- Progress monitoring and reporting
- Integration with external systems
```

---

## Advanced Implementation Patterns

### 1. Robust Error Handling Pattern
```python
import logging
from typing import Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)

class AgentErrorType(str, Enum):
    VALIDATION_ERROR = "validation_error"
    API_ERROR = "api_error"
    PROCESSING_ERROR = "processing_error"
    TIMEOUT_ERROR = "timeout_error"
    RATE_LIMIT_ERROR = "rate_limit_error"

@dataclass
class AgentError(Exception):
    error_type: AgentErrorType
    message: str
    details: Optional[Dict[str, Any]] = None

class ErrorHandler:
    @staticmethod
    def handle_error(error: Exception) -> Dict[str, Any]:
        """Convert exceptions to standardized error responses"""
        if isinstance(error, AgentError):
            return {
                "success": False,
                "error": error.error_type.value,
                "message": error.message,
                "details": error.details or {}
            }
        
        logger.error(f"Unexpected error: {error}", exc_info=True)
        return {
            "success": False,
            "error": "internal_error",
            "message": "An unexpected error occurred",
            "details": {"error_type": type(error).__name__}
        }
```

### 2. Async Processing Engine Pattern
```python
import asyncio
import aiohttp
from typing import List, Any, Callable
from concurrent.futures import ThreadPoolExecutor

class AsyncProcessingEngine:
    def __init__(self, max_concurrent: int = 10, timeout: int = 30):
        self.max_concurrent = max_concurrent
        self.timeout = timeout
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.timeout)
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def process_batch(
        self, 
        items: List[Any], 
        processor: Callable,
        **kwargs
    ) -> List[Dict[str, Any]]:
        """Process items concurrently with semaphore control"""
        semaphore = asyncio.Semaphore(self.max_concurrent)
        
        async def process_with_semaphore(item):
            async with semaphore:
                try:
                    return await processor(item, **kwargs)
                except Exception as e:
                    return ErrorHandler.handle_error(e)
        
        tasks = [process_with_semaphore(item) for item in items]
        return await asyncio.gather(*tasks, return_exceptions=True)
```

### 3. Configuration Management Pattern
```python
import os
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class AgentConfig:
    """Centralized configuration management"""
    api_timeout: int = 30
    max_retries: int = 3
    retry_delay: float = 1.0
    debug_mode: bool = False
    cache_enabled: bool = True
    max_concurrent: int = 10
    
    @classmethod
    def from_env(cls) -> 'AgentConfig':
        """Load configuration from environment variables"""
        return cls(
            api_timeout=int(os.getenv('AGENT_TIMEOUT', '30')),
            max_retries=int(os.getenv('AGENT_MAX_RETRIES', '3')),
            retry_delay=float(os.getenv('AGENT_RETRY_DELAY', '1.0')),
            debug_mode=os.getenv('AGENT_DEBUG', 'false').lower() == 'true',
            cache_enabled=os.getenv('AGENT_CACHE', 'true').lower() == 'true',
            max_concurrent=int(os.getenv('AGENT_MAX_CONCURRENT', '10'))
        )
```

### 4. Response Standardization Pattern
```python
from typing import Any, Dict, List, Optional
from datetime import datetime
import time

class ResponseBuilder:
    """Standardize all agent responses"""
    
    def __init__(self):
        self.start_time = time.time()
    
    def success(
        self, 
        data: Any, 
        message: str = "Operation completed successfully",
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Build success response"""
        return {
            "success": True,
            "message": message,
            "data": data,
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "duration_ms": int((time.time() - self.start_time) * 1000),
                **(metadata or {})
            }
        }
    
    def error(
        self, 
        error_type: str, 
        message: str, 
        details: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Build error response"""
        return {
            "success": False,
            "error": error_type,
            "message": message,
            "details": details or {},
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "duration_ms": int((time.time() - self.start_time) * 1000)
            }
        }
```

---

## Agent Archetypes & Examples

### 1. API Integration Agent
```python
# Complete example for weather agent
import asyncio
import os
import aiohttp
from typing import Annotated, Dict, Any
from dotenv import load_dotenv
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext

load_dotenv()

AGENT_JWT = "{{agent_token}}"
session = GenAISession(jwt_token=AGENT_JWT)

class WeatherService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"
    
    async def get_weather(self, city: str) -> Dict[str, Any]:
        """Fetch weather data for a city"""
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/weather"
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric"
            }
            
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temperature": data["main"]["temp"],
                        "description": data["weather"][0]["description"],
                        "humidity": data["main"]["humidity"],
                        "pressure": data["main"]["pressure"]
                    }
                else:
                    raise Exception(f"Weather API error: {response.status}")

@session.bind(
    name="weather_agent",
    description="Get current weather information for any city"
)
async def weather_agent(
    agent_context: GenAIContext,
    city: Annotated[str, "Name of the city to get weather for"],
) -> Dict[str, Any]:
    """Get current weather information for any city"""
    
    try:
        api_key = os.getenv("OPENWEATHER_API_KEY")
        if not api_key:
            return {
                "success": False,
                "error": "configuration_error",
                "message": "OpenWeather API key not configured"
            }
        
        if not city or not city.strip():
            return {
                "success": False,
                "error": "validation_error",
                "message": "City name is required"
            }
        
        weather_service = WeatherService(api_key)
        weather_data = await weather_service.get_weather(city.strip())
        
        return {
            "success": True,
            "message": f"Weather data retrieved for {city}",
            "data": weather_data,
            "metadata": {
                "source": "OpenWeatherMap",
                "units": "metric"
            }
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "processing_error",
            "message": str(e)
        }

async def main():
    print(f"Weather Agent with token '{AGENT_JWT}' started")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. Data Processing Agent
```python
# Complete example for data analysis agent
import asyncio
import os
import json
import statistics
from typing import Annotated, Dict, Any, List, Union
from dotenv import load_dotenv
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext

load_dotenv()

AGENT_JWT = "{{agent_token}}"
session = GenAISession(jwt_token=AGENT_JWT)

class DataAnalyzer:
    @staticmethod
    def analyze_numeric_data(data: List[Union[int, float]]) -> Dict[str, Any]:
        """Perform statistical analysis on numeric data"""
        if not data:
            raise ValueError("Data list is empty")
        
        return {
            "count": len(data),
            "sum": sum(data),
            "mean": statistics.mean(data),
            "median": statistics.median(data),
            "mode": statistics.mode(data) if len(set(data)) < len(data) else None,
            "std_dev": statistics.stdev(data) if len(data) > 1 else 0,
            "min": min(data),
            "max": max(data),
            "range": max(data) - min(data),
            "quartiles": {
                "q1": statistics.quantiles(data, n=4)[0] if len(data) >= 4 else None,
                "q3": statistics.quantiles(data, n=4)[2] if len(data) >= 4 else None
            }
        }

@session.bind(
    name="data_analysis_agent",
    description="Perform statistical analysis on numeric datasets"
)
async def data_analysis_agent(
    agent_context: GenAIContext,
    data: Annotated[List[Union[int, float]], "List of numeric values to analyze"],
    analysis_type: Annotated[str, "Type of analysis: 'basic', 'detailed', or 'summary'"] = "basic",
) -> Dict[str, Any]:
    """Perform statistical analysis on numeric datasets"""
    
    try:
        # Input validation
        if not isinstance(data, list):
            return {
                "success": False,
                "error": "validation_error",
                "message": "Data must be a list of numbers"
            }
        
        if not data:
            return {
                "success": False,
                "error": "validation_error",
                "message": "Data list cannot be empty"
            }
        
        # Type validation
        numeric_data = []
        for i, value in enumerate(data):
            try:
                numeric_data.append(float(value))
            except (ValueError, TypeError):
                return {
                    "success": False,
                    "error": "validation_error",
                    "message": f"Non-numeric value at index {i}: {value}"
                }
        
        # Perform analysis
        analyzer = DataAnalyzer()
        analysis_result = analyzer.analyze_numeric_data(numeric_data)
        
        # Filter results based on analysis type
        if analysis_type == "summary":
            filtered_result = {
                "count": analysis_result["count"],
                "mean": analysis_result["mean"],
                "median": analysis_result["median"],
                "std_dev": analysis_result["std_dev"]
            }
        elif analysis_type == "detailed":
            filtered_result = analysis_result
        else:  # basic
            filtered_result = {
                "count": analysis_result["count"],
                "mean": analysis_result["mean"],
                "min": analysis_result["min"],
                "max": analysis_result["max"]
            }
        
        return {
            "success": True,
            "message": f"Analysis completed for {len(numeric_data)} data points",
            "data": {
                "analysis": filtered_result,
                "analysis_type": analysis_type,
                "data_summary": {
                    "total_points": len(numeric_data),
                    "data_type": "numeric",
                    "has_duplicates": len(set(numeric_data)) < len(numeric_data)
                }
            }
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": "processing_error",
            "message": f"Analysis failed: {str(e)}"
        }

async def main():
    print(f"Data Analysis Agent with token '{AGENT_JWT}' started")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Testing & Validation

### Comprehensive Test Template
```python
# test_agent.py - Universal test template
import asyncio
import pytest
from unittest.mock import Mock, patch
from agent import [AGENT_FUNCTION_NAME]

class TestAgent:
    """Comprehensive test suite for agent"""
    
    @pytest.fixture
    def mock_context(self):
        """Mock GenAI context"""
        return Mock()
    
    @pytest.mark.asyncio
    async def test_successful_operation(self, mock_context):
        """Test successful agent operation"""
        result = await [AGENT_FUNCTION_NAME](
            agent_context=mock_context,
            # Add appropriate test parameters
        )
        
        assert result["success"] is True
        assert "data" in result
        assert "message" in result
        print(f"✓ Success test passed: {result}")
    
    @pytest.mark.asyncio
    async def test_validation_error(self, mock_context):
        """Test input validation"""
        result = await [AGENT_FUNCTION_NAME](
            agent_context=mock_context,
            # Add invalid parameters
        )
        
        assert result["success"] is False
        assert result["error"] == "validation_error"
        print(f"✓ Validation test passed: {result}")
    
    @pytest.mark.asyncio
    async def test_error_handling(self, mock_context):
        """Test error handling"""
        with patch('[MODULE_TO_PATCH]') as mock_service:
            mock_service.side_effect = Exception("Test error")
            
            result = await [AGENT_FUNCTION_NAME](
                agent_context=mock_context,
                # Add test parameters
            )
            
            assert result["success"] is False
            assert "error" in result
            print(f"✓ Error handling test passed: {result}")

# Simple run script for quick testing
async def quick_test():
    """Quick test runner"""
    mock_context = Mock()
    
    # Test 1: Basic functionality
    result = await [AGENT_FUNCTION_NAME](
        mock_context,
        # Add test parameters
    )
    print("Basic test:", result)
    
    # Test 2: Error case
    result = await [AGENT_FUNCTION_NAME](
        mock_context,
        # Add invalid parameters
    )
    print("Error test:", result)

if __name__ == "__main__":
    asyncio.run(quick_test())
```

---

## Production Deployment

### Deployment Checklist
- [ ] **Environment Variables**: All secrets in `.env` file
- [ ] **Dependencies**: All packages in `pyproject.toml`
- [ ] **Error Handling**: Comprehensive exception management
- [ ] **Input Validation**: All inputs validated
- [ ] **Logging**: Strategic logging for debugging
- [ ] **Testing**: Unit tests and integration tests
- [ ] **Documentation**: Clear usage instructions
- [ ] **Performance**: Async operations where needed
- [ ] **Security**: No hardcoded secrets or credentials
- [ ] **Monitoring**: Health checks and metrics

### Docker Deployment Template
```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install -e .

COPY agent.py .
COPY .env .

CMD ["python", "agent.py"]
```

### Docker Compose Template
```yaml
# docker-compose.yml
version: '3.8'
services:
  agent:
    build: .
    environment:
      - AGENT_JWT={{agent_token}}
    env_file:
      - .env
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "python", "-c", "import requests; requests.get('http://localhost:8000/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
```

---

## Best Practices

### 1. Code Organization
```python
# Recommended file structure for complex agents
agent_project/
├── agent.py                 # Main agent entry point
├── core/
│   ├── __init__.py
│   ├── engine.py           # Core processing logic
│   ├── validators.py       # Input validation
│   ├── exceptions.py       # Custom exceptions
│   └── utils.py           # Utility functions
├── services/
│   ├── __init__.py
│   └── external_api.py    # External service integrations
├── tests/
│   ├── __init__.py
│   ├── test_agent.py      # Main agent tests
│   └── test_core.py       # Core logic tests
├── pyproject.toml
├── .env
├── .env.example
└── README.md
```

### 2. Error Handling Best Practices
```python
# Always use structured error responses
def create_error_response(error_type: str, message: str, details: Dict = None):
    return {
        "success": False,
        "error": error_type,
        "message": message,
        "details": details or {},
        "timestamp": datetime.now().isoformat()
    }

# Common error types to use consistently
ERROR_TYPES = {
    "validation_error": "Input validation failed",
    "configuration_error": "Missing or invalid configuration",
    "api_error": "External API call failed",
    "processing_error": "Internal processing failed",
    "timeout_error": "Operation timed out",
    "rate_limit_error": "Rate limit exceeded"
}
```

### 3. Performance Optimization
```python
# Use connection pooling for HTTP requests
import aiohttp

class HttpClient:
    def __init__(self):
        self.session = None
    
    async def __aenter__(self):
        connector = aiohttp.TCPConnector(limit=100, limit_per_host=30)
        timeout = aiohttp.ClientTimeout(total=30)
        self.session = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
```

### 4. Monitoring and Observability
```python
import logging
import time
from functools import wraps

# Set up structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def monitor_performance(func):
    """Decorator to monitor function performance"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = await func(*args, **kwargs)
            duration = time.time() - start_time
            logger.info(f"{func.__name__} completed in {duration:.2f}s")
            return result
        except Exception as e:
            duration = time.time() - start_time
            logger.error(f"{func.__name__} failed after {duration:.2f}s: {e}")
            raise
    return wrapper
```

---

## Quick Reference Card

### Essential Agent Structure
```python
# Minimum viable agent structure
import asyncio
import os
from typing import Annotated, Dict, Any
from dotenv import load_dotenv
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext

load_dotenv()
AGENT_JWT = "{{agent_token}}"
session = GenAISession(jwt_token=AGENT_JWT)

@session.bind(name="agent_name", description="Agent description")
async def agent_name(
    agent_context: GenAIContext,
    param: Annotated[str, "Parameter description"],
) -> Dict[str, Any]:
    """Agent description"""
    try:
        # Core logic here
        return {
            "success": True,
            "message": "Operation completed",
            "data": {"result": "value"}
        }
    except Exception as e:
        return {
            "success": False,
            "error": "processing_error",
            "message": str(e)
        }

async def main():
    print(f"Agent started")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
```

### Common Dependencies
```toml
# pyproject.toml essentials
[project]
dependencies = [
    "genai-protocol",      # Required
    "python-dotenv>=1.0.0", # Required
    "aiohttp>=3.8.0",      # HTTP requests
    "pydantic>=2.0.0",     # Data validation
    "pytest>=7.0.0",       # Testing
    "pytest-asyncio>=0.21.0", # Async testing
]
```

---

## Conclusion

This enhanced AgentMaker system provides two powerful approaches:

1. **Template-Based Generation**: For rapid creation of production-ready agents with standardized structure
2. **Enhancement Patterns**: For transforming existing boilerplate into fully functional implementations

### Key Benefits:
- **Speed**: Generate working agents in minutes, not hours
- **Quality**: Production-ready code with proper error handling
- **Consistency**: Standardized structure and patterns
- **Maintainability**: Clear documentation and testing frameworks
- **Scalability**: Built-in performance optimizations and monitoring

### Usage Recommendations:
- **Start with templates** for new projects
- **Use enhancement patterns** for existing code
- **Always include** comprehensive error handling
- **Test thoroughly** before deployment
- **Monitor performance** in production

Transform any idea into a working AI agent using these proven patterns and templates! 🚀 