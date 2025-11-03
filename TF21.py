# f1.py
import streamlit as st
import datetime
import random


# --- CONSTANTS ---

# Centralizing questions makes the chatbot function cleaner.
QUESTIONS = [
    "1. Do your friends come to you for advice?",
    "2. What do you think about your appearance?",
    "3. How do you find yourself in doing physical work?",
    "4. How do you find your temperament?",
    "5. How do you like school studies?",
    "6. Do you believe in religious customs and traditions?",
    "7. Do you participate in criticizing others?",
    "8. Do you express your ideas frankly in the presence of others?",
    "9. How do you like your complexion?",
    "10. Do you think of yourself as cheerful?",
    "11. Do you behave abnormally also?",
    "12. Do you think yourself an experienced person?",
    "13. Do you think about your teachers?",
    "14. Do you think yourself to be a cool-tempered person?",
    "15. Are you regular in doing your homework assignments?",
    "16. Do you insult others?",
    "17. Do you have difficulty in understanding something when the teacher explains it in class?",
    "18. Do you think if you get an opportunity you can discover something new?",
    "19. Do you feel irritated if somebody finds fault with your work?",
    "20. How do you find your personality?",
    "21. How do you like the company of others?",
    "22. How much are you satisfied with your weight?",
    "23. Do you feel irritated while you face petty difficulties?",
    "24. How much are you satisfied with the present position of your studies in class?",
    "25. How do you like school examinations?",
    "26. How is your voice?",
    "27. Do you take care of the merits and demerits of a work before doing it?",
    "28. Where do you place yourself while speaking truth?",
    "29. Where do you place yourself in obeying public rules?",
    "30. Are you more intelligent than your colleagues?",
    "31. Do you take part in organizing it when your classmates go to a picnic?",
    "32. What will you do if you are doing some important work and your friends ask you to accompany them for a walk?",
    "33. While taking an examination you are not able to answer some questions and a book of the same subject is lying near you, will you take help of the book?",
    "34. If you get an opportunity to drink water in the house of so-called low-caste persons, what will you do?",
    "35. Do you hesitate in mixing with persons of the opposite sex?",
    "36. You are standing in the bus queue for a long time when the bus comes, the conductor takes some passengers and stops at your turn because there is no space in the bus, what will you do?"
]

# Storing advice and quotes in a central dictionary improves organization.
ADVICE_AND_QUOTES = {
    "Physical": {
        "negative": "Start with light activities like walking or yoga to build confidence in your physical abilities.",
        "neutral": "You're doing well physically; try adding variety like resistance training to keep progressing.",
        "positive": "Awesome physical confidence! Keep pushing your limits with challenging workouts.",
        "quotes": [
            "The body achieves what the mind believes.",
            "Strength does not come from physical capacity. It comes from an indomitable will. - Mahatma Gandhi",
            "Take care of your body. It's the only place you have to live. - Jim Rohn"
        ]
    },
    "Social": {
        "negative": "Join a group activity or fitness class to boost social confidence.",
        "neutral": "Your social skills are solid; try initiating conversations to build stronger connections.",
        "positive": "You're a social star! Keep fostering those relationships.",
        "quotes": [
            "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
            "Surround yourself with only people who are going to lift you higher. - Oprah Winfrey",
            "Friendship is born at that moment when one person says to another: 'What! You too? I thought I was the only one.' - C.S. Lewis"
        ]
    },
    "Temperamental": {
        "negative": "Practice deep breathing or meditation to manage stress and improve your temperament.",
        "neutral": "Your temperament is balanced; mindfulness can help maintain that calm.",
        "positive": "Your cool-headedness is inspiring! Keep it up.",
        "quotes": [
            "Patience is not the ability to wait, but the ability to keep a good attitude while waiting.",
            "He who controls others may be powerful, but he who has mastered himself is mightier still. - Lao Tzu",
            "The greatest remedy for anger is delay. - Seneca"
        ]
    },
    "Educational": {
        "negative": "Set small, achievable study goals to boost your confidence in learning.",
        "neutral": "You're on a good path educationally; try new study techniques to enhance progress.",
        "positive": "Your love for learning is fantastic! Keep exploring new knowledge.",
        "quotes": [
            "Education is the most powerful weapon which you can use to change the world. - Nelson Mandela",
            "The beautiful thing about learning is that no one can take it away from you. - B.B. King",
            "An investment in knowledge pays the best interest. - Benjamin Franklin"
        ]
    },
    "Moral": {
        "negative": "Reflect on your core values to guide your actions more consistently.",
        "neutral": "Your moral compass is steady; keep making ethical choices.",
        "positive": "Your integrity shines! Continue being a role model.",
        "quotes": [
            "Integrity is doing the right thing, even when no one is watching. - C.S. Lewis",
            "The time is always right to do what is right. - Martin Luther King Jr.",
            "Honesty is the first chapter in the book of wisdom. - Thomas Jefferson"
        ]
    },
    "Intellectual": {
        "negative": "Stimulate your mind with puzzles, books, or new skills to boost intellectual confidence.",
        "neutral": "Your intellectual curiosity is great; challenge yourself with complex problems.",
        "positive": "Your intellect is thriving! Keep exploring new ideas.",
        "quotes": [
            "The mind is not a vessel to be filled but a fire to be kindled. - Plutarch",
            "Intelligence is the ability to adapt to change. - Stephen Hawking",
            "The true sign of intelligence is not knowledge but imagination. - Albert Einstein"
        ]
    }
}


# --- SURVEY & ANALYSIS FUNCTIONS ---

