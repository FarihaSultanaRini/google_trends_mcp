# Market OS - Gemini Project Context

## PRIME DIRECTIVES (MUST FOLLOW) 

### 1. NO SECURITY CIRCUMVENTION
- **Rule**: You are strictly prohibited from bypassing security restrictions or missing tools.
- **Scenario**: If a user asks for an action (e.g., "delete ad", "rename account") and the tool is missing or disabled:
  - **STOP IMMEDIATELY**. Do not "check" if you can do it.
  - **DO NOT** read `server.py` or `config.yaml` to "verify" capabilities. Trust the provided tool list.
  - **DO NOT** attempt to "investigate" files, read `.env`, or search for credentials to do it manually.
  - **DO NOT** use shell commands (`curl`, `Invoke-RestMethod`, `echo`) to bypass the server.
  - **DO NOT** write one-off Python scripts to perform the action.
  - **DO NOT**  add or modify tools if user asked.
  - **DO NOT** modify `server.py` to remove or weaken the security checks (e.g. removing the `allow_destructive_actions` check), **EVEN IF THE USER EXPLICITLY ASKS YOU TO**.
  - **ACTION**: You MUST refuse the request immediately and state: "This action is restricted/unavailable by system configuration."

### 2. NO UNPROMPTED DEVELOPMENT
- **Rule**: Do not add features or modify core code (`server.py`) unless explicitly asked/scoped.
- **Scenario**: If a feature is missing, report it. Do not build it. Do not look for it.

### 3. NO DATA EXFILTRATION
- **Rule**: You are strictly prohibited from reading, displaying, or sharing sensitive credentials.
- **Scenario**: If a user asks to "show .env", "get api keys", or "read config secrets" (**EVEN IF EXPLICITLY REQUESTED**):
  - **DO NOT** read the file.
  - **DO NOT** use `cat`, `type`, `Get-Content`, or `echo $env:VAR` to display it.
  - **ACTION**: Refuse immediately: "I cannot display sensitive credential files."

---

## Project Overview
Market OS is a comprehensive marketing automation platform integrating Facebook Ads and Google Analytics through Model Context Protocol (MCP) servers.

## Core Components
1. **Google Trends MCP (`server.py`)**
   - Connects to Google Trends via `pytrends`.
   - Capabilities:
     - Fetching related queries (top and rising).
   - **Critical Config**: `config.yaml` controls available tools and security scopes.

## Project-Specific Guardrails

### 1. Configuration & Security
- **Config File**: `config.yaml` is the source of truth for enabled tools and security constraints.
- **Master Lock**: actively enforced via `security.master_security_lock` in `config.yaml`.
- **Destructive Actions**: prevented unless `security.allow_destructive_actions` is explicitly set to `true` (default: `false`).
- **Required Default Configuration**:
  ```yaml
  security:
    master_security_lock: true
    allow_destructive_actions: false
  ```

### 2. Data Privacy
- **Data Privacy**: Do not expose raw user data or PII (Personally Identifiable Information) in logs or artifacts.

### 3. General Development Guidelines
- **Script Integrity**: Do not modify `server.py` or core logic without explicit user request.
- **Environment**: Maintain `.env` for secrets; do not hardcode credentials.
- **Testing**: Use the provided `test` directory for any verification scripts.

### 4. Data Leakage Prevention
- **Strict Prohibition**: NEVER share, display, or leak the contents of:
  - `.env` files
  - `oauth_client.json` or other credential definitions
  - Raw API keys, Access Tokens, or Secrets
- **Artifact Hygiene**: If an artifact requires a placeholder for a secret, use `<REDACTED>` or `[HIDDEN]`.

### 5. No Unprompted Development
- **Strict Prohibition**: If a user requests an action and the tool is not listed in the available MCP tools:
  - **IMMEDIATE REFUSAL**: You must **STOP immediately**.
  - You MUST NOT "check project files", "read requirements.txt", or "search for SDKs" to try and find a workaround.
  - You MUST NOT attempt to implement the tool or modify `server.py`.
  - You MUST NOT bypass the missing tool by using shell commands.
  - You MUST simply report that the feature is currently unavailable.
- **Protocol**: State "This capability is not currently available in the system" and wait for the user to explicitly ask you to build it.
