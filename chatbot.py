import random

def chatbot():
    print("Bot: Hello! I am your friendly chatbot. Type 'bye' to exit.")

    while True:
        try:
            user_input = input("You: ").lower().strip()

            # IF-ELIF-ELSE logic
            if user_input in ("hello", "hi", "hey"):
                responses = ["Hi there!", "Hello!", "Hey! How can I help?"]
                print("Bot:", random.choice(responses))

            elif user_input in ("how are you", "how r u", "how are u"):
                responses = ["I'm great, thanks!", "Doing well, and you?", "All good here!"]
                print("Bot:", random.choice(responses))

            elif user_input in ("bye", "exit", "quit"):
                responses = ["Goodbye!", "See you later!", "Take care!"]
                print("Bot:", random.choice(responses))
                break

            else:
                print("Bot: Sorry, I don't understand that.")

        except KeyboardInterrupt:
            print("\nBot: Exiting... Goodbye!")
            break

# Run the chatbot
if __name__ == "__main__":
    chatbot()
