# 🔐 Cybersecurity Newsletter Editor Agent

A Bindu agent that researches the latest cybersecurity threats, CVEs, and security news, then drafts a professional newsletter section in Markdown — ready to publish.

## What It Does

Given a topic or free-form request, the agent:

1. **Searches the web** for the latest cybersecurity news, CVEs, and threat intelligence
2. **Synthesizes findings** into a structured newsletter with four sections
3. **Returns clean Markdown** ready to paste into your newsletter tool

### Output Format

```
# 🔐 Cybersecurity Newsletter — [Topic/Date]

## 🔥 Top Threats This Week
## 🛡️ CVE Spotlight
## 📰 News Digest
## ✅ Recommendations
```

## Prerequisites

- Python 3.12+
- [UV package manager](https://github.com/astral-sh/uv)
- [OpenRouter API key](https://openrouter.ai/) (free tier available)

## Setup

```bash
# 1. Clone the repo and install dependencies
git clone https://github.com/getbindu/Bindu.git
cd Bindu
uv sync --dev

# 2. Set up environment variables
cp examples/cybersecurity-newsletter/.env.example examples/cybersecurity-newsletter/.env
# Edit .env and add your OPENROUTER_API_KEY

# 3. Run the agent
uv run examples/cybersecurity-newsletter/cybersecurity_newsletter_agent.py
```

Agent starts at `http://localhost:3773`

## Example Prompts

| Prompt                                                      | What You Get                                                              |
| ----------------------------------------------------------- | ------------------------------------------------------------------------- |
| `"Write a cybersecurity newsletter for this week"`          | Full newsletter covering top threats, CVEs, and news from the past 7 days |
| `"Summarize the latest ransomware threats"`                 | Focused newsletter section on ransomware campaigns                        |
| `"Create a CVE spotlight for recent Linux vulnerabilities"` | Deep-dive on Linux CVEs with patch status                                 |
| `"Write a newsletter about recent data breaches"`           | Breach-focused edition with affected organizations and data types         |

## Testing

### Via curl

```bash
# Send a message
curl --location 'http://localhost:3773/' \
--header 'Content-Type: application/json' \
--data '{
    "jsonrpc": "2.0",
    "method": "message/send",
    "params": {
        "message": {
            "role": "user",
            "parts": [{"kind": "text", "text": "Write a cybersecurity newsletter for this week"}],
            "kind": "message",
            "messageId": "msg-001",
            "contextId": "ctx-001",
            "taskId": "task-001"
        },
        "configuration": {"acceptedOutputModes": ["application/json"]}
    },
    "id": "req-001"
}'

# Check the result
curl --location 'http://localhost:3773/' \
--header 'Content-Type: application/json' \
--data '{
    "jsonrpc": "2.0",
    "method": "tasks/get",
    "params": {"taskId": "task-001"},
    "id": "req-002"
}'
```

### Via Frontend UI

```bash
cd frontend
npm run dev
# Open http://localhost:5173
```

## Environment Variables

| Variable             | Required | Description                                |
| -------------------- | -------- | ------------------------------------------ |
| `OPENROUTER_API_KEY` | ✅ Yes   | Your OpenRouter API key                    |
| `STORAGE_TYPE`       | No       | `postgres` or `memory` (default: `memory`) |
| `DATABASE_URL`       | No       | PostgreSQL connection URL                  |
| `SCHEDULER_TYPE`     | No       | `redis` or `memory` (default: `memory`)    |
| `REDIS_URL`          | No       | Redis connection URL                       |

## How It Works

```
User Prompt
    ↓
Bindu (A2A Protocol)
    ↓
Agno Agent
    ├── DuckDuckGo Search (live web search for current threats/CVEs)
    └── OpenRouter LLM (gpt-oss-120b for synthesis and writing)
    ↓
Structured Newsletter (Markdown)
```

The agent uses **DuckDuckGo** for live web search — no additional API keys needed beyond OpenRouter. It searches for current events before writing, so the newsletter always reflects the latest threat landscape.

## Contributing

See the [Bindu Contributing Guide](../../.github/contributing.md).
