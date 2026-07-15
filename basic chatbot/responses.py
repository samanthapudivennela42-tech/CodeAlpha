def get_response(user_input):
    text = user_input.lower()

    responses = {
        "hello": "Hello! How can I help you?",
        "hi": "Hi there!",
        "how are you": "I'm doing great. Thanks for asking!",
        "what is your name": "I'm a simple Python chatbot.",
        "bye": "Goodbye! Have a nice day!",
        "help": "You can ask me simple questions.",
        "venni": "Hello Venni ! Nice to meet you. 😊"
"
    }

    for key in responses:
        if key in text:
            return responses[key]

    return "Sorry, I don't understand that."