# AI-Powered Currency Converter Agent 💱

A demonstration of LLM **tool-calling and agentic reasoning** — where a language model autonomously decides which APIs to call, in what order, and how to synthesize their results into a final answer. Built around a real-time currency converter as the driving use case, powered by **LangChain** and **HuggingFace** open-source LLMs (`Qwen/Qwen2.5-7B-Instruct`).

---

## 🚀 Key Technologies & Skills Demonstrated

- **Generative AI & LLMs**: LangChain, HuggingFace Inference API
- **Agentic Workflows**: Automated reasoning and multi-step tool execution (`bind_tools`, iterative `tool_calls` parsing).
- **Advanced LangChain Concepts**: Implementation of `InjectedToolArg` to handle hidden parameters safely at runtime without exposing them to the model's generation context.
- **Robust Tool Orchestration**: Two-pass tool execution loop to guarantee dependency ordering — `get_conversion_factor` always resolves before `convert` is invoked, preventing runtime errors on undefined state.
- **API Integration**: RESTful API integration with ExchangeRate-API for live financial data.
- **Python Architecture**: Strong typing with `Annotated`, secure environment variable management via `python-dotenv`, and functional separation of concerns.

---

## 📁 Project Structure

```text
CurrencyConversion/
├── currency_convert.py   # Main agent script: defines tools, initializes LLM, and orchestrates the tool-calling loop.
├── fake_env              # Template for required environment variables — copy to .env, never commit real keys.
└── README.md             # Project documentation and setup guide.
```

---

## 🛠️ How It Works

```text
User Prompt
    │
    ▼
LLM reasons → selects tools → [get_conversion_factor] ──► ExchangeRate API
                                                               │
                                         inject rate ◄─────────┘
                                               │
                                               ▼
                                         [convert] ──► Final Answer
```

1. **User Query**: The user provides a natural language prompt (e.g., *"conversion factor between USD and INR and based on that convert 10 USD to INR"*).
2. **Real-Time Data Fetching**: The LLM intelligently decides to use the `get_conversion_factor` tool to fetch live exchange rates from the ExchangeRate-API.
3. **Dynamic Argument Injection**: The system intercepts the workflow to explicitly inject the retrieved rate into the next tool using LangChain's `InjectedToolArg`. This prevents the LLM from hallucinating mathematical parameters.
4. **Deterministic Calculation**: The agent invokes the `convert` tool to safely and accurately calculate the final converted amount.

> 💡 **Core concept**: `InjectedToolArg` decouples the LLM's *reasoning* about which tools to call from the *runtime values* those tools depend on — a key pattern for building reliable, hallucination-resistant agentic pipelines.

---

## ⚙️ Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install langchain-core langchain-huggingface python-dotenv requests
   ```

2. **Configure environment variables**:
   Copy the `fake_env` file to a `.env` file and populate with your API credentials:
   - `HF_TOKEN`: Your HuggingFace Access Token
   - `RATE_EXCHANGE`: Your ExchangeRate-API Key

3. **Run the application**:
   ```bash
   python currency_convert.py
   # Output: "10 USD = 834.20 INR" (rate varies with live data)
   ```
