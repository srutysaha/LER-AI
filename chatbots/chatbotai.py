from transformers import pipeline

# Load the text2text generation pipeline with FLAN-T5 model
chatbot_pipe = pipeline("text2text-generation", model="google/flan-t5-large")

print("Hello I am Emerald - Your Chatbot friend 🤖 Let's Start Talking!")
print("Say bye to exit the conversation anytime")

while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() == "bye":
        print("👋 Goodbye! Have a great day!")
        break
    
    # Generate chatbot response using FLAN-T5
    response = chatbot_pipe(f"Answer as a chatbot: {user_input}", max_length=100, num_return_sequences=1)
    
    # Extract and print generated text
    bot_response = response[0]["generated_text"]
    print(f"Emerald 🤖: {bot_response}\n")