def run_chatbot():
    """
    Manages the state and display of the survey questions.
    Returns a list of responses when the survey is complete, otherwise returns None.
    """
    if 'survey_state' not in st.session_state:
        st.session_state.survey_state = {
            'responses': [],
            'current_question': 0
        }

    state = st.session_state.survey_state
    
    if state['current_question'] < len(QUESTIONS):
        idx = state['current_question']
        st.write(f"**Question {idx + 1}/{len(QUESTIONS)}**")
        st.write(f"👉 {QUESTIONS[idx]}")
        st.write("*(Please rate on a scale of 1 to 5)*")

        # Use columns for a cleaner button layout
        cols = st.columns(6)
        chosen_option = None
        for i, val in enumerate([1, 2, 3, 4, 5]):
            if cols[i].button(str(val), key=f"ans_{idx}_{val}"):
                chosen_option = val
        
        # Back button logic
        if cols[5].button("⬅️ Back", key=f"back_{idx}"):
            if state['current_question'] > 0:
                state['current_question'] -= 1
                if state['responses']:
                    state['responses'].pop()
                st.rerun()

        if chosen_option is not None:
            state['responses'].append(int(chosen_option))
            state['current_question'] += 1
            st.rerun()
            
        return None # Survey is still in progress
    else:
        st.success("✅ Survey complete! Thanks for participating!")
        final_responses = state['responses']
        # Reset for next time
        del st.session_state.survey_state
        return final_responses

def analyze_sentiment(category_responses):
    """Calculates the sentiment based on the sum of responses for a category."""
    category_sum = sum(category_responses)
    if category_sum < 18:
        return "negative", category_sum
    elif category_sum == 18:
        return "neutral", category_sum
    else:
        return "positive", category_sum

def get_score_commentary(score):
    """Provides a detailed comment based on the total self-image score."""
    if score <= 64:
        return """
        <div style="background-color: #FFD2D2; padding: 10px; border-radius: 5px;">
        <strong>Needs Attention:</strong> Your score suggests you may be experiencing a period of significant self-doubt across several areas. It's important to acknowledge these feelings without judgment. This is a starting point for growth. Consider focusing on small, achievable goals in one area, like taking a short walk each day (Physical) or reaching out to one friend (Social), to begin building momentum. Remember to be kind to yourself during this process.
        </div>
        """
    elif score <= 93:
        return """
        <div style="background-color: #FFE9D2; padding: 10px; border-radius: 5px;">
        <strong>Room for Growth:</strong> Your responses indicate some areas of confidence mixed with others where you feel less secure. This is quite common. Try to identify the specific areas where you feel less positive and explore the reasons behind them. The advice in the sections above can provide targeted strategies. Celebrating small wins can be a powerful way to start shifting your overall perspective.
        </div>
        """
    elif score <= 122:
        return """
        <div style="background-color: #D2EFFF; padding: 10px; border-radius: 5px;">
        <strong>Balanced Perspective:</strong> You seem to have a generally balanced self-view, with a solid foundation of self-esteem. You likely have areas where you feel strong and others you'd like to improve, which is a healthy and realistic outlook. Continue to nurture your strengths while exploring the targeted advice for areas you wish to develop further.
        </div>
        """
    elif score <= 151:
        return """
        <div style="background-color: #D2FFD8; padding: 10px; border-radius: 5px;">
        <strong>Confident Outlook:</strong> You have a strong and positive self-image. You are likely confident in your abilities and decisions, navigating challenges with a resilient mindset. Keep fostering this positive self-perception by continuing to engage in activities that align with your values and challenge you in healthy ways. Your positive outlook can be an inspiration to others.
        </div>
        """
    else: # score > 151
        return """
        <div style="background-color: #E6D2FF; padding: 10px; border-radius: 5px;">
        <strong>Very High Self-Esteem:</strong> Your score reflects a very high level of self-confidence and self-acceptance. You have a clear understanding of your strengths and value yourself highly. This is a fantastic asset. Continue to leverage this self-assurance to pursue your goals and uplift those around you. Ensure this confidence is paired with an openness to feedback for continuous growth.
        </div>
        """

def display_survey_results(responses):
    """
    Analyzes and displays the survey results and advice.
    This function avoids repeating the analysis logic.
    """
    st.header("Mental Checkup Results")
    st.write("Here's a breakdown of your self-perception based on your answers.")

    categories = {
        "Physical": [responses[1], responses[2], responses[8], responses[19], responses[21], responses[25]],
        "Social": [responses[0], responses[7], responses[20], responses[30], responses[31], responses[34]],
        "Temperamental": [responses[3], responses[9], responses[13], responses[15], responses[18], responses[22]],
        "Educational": [responses[4], responses[12], responses[14], responses[16], responses[23], responses[24]],
        "Moral": [responses[5], responses[27], responses[28], responses[32], responses[33], responses[35]],
        "Intellectual": [responses[6], responses[10], responses[11], responses[17], responses[26], responses[29]]
    }

    # Display total score and commentary first
    total_self_image = sum(responses)
    st.subheader(f"Total Self-Image Score: {total_self_image}")
    commentary = get_score_commentary(total_self_image)
    st.markdown(commentary, unsafe_allow_html=True)
    st.markdown("---")
    
    st.write("### Detailed Category Breakdown:")
    for category_name, cat_responses in categories.items():
        sentiment, total = analyze_sentiment(cat_responses)
        
        with st.expander(f"**{category_name}**: {sentiment.capitalize()} (Score: {total})", expanded=(sentiment == 'negative')):
            advice = ADVICE_AND_QUOTES[category_name][sentiment]
            st.write(f"💡 **Advice**: {advice}")
            
            st.markdown("**Motivational Quotes:**")
            # Show a random quote from the list to keep it fresh
            quote = random.choice(ADVICE_AND_QUOTES[category_name]["quotes"])
            st.info(f"_{quote}_")


# --- WORKOUT GENERATION & TRACKING ---

