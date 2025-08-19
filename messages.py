from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    HumanMessage("Hi"),
    SystemMessage("YOu're an assistant")
]

print(messages)