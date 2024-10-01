import streamlit as st
import random

# Define a list of questions and answers about LLMs, including multiple choice options
# Each tuple contains a question and a list of possible answers
# The first answer in each list is always the correct one
llm_questions = [
    ("What does LLM stand for?", ["Large Language Model", "Linear Logic Machine", "Linguistic Learning Method", "Long-term Language Memory"]),
    ("Which company developed GPT-3?", ["OpenAI", "Google", "Microsoft", "Facebook"]),
    # ... (other questions)
]

def generate_quiz():
    """
    Generate a quiz by randomly selecting 10 questions from the llm_questions list.
    
    Returns:
    list: A list of 10 randomly selected (question, answers) tuples.
    """
    return random.sample(llm_questions, 10)

def main():
    """
    Main function to run the Streamlit app for the LLM Quiz Generator.
    
    This function handles the app's UI and logic, including:
    - Generating a new quiz
    - Displaying questions and answer options
    - Collecting user responses
    - Scoring the quiz and showing results
    """
    st.title("LLM Quiz Generator")
    
    st.write("Welcome to the LLM Quiz Generator! Click the button below to generate a new quiz.")
    
    # Initialize session state variables if they don't exist
    if 'quiz_generated' not in st.session_state:
        st.session_state.quiz_generated = False
    
    if 'quiz' not in st.session_state:
        st.session_state.quiz = []
    
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}
    
    # Button to generate a new quiz
    if st.button("Generate New Quiz"):
        st.session_state.quiz = generate_quiz()
        st.session_state.quiz_generated = True
        st.session_state.user_answers = {}
    
    # Display the quiz if it has been generated
    if st.session_state.quiz_generated:
        st.subheader("Your LLM Quiz:")
        
        # Iterate through each question in the quiz
        for i, (question, options) in enumerate(st.session_state.quiz, 1):
            st.write(f"{i}. {question}")
            
            # Store the correct answer (always the first in the list)
            correct_answer = options[0]
            
            # Shuffle the options to randomize their order
            shuffled_options = random.sample(options, len(options))
            
            # Create checkboxes for each option and store user's selections
            st.session_state.user_answers[i] = []
            for option in shuffled_options:
                if st.checkbox(option, key=f"q{i}_{option}"):
                    st.session_state.user_answers[i].append(option)
        
        # Button to submit the quiz and see results
        if st.button("Submit Quiz"):
            score = 0
            for i, (question, options) in enumerate(st.session_state.quiz, 1):
                correct_answer = options[0]
                user_answers = st.session_state.user_answers[i]
                
                # Check if the user's answer matches exactly with the correct answer
                if user_answers == [correct_answer]:
                    score += 1
                    st.success(f"Question {i}: Correct!")
                else:
                    st.error(f"Question {i}: Incorrect. The correct answer is: {correct_answer}")
            
            # Display the final score
            st.write(f"Your final score: {score} out of 10")

if __name__ == "__main__":
    main()

