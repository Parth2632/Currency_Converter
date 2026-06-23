# AI-Powered Currency Converter Agent 💱

An intelligent, agent-based currency conversion tool powered by **LangChain** and **HuggingFace** open-source Large Language Models (`Qwen/Qwen2.5-7B-Instruct`). This project demonstrates advanced LLM tool-calling capabilities, including real-time API integration and dynamic argument injection.

## 🚀 Key Technologies & Skills Demonstrated
- **Generative AI & LLMs**: LangChain, HuggingFace Inference API
- **Agentic Workflows**: Automated reasoning and multi-step tool execution (`bind_tools`, iterative `tool_calls` parsing).
- **Advanced LangChain Concepts**: Implementation of `InjectedToolArg` to handle hidden parameters safely at runtime without exposing them to the model's generation context.
- **API Integration**: RESTful API integration with ExchangeRate-API for live financial data.
- **Python Architecture**: Strong typing with `Annotated`, secure environment variable management via `python-dotenv`, and functional separation of concerns.

## 📁 Project Structure

```text
CurrencyConversion/
├── currency_convert.py   # Main agent script: defines tools, initializes LLM, and orchestrates the tool-calling loop.
├── fake_env              # Template for required environment variables (API keys and tokens).
└── README.md             # Project documentation and setup guide.
```

## 🛠️ How It Works
1. **User Query**: The user provides a natural language prompt (e.g., *"conversion factor between USD and INR and based on that convert 10 USD to INR"*).
2. **Real-Time Data Fetching**: The LLM intelligently decides to use the `get_conversion_factor` tool to fetch live exchange rates from the ExchangeRate-API.
3. **Dynamic Argument Injection**: The system intercepts the workflow to explicitly inject the retrieved rate into the next tool using LangChain's `InjectedToolArg`. This prevents the LLM from hallucinating mathematical parameters.
4. **Deterministic Calculation**: The agent invokes the `convert` tool to safely and accurately calculate the final converted currency amount.

## ⚙️ Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install langchain-core langchain-huggingface python-dotenv requests
   ```

2. **Configure environment variables**:
   Copy the `fake_env` file to a `.env` file and insert your API credentials:
   - `HF_TOKEN`: Your HuggingFace Access Token
   - `RATE_EXCHANGE`: Your ExchangeRate-API Key

3. **Run the application**:
   ```bash
   python currency_convert.py
   ```
