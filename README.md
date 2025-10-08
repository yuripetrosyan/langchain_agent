## LangChain “ai_agent”


- Loads environment variables with `python-dotenv` and spins up `ChatOpenAI` (`gpt-5-nano`) as the default LLM.
- Registers three tools: DuckDuckGo search, Wikipedia lookup, and a saver that drops structured responses into `outputs/research_output.txt`.
- Prompts the agent for a topic, lets LangChain route tool calls, parses the model output into a Pydantic schema, then writes the final JSON to disk.
- Works entirely from the CLI, so it’s easy to demo or extend.

### Run it
```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # add your OpenAI key or other creds
python main.py
```

You’ll be asked what you want to research. After the agent finishes, check `outputs/` for the saved report.
