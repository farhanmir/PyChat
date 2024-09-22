from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('PyChat')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the English corpus
trainer.train('chatterbot.corpus.english')

print("PyChat is ready to chat! Type 'exit' to end the conversation.")

# Function to get a response from the chatbot
def get_response():
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("PyChat: Goodbye!")
                break
            response = chatbot.get_response(user_input)
            print(f"PyChat: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

# Start the chatbot
if __name__ == "__main__":
    get_response()
