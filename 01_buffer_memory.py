from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o")
memory = ConversationBufferMemory()
template = """You are a helpful assistant.
Current conversation:
{history}
Human: {input}
AI:"""

prompt = PromptTemplate(input_variables=["history", "input"], template=template)

# Connect everything in a Chain
conversation = LLMChain(llm=llm, prompt=prompt, memory=memory)

# Usage
print(conversation.predict(input="Hi, my name is Muhammad Ayub."))
print(conversation.predict(input="What is my name?"))