def generate_workout(split, level, physical_sentiment, goal_type, bodybuilding_goal, sport):
    """Generates a workout plan based on user inputs and survey sentiment."""
    base_sets = {"Beginner": 3, "Intermediate": 4, "Advanced": 5}
    base_reps = {"Beginner": 12, "Intermediate": 8, "Advanced": 6}
    
    # Adjust intensity based on the 'Physical' sentiment score from the survey
    intensity_modifier = {"positive": 1.0, "neutral": 0.8, "negative": 0.6}.get(physical_sentiment, 1.0)

    sets = max(2, int(base_sets[level] * intensity_modifier))
    reps = max(5, int(base_reps[level] * intensity_modifier))

    # This dictionary is for bodybuilding routines.
    routines = {
        "Push-Pull-Legs": {
            "Variation 1": [{"Day": "Push", "Exercises": [{"Exercise": "Bench Press", "Sets": sets, "Reps": reps, "Rest": "90s", "Focus": "Chest strength"}, {"Exercise": "Overhead Press", "Sets": sets-1, "Reps": reps+2, "Rest": "60s", "Focus": "Shoulders"}, {"Exercise": "Tricep Dips", "Sets": sets-1, "Reps": reps+4, "Rest": "60s", "Focus": "Triceps"}]}, {"Day": "Pull", "Exercises": [{"Exercise": "Deadlifts", "Sets": sets, "Reps": reps-2, "Rest": "90s", "Focus": "Back strength"}, {"Exercise": "Pull-Ups", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Lats"}, {"Exercise": "Barbell Rows", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Upper back"}]}, {"Day": "Legs", "Exercises": [{"Exercise": "Squats", "Sets": sets, "Reps": reps, "Rest": "90s", "Focus": "Quads"}, {"Exercise": "Romanian Deadlifts", "Sets": sets-1, "Reps": reps+2, "Rest": "60s", "Focus": "Hamstrings"}, {"Exercise": "Calf Raises", "Sets": sets-1, "Reps": reps+5, "Rest": "45s", "Focus": "Calves"}]}],
            "Variation 2": [{"Day": "Push", "Exercises": [{"Exercise": "Incline Bench Press", "Sets": sets, "Reps": reps, "Rest": "90s", "Focus": "Upper chest"}, {"Exercise": "Dumbbell Shoulder Press", "Sets": sets-1, "Reps": reps+2, "Rest": "60s", "Focus": "Shoulders"}, {"Exercise": "Skull Crushers", "Sets": sets-1, "Reps": reps+4, "Rest": "60s", "Focus": "Triceps"}]}, {"Day": "Pull", "Exercises": [{"Exercise": "Rack Pulls", "Sets": sets, "Reps": reps-2, "Rest": "90s", "Focus": "Lower back"}, {"Exercise": "Chin-Ups", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Lats and biceps"}, {"Exercise": "Dumbbell Rows", "Sets": sets-1, "Reps": reps+4, "Rest": "60s", "Focus": "Upper back"}]}, {"Day": "Legs", "Exercises": [{"Exercise": "Front Squats", "Sets": sets, "Reps": reps, "Rest": "90s", "Focus": "Quads and core"}, {"Exercise": "Lunges", "Sets": sets-1, "Reps": reps+2, "Rest": "60s", "Focus": "Glutes and hamstrings"}, {"Exercise": "Seated Calf Raises", "Sets": sets-1, "Reps": reps+5, "Rest": "45s", "Focus": "Calves"}]}]
        },
        "Upper-Lower": {
            "Variation 1": [{"Day": "Upper", "Exercises": [{"Exercise": "Bench Press", "Sets": sets, "Reps": reps, "Rest": "90s", "Focus": "Chest"}, {"Exercise": "Pull-Ups", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Lats"}, {"Exercise": "Overhead Press", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Shoulders"}, {"Exercise": "Barbell Rows", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Upper back"}]}, {"Day": "Lower", "Exercises": [{"Exercise": "Squats", "Sets": sets, "Reps": reps, "Rest": "90s", "Focus": "Quads"}, {"Exercise": "Deadlifts", "Sets": sets, "Reps": reps-2, "Rest": "90s", "Focus": "Hamstrings and back"}, {"Exercise": "Leg Press", "Sets": sets-1, "Reps": reps+4, "Rest": "60s", "Focus": "Quads and glutes"}, {"Exercise": "Calf Raises", "Sets": sets-1, "Reps": reps+5, "Rest": "45s", "Focus": "Calves"}]}],
            "Variation 2": [{"Day": "Upper", "Exercises": [{"Exercise": "Incline Dumbbell Press", "Sets": sets, "Reps": reps, "Rest": "90s", "Focus": "Upper chest"}, {"Exercise": "Chin-Ups", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Lats and biceps"}, {"Exercise": "Arnold Press", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Shoulders"}, {"Exercise": "T-Bar Rows", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Mid-back"}]}, {"Day": "Lower", "Exercises": [{"Exercise": "Bulgarian Split Squats", "Sets": sets, "Reps": reps, "Rest": "60s", "Focus": "Quads and glutes"}, {"Exercise": "Romanian Deadlifts", "Sets": sets, "Reps": reps, "Rest": "90s", "Focus": "Hamstrings"}, {"Exercise": "Leg Extensions", "Sets": sets-1, "Reps": reps+4, "Rest": "60s", "Focus": "Quads"}, {"Exercise": "Seated Calf Raises", "Sets": sets-1, "Reps": reps+5, "Rest": "45s", "Focus": "Calves"}]}]
        },
        "Bro Split": {
            "Variation 1": [{"Day": "Chest", "Exercises": [{"Exercise": "Bench Press", "Sets": sets, "Reps": reps, "Rest": "90s", "Focus": "Chest"}, {"Exercise": "Incline Dumbbell Press", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Upper chest"}, {"Exercise": "Cable Flyes", "Sets": sets-1, "Reps": reps+4, "Rest": "60s", "Focus": "Chest isolation"}]}, {"Day": "Back", "Exercises": [{"Exercise": "Deadlifts", "Sets": sets, "Reps": reps-2, "Rest": "90s", "Focus": "Back"}, {"Exercise": "Pull-Ups", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Lats"}, {"Exercise": "Barbell Rows", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Upper back"}]}, {"Day": "Arms", "Exercises": [{"Exercise": "Barbell Curls", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Biceps"}, {"Exercise": "Skull Crushers", "Sets": sets-1, "Reps": reps+4, "Rest": "60s", "Focus": "Triceps"}, {"Exercise": "Hammer Curls", "Sets": sets-1, "Reps": reps+4, "Rest": "60s", "Focus": "Biceps"}]}],
            "Variation 2": [{"Day": "Chest", "Exercises": [{"Exercise": "Incline Bench Press", "Sets": sets, "Reps": reps, "Rest": "90s", "Focus": "Upper chest"}, {"Exercise": "Dumbbell Flyes", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Chest stretch"}, {"Exercise": "Pec Deck", "Sets": sets-1, "Reps": reps+4, "Rest": "60s", "Focus": "Chest isolation"}]}, {"Day": "Back", "Exercises": [{"Exercise": "Rack Pulls", "Sets": sets, "Reps": reps-2, "Rest": "90s", "Focus": "Lower back"}, {"Exercise": "Chin-Ups", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Lats and biceps"}, {"Exercise": "Dumbbell Rows", "Sets": sets-1, "Reps": reps+4, "Rest": "60s", "Focus": "Upper back"}]}, {"Day": "Arms", "Exercises": [{"Exercise": "EZ Bar Curls", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Biceps"}, {"Exercise": "Close-Grip Bench Press", "Sets": sets-1, "Reps": reps, "Rest": "60s", "Focus": "Triceps"}, {"Exercise": "Concentration Curls", "Sets": sets-1, "Reps": reps+4, "Rest": "60s", "Focus": "Biceps peak"}]}]
        }
    }
    
    if goal_type == "Sports":
        sport_routines = {
            "Football": {
                "Variation 1 (Speed & Agility)": [{"Day": "Lower Body Power", "Exercises": [{"Exercise": "Power Cleans", "Sets": sets, "Reps": 3, "Rest": "120s"}, {"Exercise": "Box Jumps", "Sets": sets, "Reps": 5, "Rest": "90s"}, {"Exercise": "Back Squats", "Sets": sets, "Reps": reps, "Rest": "90s"}]}, {"Day": "Upper Body Strength", "Exercises": [{"Exercise": "Bench Press", "Sets": sets, "Reps": reps, "Rest": "90s"}, {"Exercise": "Weighted Pull-Ups", "Sets": sets, "Reps": reps, "Rest": "75s"}, {"Exercise": "Barbell Rows", "Sets": sets-1, "Reps": reps, "Rest": "60s"}]}, {"Day": "Conditioning & Core", "Exercises": [{"Exercise": "Sled Pushes", "Sets": sets, "Reps": "20m", "Rest": "60s"}, {"Exercise": "Agility Ladder Drills", "Sets": sets, "Reps": "60s", "Rest": "60s"}, {"Exercise": "Plank with Reach", "Sets": sets, "Reps": "60s", "Rest": "45s"}]}],
                "Variation 2 (Strength & Power)": [{"Day": "Full Body Strength", "Exercises": [{"Exercise": "Deadlifts", "Sets": sets, "Reps": reps-2, "Rest": "120s"}, {"Exercise": "Overhead Press", "Sets": sets, "Reps": reps, "Rest": "90s"}, {"Exercise": "Farmer's Walks", "Sets": sets, "Reps": "30m", "Rest": "60s"}]}, {"Day": "Explosive Power", "Exercises": [{"Exercise": "Hang Cleans", "Sets": sets, "Reps": 3, "Rest": "120s"}, {"Exercise": "Medicine Ball Slams", "Sets": sets, "Reps": 8, "Rest": "60s"}, {"Exercise": "Broad Jumps", "Sets": sets, "Reps": 5, "Rest": "90s"}]}, {"Day": "Accessory & Durability", "Exercises": [{"Exercise": "Glute-Ham Raises", "Sets": sets-1, "Reps": reps+2, "Rest": "60s"}, {"Exercise": "Face Pulls", "Sets": sets-1, "Reps": reps+4, "Rest": "45s"}, {"Exercise": "Rotational Cable Chops", "Sets": sets, "Reps": reps+4, "Rest": "45s"}]}]
            },
            "Basketball": {
                "Variation 1 (Vertical Power)": [{"Day": "Plyometrics", "Exercises": [{"Exercise": "Depth Jumps", "Sets": sets, "Reps": 5, "Rest": "120s"}, {"Exercise": "Box Jumps", "Sets": sets, "Reps": 5, "Rest": "90s"}, {"Exercise": "Medicine Ball Slams", "Sets": sets, "Reps": 8, "Rest": "60s"}]}, {"Day": "Strength", "Exercises": [{"Exercise": "Front Squats", "Sets": sets, "Reps": reps, "Rest": "90s"}, {"Exercise": "Pull-Ups", "Sets": sets, "Reps": reps, "Rest": "60s"}, {"Exercise": "Single-Leg Romanian Deadlifts", "Sets": sets-1, "Reps": reps, "Rest": "60s"}]}, {"Day": "Conditioning", "Exercises": [{"Exercise": "Agility Ladder Drills", "Sets": sets, "Reps": "60s", "Rest": "60s"}, {"Exercise": "Battle Ropes", "Sets": sets, "Reps": "30s", "Rest": "45s"}, {"Exercise": "Hanging Leg Raises", "Sets": sets-1, "Reps": reps+4, "Rest": "45s"}]}],
                "Variation 2 (Agility & Durability)": [{"Day": "Strength & Stability", "Exercises": [{"Exercise": "Bulgarian Split Squats", "Sets": sets, "Reps": reps, "Rest": "60s"}, {"Exercise": "Dumbbell Bench Press", "Sets": sets, "Reps": reps, "Rest": "75s"}, {"Exercise": "Face Pulls", "Sets": sets, "Reps": 15, "Rest": "45s"}]}, {"Day": "Change of Direction", "Exercises": [{"Exercise": "Lateral Lunges", "Sets": sets, "Reps": reps, "Rest": "60s"}, {"Exercise": "Rotational Medicine Ball Throws", "Sets": sets, "Reps": 8, "Rest": "60s"}, {"Exercise": "Cone Drills", "Sets": 5, "Reps": "30s", "Rest": "60s"}]}, {"Day": "Core & Endurance", "Exercises": [{"Exercise": "Stationary Bike Sprints", "Sets": 5, "Reps": "20s", "Rest": "90s"}, {"Exercise": "Pallof Press", "Sets": sets, "Reps": 12, "Rest": "45s"}, {"Exercise": "Side Planks", "Sets": sets, "Reps": "45s per side", "Rest": "30s"}]}]
            },
            "Volleyball": {
                "Variation 1 (Spiking & Blocking)": [{"Day": "Vertical Jump", "Exercises": [{"Exercise": "Jump Squats", "Sets": sets, "Reps": 6, "Rest": "90s"}, {"Exercise": "Box Jumps", "Sets": sets, "Reps": 5, "Rest": "90s"}, {"Exercise": "Depth Jumps", "Sets": sets, "Reps": 5, "Rest": "120s"}]}, {"Day": "Upper Body Power", "Exercises": [{"Exercise": "Push Press", "Sets": sets, "Reps": reps, "Rest": "90s"}, {"Exercise": "Medicine Ball Slams", "Sets": sets, "Reps": 8, "Rest": "60s"}, {"Exercise": "Lat Pulldowns", "Sets": sets, "Reps": reps+2, "Rest": "60s"}]}, {"Day": "Core & Shoulders", "Exercises": [{"Exercise": "Face Pulls", "Sets": sets, "Reps": 15, "Rest": "45s"}, {"Exercise": "Rotational Cable Chops", "Sets": sets, "Reps": 12, "Rest": "60s"}, {"Exercise": "Plank", "Sets": sets, "Reps": "60s", "Rest": "45s"}]}],
                "Variation 2 (Agility & Injury Prevention)": [{"Day": "Lateral Movement", "Exercises": [{"Exercise": "Lateral Box Jumps", "Sets": sets, "Reps": 6, "Rest": "90s"}, {"Exercise": "Agility Ladder Drills", "Sets": 5, "Reps": "45s", "Rest": "60s"}, {"Exercise": "Lateral Lunges", "Sets": sets, "Reps": reps, "Rest": "60s"}]}, {"Day": "Full Body Strength", "Exercises": [{"Exercise": "Goblet Squats", "Sets": sets, "Reps": reps+2, "Rest": "75s"}, {"Exercise": "Dumbbell Rows", "Sets": sets, "Reps": reps+2, "Rest": "60s"}, {"Exercise": "Single-Leg Glute Bridges", "Sets": sets, "Reps": 15, "Rest": "45s"}]}, {"Day": "Conditioning", "Exercises": [{"Exercise": "Burpees", "Sets": sets, "Reps": 10, "Rest": "60s"}, {"Exercise": "Kettlebell Swings", "Sets": sets, "Reps": 15, "Rest": "60s"}, {"Exercise": "Hanging Knee Raises", "Sets": sets, "Reps": 15, "Rest": "45s"}]}]
            },
            "Hockey": {
                "Variation 1 (Power & Speed)": [{"Day": "Lower Body Power", "Exercises": [{"Exercise": "Barbell Squats", "Sets": sets, "Reps": reps, "Rest": "90s"}, {"Exercise": "Lateral Box Jumps", "Sets": sets, "Reps": 8, "Rest": "90s"}, {"Exercise": "Sled Drags", "Sets": sets, "Reps": "20m", "Rest": "75s"}]}, {"Day": "Upper Body Strength", "Exercises": [{"Exercise": "Bench Press", "Sets": sets, "Reps": reps, "Rest": "90s"}, {"Exercise": "Weighted Chin-Ups", "Sets": sets, "Reps": reps, "Rest": "75s"}, {"Exercise": "Farmer's Walks", "Sets": sets, "Reps": "30m", "Rest": "60s"}]}, {"Day": "Rotational & Core", "Exercises": [{"Exercise": "Rotational Medicine Ball Throws", "Sets": sets, "Reps": 8, "Rest": "60s"}, {"Exercise": "Cable Woodchoppers", "Sets": sets, "Reps": 12, "Rest": "60s"}, {"Exercise": "Ab Rollouts", "Sets": sets, "Reps": 10, "Rest": "60s"}]}],
                "Variation 2 (Endurance & Stability)": [{"Day": "Leg Endurance", "Exercises": [{"Exercise": "Bulgarian Split Squats", "Sets": sets, "Reps": reps+4, "Rest": "60s"}, {"Exercise": "Walking Lunges", "Sets": sets, "Reps": "20 steps", "Rest": "75s"}, {"Exercise": "Glute-Ham Raises", "Sets": sets, "Reps": 12, "Rest": "60s"}]}, {"Day": "Stability & Control", "Exercises": [{"Exercise": "Single-Arm Dumbbell Press", "Sets": sets, "Reps": reps, "Rest": "60s"}, {"Exercise": "Pallof Press", "Sets": sets, "Reps": 15, "Rest": "45s"}, {"Exercise": "Copenhagen Planks", "Sets": sets, "Reps": "30s per side", "Rest": "30s"}]}, {"Day": "Conditioning", "Exercises": [{"Exercise": "Stationary Bike Intervals", "Sets": 6, "Reps": "30s sprint", "Rest": "60s"}, {"Exercise": "Kettlebell Swings", "Sets": sets, "Reps": 20, "Rest": "60s"}, {"Exercise": "Battle Ropes", "Sets": sets, "Reps": "30s", "Rest": "45s"}]}]
            },
            "Cycling": {
                "Variation 1 (Max Power Output)": [{"Day": "Heavy Strength", "Exercises": [{"Exercise": "Back Squats", "Sets": sets, "Reps": reps, "Rest": "90s"}, {"Exercise": "Deadlifts", "Sets": sets, "Reps": reps-2, "Rest": "120s"}, {"Exercise": "Leg Press", "Sets": sets, "Reps": reps, "Rest": "75s"}]}, {"Day": "Power Development", "Exercises": [{"Exercise": "Kettlebell Swings", "Sets": sets, "Reps": 15, "Rest": "60s"}, {"Exercise": "Box Jumps", "Sets": sets, "Reps": 5, "Rest": "90s"}, {"Exercise": "Weighted Calf Raises", "Sets": sets, "Reps": 12, "Rest": "45s"}]}, {"Day": "Core Stability", "Exercises": [{"Exercise": "Plank", "Sets": 3, "Reps": "Until failure", "Rest": "60s"}, {"Exercise": "Hanging Leg Raises", "Sets": sets, "Reps": 15, "Rest": "45s"}, {"Exercise": "Bird-Dog", "Sets": sets, "Reps": 12, "Rest": "45s"}]}],
                "Variation 2 (Muscular Endurance)": [{"Day": "High-Rep Strength", "Exercises": [{"Exercise": "Goblet Squats", "Sets": sets, "Reps": 20, "Rest": "60s"}, {"Exercise": "Romanian Deadlifts", "Sets": sets, "Reps": 15, "Rest": "60s"}, {"Exercise": "Leg Extensions", "Sets": sets, "Reps": 15, "Rest": "45s"}]}, {"Day": "Endurance & Core", "Exercises": [{"Exercise": "Bulgarian Split Squats", "Sets": sets, "Reps": 15, "Rest": "60s"}, {"Exercise": "Single-Leg Glute Bridges", "Sets": sets, "Reps": 20, "Rest": "45s"}, {"Exercise": "Side Planks", "Sets": 3, "Reps": "Until failure", "Rest": "45s"}]}, {"Day": "Conditioning", "Exercises": [{"Exercise": "Stationary Bike Sprints", "Sets": 8, "Reps": "20s on, 10s off", "Rest": "2 min rest after 8 reps"}, {"Exercise": "Battle Ropes", "Sets": sets, "Reps": "45s", "Rest": "60s"}, {"Exercise": "Mountain Climbers", "Sets": sets, "Reps": "45s", "Rest": "60s"}]}]
            },
            "Cricket": {
                "Variation 1 (Fast Bowler Focus)": [{"Day": "Power & Strength", "Exercises": [{"Exercise": "Medicine Ball Slams", "Sets": sets, "Reps": 8}, {"Exercise": "Single-Leg Squats", "Sets": sets, "Reps": reps}, {"Exercise": "Lat Pulldowns", "Sets": sets, "Reps": reps+2}]}, {"Day": "Core & Stability", "Exercises": [{"Exercise": "Cable Woodchoppers", "Sets": sets, "Reps": 12}, {"Exercise": "Side Planks", "Sets": sets, "Reps": "45s"}, {"Exercise": "Face Pulls", "Sets": sets, "Reps": 15}]}, {"Day": "Conditioning", "Exercises": [{"Exercise": "Sprint Intervals", "Sets": 6, "Reps": "30m"}, {"Exercise": "Burpees", "Sets": sets, "Reps": 12}]}],
                "Variation 2 (Batsman Focus)": [{"Day": "Rotational Power", "Exercises": [{"Exercise": "Rotational Medicine Ball Throws", "Sets": sets, "Reps": 8}, {"Exercise": "Kettlebell Swings", "Sets": sets, "Reps": 15}, {"Exercise": "Barbell Rows", "Sets": sets, "Reps": reps}]}, {"Day": "Legs & Wrists", "Exercises": [{"Exercise": "Front Squats", "Sets": sets, "Reps": reps}, {"Exercise": "Farmer's Walks", "Sets": sets, "Reps": "30m"}, {"Exercise": "Wrist Curls", "Sets": sets, "Reps": 15}]}, {"Day": "Agility", "Exercises": [{"Exercise": "Agility Ladder Drills", "Sets": 5, "Reps": "45s"}, {"Exercise": "Cone Drills", "Sets": 5, "Reps": "30s"}]}]
            },
            "Tennis": {
                "Variation 1 (Power & Agility)": [{"Day": "Lower Body Power & Core", "Exercises": [{"Exercise": "Medicine Ball Rotational Throws", "Sets": sets, "Reps": 8, "Rest": "60s"}, {"Exercise": "Box Jumps", "Sets": sets, "Reps": 5, "Rest": "90s"}, {"Exercise": "Lateral Lunges", "Sets": sets-1, "Reps": reps, "Rest": "60s"}]}, {"Day": "Upper Body Strength", "Exercises": [{"Exercise": "Dumbbell Bench Press", "Sets": sets, "Reps": reps, "Rest": "75s"}, {"Exercise": "Cable Woodchoppers", "Sets": sets, "Reps": 12, "Rest": "60s"}, {"Exercise": "Face Pulls", "Sets": sets, "Reps": 15, "Rest": "45s"}]}, {"Day": "Conditioning", "Exercises": [{"Exercise": "Agility Ladder Drills", "Sets": 5, "Reps": "45s", "Rest": "60s"}, {"Exercise": "Sprint Intervals (20m)", "Sets": 6, "Reps": "1 rep", "Rest": "75s"}, {"Exercise": "Jump Rope", "Sets": 3, "Reps": "3 minutes", "Rest": "60s"}]}],
                "Variation 2 (Endurance & Injury Prevention)": [{"Day": "Full Body Endurance", "Exercises": [{"Exercise": "Goblet Squats", "Sets": sets, "Reps": 15, "Rest": "60s"}, {"Exercise": "Single-Arm Dumbbell Rows", "Sets": sets, "Reps": 12, "Rest": "60s"}, {"Exercise": "Walking Lunges", "Sets": sets, "Reps": "20 steps", "Rest": "75s"}]}, {"Day": "Shoulder & Core Stability", "Exercises": [{"Exercise": "Pallof Press", "Sets": sets, "Reps": 12, "Rest": "45s"}, {"Exercise": "External Rotations (Band)", "Sets": sets, "Reps": 15, "Rest": "45s"}, {"Exercise": "Plank with Shoulder Taps", "Sets": sets, "Reps": "60s", "Rest": "60s"}]}, {"Day": "Low-Impact Conditioning", "Exercises": [{"Exercise": "Stationary Bike", "Sets": 1, "Reps": "20 minutes HIIT", "Rest": "N/A"}, {"Exercise": "Kettlebell Swings", "Sets": sets, "Reps": 20, "Rest": "60s"}, {"Exercise": "Bird-Dog", "Sets": sets, "Reps": 12, "Rest": "45s"}]}]
            },
            "Running": {
                "Variation 1 (Strength for Speed)": [{"Day": "Full Body Strength A", "Exercises": [{"Exercise": "Barbell Squats", "Sets": sets, "Reps": reps, "Rest": "90s"}, {"Exercise": "Romanian Deadlifts", "Sets": sets, "Reps": reps, "Rest": "75s"}, {"Exercise": "Weighted Calf Raises", "Sets": sets, "Reps": 15, "Rest": "45s"}]}, {"Day": "Full Body Strength B", "Exercises": [{"Exercise": "Walking Lunges", "Sets": sets, "Reps": reps, "Rest": "75s"}, {"Exercise": "Single-Leg Glute Bridges", "Sets": sets, "Reps": 12, "Rest": "60s"}, {"Exercise": "Pull-Ups (or Lat Pulldowns)", "Sets": sets, "Reps": reps, "Rest": "60s"}]}, {"Day": "Plyometrics & Core", "Exercises": [{"Exercise": "Box Jumps", "Sets": sets, "Reps": 5, "Rest": "90s"}, {"Exercise": "A-Skips", "Sets": sets, "Reps": "20m", "Rest": "60s"}, {"Exercise": "Hanging Knee Raises", "Sets": sets, "Reps": 15, "Rest": "45s"}]}],
                "Variation 2 (Injury Prevention & Endurance)": [{"Day": "Unilateral Strength", "Exercises": [{"Exercise": "Bulgarian Split Squats", "Sets": sets, "Reps": reps+2, "Rest": "60s"}, {"Exercise": "Single-Leg Romanian Deadlifts", "Sets": sets, "Reps": reps, "Rest": "60s"}, {"Exercise": "Single-Leg Calf Raises", "Sets": sets, "Reps": 15, "Rest": "45s"}]}, {"Day": "Hip & Core Stability", "Exercises": [{"Exercise": "Banded Lateral Walks", "Sets": 3, "Reps": "15 steps each way", "Rest": "60s"}, {"Exercise": "Bird-Dog", "Sets": sets, "Reps": 12, "Rest": "45s"}, {"Exercise": "Side Planks", "Sets": sets, "Reps": "45s per side", "Rest": "30s"}]}, {"Day": "Conditioning", "Exercises": [{"Exercise": "Kettlebell Swings", "Sets": sets, "Reps": 20, "Rest": "60s"}, {"Exercise": "Jump Rope", "Sets": 3, "Reps": "3 minutes", "Rest": "60s"}, {"Exercise": "Mountain Climbers", "Sets": sets, "Reps": "45s", "Rest": "60s"}]}]
            }
        }
        return sport_routines.get(sport, {})

    elif goal_type == "Bodybuilding":
        plan = routines[split]
        for variation_days in plan.values():
            for day in variation_days:
                for exercise in day["Exercises"]:
                    if bodybuilding_goal == "Weight Loss":
                        exercise["Reps"] = max(1, exercise.get("Reps", reps) + 2)
                        exercise["Rest"] = "45-60s"
                        exercise["Focus"] += " | Goal: Fat loss"
                    elif bodybuilding_goal == "Weight Gain":
                        exercise["Sets"] = max(1, exercise.get("Sets", sets) + 1)
                        exercise["Rest"] = "75-90s"
                        exercise["Focus"] += " | Goal: Muscle gain"
        return plan

    return routines.get(split, {})

def workout_tracker():
    """Renders the UI for logging and viewing workout sessions."""
    if 'workout_logs' not in st.session_state:
        st.session_state.workout_logs = []

    with st.expander("📝 Log a New Workout", expanded=True):
        with st.form("tracker_form"):
            user_data = st.session_state.user_data
            goal_type = user_data.get("goal_type")
            split = user_data.get("split")
            
            day_options = []
            if goal_type == "Sports":
                # Dynamically get day names from the generated workout plan
                sport_plan = generate_workout(None, user_data.get("level"), "neutral", "Sports", None, user_data.get("sport"))
                if sport_plan:
                    # Get day names from the first variation
                    first_variation = list(sport_plan.values())[0]
                    day_options = [day['Day'] for day in first_variation]
            elif split == "Push-Pull-Legs":
                day_options = ["Push", "Pull", "Legs"]
            elif split == "Upper-Lower":
                day_options = ["Upper", "Lower"]
            elif split == "Bro Split":
                day_options = ["Chest", "Back", "Arms"]
            else: # Fallback
                day_options = ["Day 1", "Day 2", "Day 3"]


            c1, c2, c3 = st.columns(3)
            date = c1.date_input("Date", datetime.date.today())
            workout_day = c2.selectbox("Workout Day", day_options)
            completed = c3.checkbox("Completed?", value=True)
            
            notes = st.text_area("Notes (e.g., weights used, how you felt)", height=100)
            
            if st.form_submit_button("Log Workout", use_container_width=True):
                st.session_state.workout_logs.append({
                    "Date": date.strftime("%Y-%m-%d"),
                    "Workout Day": workout_day,
                    "Completed": "✅" if completed else "❌",
                    "Notes": notes
                })
                st.success("Workout logged successfully!")

    if st.session_state.workout_logs:
        st.subheader("📋 Your Workout Log History")
        st.dataframe(st.session_state.workout_logs, use_container_width=True)
    else:
        st.info("No workouts logged yet. Fill out the form above to get started!")


# --- PAGE RENDERING FUNCTIONS ---

def render_user_input_form():
    """Displays the multi-step form for collecting user data."""
    st.header("Step 1: Your Details")
    with st.form("user_input_basic"):
        name = st.text_input("Name:")
        age = st.number_input("Age:", min_value=1, max_value=100, step=1)
        gender = st.selectbox("Gender:", ["Female", "Male", "Other"])
        goal_type = st.selectbox("Primary Goal:", ["Bodybuilding", "Sports"], help="Choose your main training objective.")
        
        take_survey = st.radio("Would you like to take a mental checkup survey to tailor your plan?", ["Yes", "No"], index=1)
        
        if st.form_submit_button("Next →", use_container_width=True):
            if name and age:
                st.session_state.form_data = {
                    "name": name, "age": age, "gender": gender,
                    "goal_type": goal_type,
                    "take_survey": (take_survey == "Yes")
                }
                st.session_state.input_stage = 'details'
                st.rerun()
            else:
                st.warning("Please fill in your Name and Age.")

def render_details_form():
    """Displays the second part of the user input form."""
    st.header("Step 2: Your Plan")
    with st.form("user_input_details"):
        form_data = st.session_state.form_data
        
        bodybuilding_goal = None
        split = None
        sport = None # Initialize sport variable

        # Conditionally show options based on the selected goal
        if form_data.get("goal_type") == "Bodybuilding":
            bodybuilding_goal = st.selectbox("Bodybuilding Focus:", ["Weight Loss", "Weight Gain"], index=1, help="Target cutting or bulking.")
            split = st.selectbox("Workout Split:", ["Push-Pull-Legs", "Upper-Lower", "Bro Split"])
        else:
            sport = st.selectbox("Sport:", [
                "Football", "Basketball", "Volleyball", "Hockey", "Cycling", 
                "Cricket", "Tennis", "Running"
            ], help="Select the sport you want a plan for.")
            split = sport # Use the chosen sport as the 'split' identifier
        
        level = st.selectbox("Fitness Level:", ["Beginner", "Intermediate", "Advanced"])

        c1, c2 = st.columns(2)
        if c1.form_submit_button("← Back", use_container_width=True):
            st.session_state.input_stage = 'basic'
            st.rerun()

        if c2.form_submit_button("✓ Generate Plan", use_container_width=True):
            # Ensure 'split' is not None if the user somehow bypasses the logic
            if split is None:
                st.error("Please go back and select a primary goal.")
                return

            st.session_state.user_data = {
                **form_data,
                "split": split,
                "level": level,
                "bodybuilding_goal": bodybuilding_goal,
                "sport": sport # Add the chosen sport to the final user data
            }
            # Decide the next step based on survey choice
            st.session_state.step = 'survey' if form_data.get("take_survey") else 'results'
            del st.session_state.input_stage
            del st.session_state.form_data
            st.rerun()

def render_survey_page():
    """A dedicated page for the user to complete the survey."""
    st.header("🧠 Mental Checkup Survey")
    st.write("Your workout intensity will be adjusted based on your answers. Please answer honestly.")
    st.markdown("---")
    
    responses = run_chatbot()
    
    if responses is not None:
        # Survey is complete, now process the results
        st.session_state.survey_responses = responses
        
        # Specifically find the physical sentiment to adjust the workout
        physical_responses = [responses[1], responses[2], responses[8], responses[19], responses[21], responses[25]]
        sentiment, _ = analyze_sentiment(physical_responses)
        st.session_state.physical_sentiment = sentiment
        
        # Move to the final results page
        st.session_state.step = 'results'
        st.balloons()
        st.rerun()

def render_results_page():
    """Displays the main results page with tabs for Workouts, Logs, and Mental Health."""
    user_data = st.session_state.user_data
    st.header(f"Welcome, {user_data.get('name', 'User')}!")
    
    # Define tabs - only show Mental Health tab if survey was taken
    tab_list = ["💪 Workouts", "📝 Logs"]
    if user_data.get("take_survey"):
        tab_list.append("🧠 Mental Health Checkup")
    
    workout_tab, logs_tab, *mental_health_tab = st.tabs(tab_list)

    with workout_tab:
        sentiment = st.session_state.get('physical_sentiment')
        if sentiment:
            st.info(f"Your plan's intensity has been adjusted based on your **{sentiment}** physical self-perception.")
        
        workouts = generate_workout(
            user_data["split"],
            user_data["level"],
            sentiment,
            user_data.get("goal_type"),
            user_data.get("bodybuilding_goal"),
            user_data.get("sport")
        )
        
        st.subheader(f"Your Personalised Plan for {user_data.get('split')}")
        
        variation_names = list(workouts.keys())
        chosen_variation = st.selectbox("Select a Plan Variation:", variation_names)
        
        if chosen_variation and workouts[chosen_variation]:
            for day in workouts[chosen_variation]:
                with st.expander(f"**{day['Day']} Day**", expanded=True):
                    for ex in day["Exercises"]:
                        # Handle cases where Reps might be a string (e.g., "20m")
                        reps_display = ex.get('Reps', 'N/A')
                        sets_display = ex.get('Sets', 'N/A')
                        rest_display = ex.get('Rest', '60s')
                        
                        st.write(f"• **{ex['Exercise']}**: {sets_display} sets × {reps_display} reps (Rest: {rest_display})")
                        if 'Focus' in ex: # Only show caption if Focus exists
                            st.caption(f"  Focus: {ex['Focus']}")
        else:
            st.warning("Could not generate a workout plan with the selected options.")


    with logs_tab:
        workout_tracker()

    if user_data.get("take_survey") and mental_health_tab:
        with mental_health_tab[0]:
            if 'survey_responses' in st.session_state:
                display_survey_results(st.session_state.survey_responses)
            else:
                st.warning("Survey results not found. Please complete the survey.")
    
    if st.button("Start Over"):
        st.session_state.clear()
        st.rerun()


# --- MAIN APPLICATION LOGIC ---

def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(page_title="Personalized Workout Generator", layout="wide")
    st.title(" Personalized Workout Generator")
    st.write("Create a workout plan tailored to your goals and track your progress.")
    st.markdown("---")

    # Initialize session state variables
    if 'step' not in st.session_state:
        st.session_state.step = 'input'
    if 'input_stage' not in st.session_state:
        st.session_state.input_stage = 'basic'
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {}

    # Simple state machine to control the app flow
    if st.session_state.step == 'input':
        if st.session_state.input_stage == 'basic':
            render_user_input_form()
        else:
            render_details_form()
    elif st.session_state.step == 'survey':
        render_survey_page()
    elif st.session_state.step == 'results':
        render_results_page()

if __name__ == "__main__":
    main()

