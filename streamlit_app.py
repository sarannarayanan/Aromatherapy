import streamlit as st
import datetime
import os
import sys
from streamlit_js_eval import streamlit_js_eval


def get_scent_suggestion(mood):
    scent_suggestions = {
        "happy": "Lemon – Bright and refreshing 🍋",
        "sad": "Lavender – Calming and soothing 🌸",
        "angry": "Chamomile – Helps calm emotions 🌼",
        "stressed": "Peppermint – Refreshing and energizing 🌿",
        "tired": "Eucalyptus – Awakens the senses 🌱",
        "bored": "Jasmine – Uplifts and inspires 🌼",
        "anxious": "Rose – Comforting and balancing 🌹",
        "confused": "Sandalwood – Grounds and centers 🌳",
        "sick": "Tea Tree Oil – Helps with acne, athlete’s foot, and boosts immunity 🌿"
    }
    return scent_suggestions.get(mood.lower(), "Sorry, we don't have a suggestion for that mood yet!")

def main():
    st.title("🌿✨ Aromatherapy Mood Matcher ✨🌿")
    st.write("Let's find the perfect scent to match your mood!")

    questions = [
        "Do you feel energetic and ready to take on the day?",
        "Are you currently experiencing feelings of stress or being overwhelmed?",
        "Have you noticed that you’ve been feeling sad or down lately?",
        "Do you find it challenging to concentrate on tasks or make decisions?",
        "Are you feeling calm and content with your current situation?"
    ]
    
    responses = []
    for question in questions:
        response = st.radio(question, ("Yes", "No"), key=question,index=None)
        responses.append(response)

    if st.button("Get Scent Suggestion"):
        mood = ""
        if responses[0] == "Yes" and responses[4] == "Yes":
            mood = "happy"
        elif responses[1] == "Yes":
            mood = "stressed"
        elif responses[2] == "Yes":
            mood = "sad"
        elif responses[3] == "Yes":
            mood = "confused"
        elif responses[0] == "No" and responses[2] == "Yes":
            mood = "anxious"
        else:
            mood = "bored"

        suggestion = get_scent_suggestion(mood)
        
        st.write("🌸 Your Aromatherapy Suggestion 🌸")
        st.write("--------------------------------")
        st.write(f"Mood: {mood.capitalize()}")
        st.write(f"Scent: {suggestion}\n")

        st.write("💡 Disclaimer:")
        st.write("The aromatherapy used for influencing mental health, emotions, uplifting mood, and reducing stress is an alternative and complementary therapy. It cannot be used to treat chronic or acute diseases, allergies, or medical conditions.")

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f"🕒 Suggestion generated on: {current_time}\n")

        with open("aromatherapy_log.txt", "a", encoding="utf-8") as file:
            file.write(f"\nTime: {current_time}\n")
            file.write(f"Mood: {mood.capitalize()}\n")
            file.write(f"Scent: {suggestion}\n")
            file.write("Disclaimer: The aromatherapy used for influencing mental health, emotions, uplifting mood, and reducing stress is an alternative and complementary therapy. It is not a cure for chronic or acute diseases, allergies, or medical conditions.\n")
            file.write("-" * 60 + "\n")
    

def respond():
        satisfaction = st.radio("Did you like the suggestion?", ("Yes", "No"),index=None)
        if satisfaction == "No":
            st.write("🌟 Let's upgrade your experience! Try combining your scent with meditation, soft music, or a gratitude journal for extra positivity 💖")
        elif satisfaction=="Yes":
            st.write("We are glad that we found the perfect scent to elevate your mood! Have a nice day!💖")
            

        try_again = st.radio("Would you like to try again?", ("Yes", "No"),index=None)
        if try_again == "No":
           st.write("🌺 Thank you for using the Aromatherapy Mood Matcher! Remember — small moments of calm can make a big difference. 🌞")
        elif try_again == "Yes":
           streamlit_js_eval(js_expressions="parent.window.location.reload()")
            #   st.rerun()
    
    

    
        
           
            

if __name__ == "__main__":
    main()
    respond()
    
