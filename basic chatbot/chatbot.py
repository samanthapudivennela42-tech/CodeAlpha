from responses import get_response

def main():
    print("=" * 40)
    print("🤖 Welcome to Basic Chatbot")
    print("Type 'exit' to quit.")
    print("=" * 40)

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break

        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()