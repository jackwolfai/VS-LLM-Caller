from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
        """Useful for performing basic arithmetic operations."""
        print("Tool has been called.")
        return f"The sum of {a} and {b} is {a + b}."
@tool
def greet(name: str) -> str:
        """Useful for greeting a user."""
        print("Greet tool has been called.")
        return f"Hello, {name}! I hope you are well today."

def main():
    model = ChatOpenAI(temperature=0.0, model="gpt-4o")

    tools = [calculator, greet]
    agent_executor = create_react_agent(model, tools)
    
    print("Welcome! I'm your AI assistant. How can I help you today?")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input == "quit":
            print("Goodbye!")
            break
        
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()