import streamlit as st
import random

# Define a list of questions and answers about LLMs, including multiple choice options
llm_questions = [
    ("What does LLM stand for?", ["Large Language Model", "Linear Logic Machine", "Linguistic Learning Method", "Long-term Language Memory"]),
    ("Which company developed GPT-3?", ["OpenAI", "Google", "Microsoft", "Facebook"]),
    ("What is the main purpose of an LLM?", ["To generate human-like text based on input", "To analyze images", "To create music", "To play chess"]),
    ("What type of AI architecture are most LLMs based on?", ["Transformer", "Convolutional Neural Network", "Recurrent Neural Network", "Support Vector Machine"]),
    ("What is 'few-shot learning' in the context of LLMs?", ["The ability to perform a task with only a few examples", "Learning from a large dataset", "Training on a single example", "Continuous learning without examples"]),
    ("Which LLM is known for its ability to generate images from text descriptions?", ["DALL-E", "GPT-3", "BERT", "T5"]),
    ("What is 'prompt engineering' in relation to LLMs?", ["The practice of designing effective input prompts to get desired outputs", "Creating hardware for LLMs", "Developing new training algorithms", "Optimizing model architecture"]),
    ("What potential ethical concern is associated with LLMs?", ["Bias in generated content", "Excessive energy consumption", "Physical robot control", "Time travel paradoxes"]),
    ("Which company developed the LLM called 'LaMDA'?", ["Google", "OpenAI", "Microsoft", "Amazon"]),
    ("What is 'fine-tuning' in the context of LLMs?", ["Adapting a pre-trained model to a specific task or domain", "Adjusting the hardware for better performance", "Creating a new model from scratch", "Reducing the model size"]),
    ("What is 'tokenization' in NLP and LLMs?", ["The process of breaking text into smaller units or tokens", "Encrypting the model's parameters", "Converting text to binary", "Translating text between languages"]),
    ("Which LLM is known for its conversational abilities and was developed by Anthropic?", ["Claude", "GPT-4", "BERT", "XLNet"]),
]

def generate_quiz():
    return random.sample(llm_questions, 10)

def main():
    st.title("LLM Quiz Generator")
    
    st.write("Welcome to the LLM Quiz Generator! Click the button below to generate a new quiz.")
    
    if 'quiz_generated' not in st.session_state:
        st.session_state.quiz_generated = False
    
    if 'quiz' not in st.session_state:
        st.session_state.quiz = []
    
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}
    
    if st.button("Generate New Quiz"):
        st.session_state.quiz = generate_quiz()
        st.session_state.quiz_generated = True
        st.session_state.user_answers = {}
    
    if st.session_state.quiz_generated:
        st.subheader("Your LLM Quiz:")
        
        for i, (question, options) in enumerate(st.session_state.quiz, 1):
            st.write(f"{i}. {question}")
            
            # Store the correct answer
            correct_answer = options[0]
            
            # Shuffle the options
            shuffled_options = random.sample(options, len(options))
            
            # Create checkboxes for each option
            st.session_state.user_answers[i] = []
            for option in shuffled_options:
                if st.checkbox(option, key=f"q{i}_{option}"):
                    st.session_state.user_answers[i].append(option)
        
        if st.button("Submit Quiz"):
            score = 0
            for i, (question, options) in enumerate(st.session_state.quiz, 1):
                correct_answer = options[0]
                user_answers = st.session_state.user_answers[i]
                
                if user_answers == [correct_answer]:
                    score += 1
                    st.success(f"Question {i}: Correct!")
                else:
                    st.error(f"Question {i}: Incorrect. The correct answer is: {correct_answer}")
            
            st.write(f"Your final score: {score} out of 10")

if __name__ == "__main__":
    main()

