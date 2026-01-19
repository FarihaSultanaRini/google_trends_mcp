# Google Trends MCP Server

An MCP server for fetching Google Trends data.

## Installation

### Data Privacy & Security
This package modifies your global Gemini settings to register itself. It does not transmit any data outside of your local machine and Google Trends.

### Automatic Installation (Recommended)

1.  **Install the package:**
    
    ```bash
    pip install git+https://github.com/Startdust12/google-trends-mcp.git
    ```
    *(No need to manually clone the repository)*

2.  **Register with Gemini:**
    
    **Standard (Windows/Linux/Mac):**
    ```bash
    google-trends-mcp install
    ```
    *(Detects `~/.gemini/settings.json` automatically)*

    **Custom Path:**
    If your settings file is in a different location:
    ```bash
    google-trends-mcp install --path /path/to/your/settings.json
    ```

3.  **Restart Gemini CLI**
    The tool `fetch_trending_keywords` should now be available.

## Manual Configuration
If you prefer to configure it manually, add the following to your `settings.json` under `mcpServers`:

```json
"google-trends-mcp": {
  "command": "google-trends-mcp",
  "args": ["run"],
  "env": {}
}
```

## Usage
**Tool:** `fetch_trending_keywords`
- `keyword`: Search term (e.g., "Python")
- `region`: ISO Code (e.g., "US", "IN")
- `days`: Timeframe in days (e.g., 1, 7, 30)
