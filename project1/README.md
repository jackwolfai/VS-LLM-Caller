# 🤖 LangGraph AI Assistant

A terminal-based AI assistant using **LangGraph**, **LangChain**, and **OpenAI's GPT-4o**.

---

## 🗂️ Project Structure

project1/
- .env # Your OpenAI API key goes here
- .venv/ # Required Python virtual environment
- main.py # Core assistant script
- requirements.txt # Optional if using UV for dependency management
---

## 🚀 Getting Started

### 🔧 1. Clone the Repository

```bash
git clone <your-repo-url>
cd project1
```


### 🔧 2. Create a Virtual Environment
#### Important: The virtual environment must be named .venv & and found it only worked with Python 3.11+
```bash
python3 -m venv .venv # to create

source .venv/bin/activate  # to activate

# On Windows:
# .venv\Scripts\activate
```
### 📦 3. Install Dependencies with UV
#### This project uses uv, not pip.

```bash
uv add langchain-openai langgraph langchain python-dotenv 
```
### 🔐 4. Create Your .env File
#### Create a file named .env in the project root with your OpenAI key:

```bash
OPENAI_API_KEY=your-openai-key-here
```

### ▶️ 5. Run the Assistant

```bash
uv run main.py
```
#### what you'll see:

```bash
Welcome! I'm your AI assistant. How can I help you today?
```
Type your message and get streaming responses.

### 🧪 Quick Test Prompt
After setup, run:
```bash
uv run main.py
```
Ask anything:
```bash
What's the capital of Japan?
```
It should respond with a streamed answer like:
```bash
Assistant: Tokyo
```
To quit, type:
```bash
quit
```
## 🧠 Full Source: main.py
```bash
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def main():
    if "OPENAI_API_KEY" not in os.environ:
        raise ValueError("OPENAI_API_KEY is missing from your environment variables.")

    model = ChatOpenAI(temperature=0.0, model="gpt-4o")
    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm your AI assistant. How can I help you today?")

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["quit", "exit"]:
                print("Goodbye!")
                break

            print("\nAssistant: ", end="")
            for chunk in agent_executor.stream({"messages": [HumanMessage(content=user_input)]}):
                agent_data = chunk.get("agent", {})
                for message in agent_data.get("messages", []):
                    print(message.content, end="")
            print()

        except Exception as e:
            print(f"\n[Error] {e}")

if __name__ == "__main__":
    main()
```

### ⚠️ Notes & Gotchas
✅ The .venv folder must be used (don't use global or system Python).

✅ The .env file is required and must include a valid OPENAI_API_KEY.

⚠️ The assistant uses uv run, not standard Python scripts like python main.py.
