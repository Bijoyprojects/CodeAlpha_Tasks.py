def rule_based_chatbot():
    """
    A simple rule-based chatbot that responds to user greetings,
    status inquiries, and exit commands.
    """
    print("Chatbot: Hello! I am your assistant. (Type 'bye' to exit)")
    
    # 1. Loop to keep the conversation running continuously
    while True:
        # 2. Input/Output to receive user text and clean it
        user_input = input("You: ").strip().lower()
        
        # 3. If-Elif-Else structure to manage predefined rules
        if user_input == "hello":
            print("Chatbot: Hi!")
            
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
            
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  # Exits the continuous loop
            
        else:
            print("Chatbot: I am sorry, I do not understand that command.")

# 4. Function call to execute the chatbot program
if __name__ == "__main__":
    rule_based_chatbot()