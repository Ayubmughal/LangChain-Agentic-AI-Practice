from langchain.memory import ConversationSummaryMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

# This memory requires an LLM to perform the summarization
summary_memory = ConversationSummaryMemory(llm=llm)

# Simulating long-form input
summary_memory.save_context(
    {"input": "We are discussing Human-Computer Interaction assignments."}, 
    {"output": "I can help with the Airbnb case study analysis."}
)

# Checking the memory
print(summary_memory.load_memory_variables({}))
# Output will be a summary like: "The human and AI are discussing HCI assignments and Airbnb."
