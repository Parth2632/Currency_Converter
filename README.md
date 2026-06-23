# Currency Converter with LangChain and HuggingFace

This project demonstrates how to use LangChain's tool-calling capabilities with a HuggingFace open-source LLM (`Qwen/Qwen2.5-7B-Instruct`). It acts as a currency converter by fetching real-time exchange rates and applying mathematical operations through agent tools.

## Features
- **LangChain Tool Calling**: Leverages LangChain's `@tool` decorator to define custom tools.
- **HuggingFace Integration**: Connects to the HuggingFace Hub to use `Qwen/Qwen2.5-7B-Instruct`.
- **Injected Tool Arguments**: Demonstrates advanced tool calling by injecting the `conversion_rate` argument at runtime without exposing it to the LLM.
- **Real-time Rates**: Uses [ExchangeRate-API](https://www.exchangerate-api.com/) for up-to-date currency conversion.

## Setup

1. Install dependencies:
   ```bash
   pip install langchain-core langchain-huggingface python-dotenv requests
   ```

2. Configure environment variables:
   Copy the `fake_env` file to `.env` and fill in your API keys:
   ```bash
   cp fake_env .env
   ```

3. Run the script:
   ```bash
   python currency_convert.py
   ```
