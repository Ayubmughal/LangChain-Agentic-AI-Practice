from langchain.memory import ConversationBufferWindowMemory

# k=1 means it only remembers the 1 most recent interaction (1 Human + 1 AI)
window_memory = ConversationBufferWindowMemory(k=1)

# Simulating a conversation
window_memory.save_context({"input": "I run a hardware shop."}, {"output": "That's great, Ayub!"})
window_memory.save_context({"input": "It is called Perfect Hardware."}, {"output": "Got it."})

# If we load memory variables now:
print(window_memory.load_memory_variables({}))
# Output will NOT show the first message about the hardware shop because k=1
