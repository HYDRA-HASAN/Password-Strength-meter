import streamlit as st
import re
import secrets
import string

# Optimized password strength checker
def check_password_strength(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"[0-9]", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    score = sum(criteria.values())
    feedback = [
        "At least 8 characters" if not criteria["length"] else "",
        "Add an uppercase letter" if not criteria["uppercase"] else "",
        "Add a lowercase letter" if not criteria["lowercase"] else "",
        "Include a digit" if not criteria["digit"] else "",
        "Use a special character" if not criteria["special"] else ""
    ]
    feedback = [f for f in feedback if f]
    
    strength, bar_color = ("Weak", "#FF5555") if score <= 2 else \
                         ("Moderate", "#FFD700") if score <= 4 else \
                         ("Strong", "#00FF7F")
    
    return score, strength, feedback, bar_color

# Password generator
def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*(),.?\":{}|<>"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Custom CSS for a visually stunning design
def add_custom_design():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0F0F0F 0%, #1A1A1A 100%);
        font-family: 'Poppins', sans-serif;
        color: #FFFFFF;
    }
    
    /* Main container */
    .main {
        background: rgba(28, 28, 28, 0.95);
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 0 10px 40px rgba(255, 255, 255, 0.1);
        max-width: 750px;
        margin: 3rem auto;
        backdrop-filter: blur(12px);
    }
    
    /* Title with gradient and shadow */
    h1 {
        font-size: 2.8rem;
        text-align: center;
        margin-bottom: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #03a9f4, #f441a5);
        -webkit-background-clip: text;
        color: transparent;
        text-shadow: 0 2px 10px rgba(244, 65, 165, 0.3);
        animation: fadeIn 1s ease-in-out;
    }
    
    /* Input field with neon glow */
    .stTextInput > div > div > input {
        background: rgba(40, 40, 40, 0.9);
        color: #FFFFFF;
        border: 2px solid #333333;
        border-radius: 12px;
        padding: 0.9rem;
        font-size: 1.2rem;
        transition: all 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #f441a5;
        box-shadow: 0 0 15px rgba(244, 65, 165, 0.5);
    }
    
    /* Uiverse.io Button Design (Modified for smaller size) */
    .stButton > button {
        font-size: 0.9em; /* Smaller font size */
        padding: 0.4em 0.6em; /* Smaller padding */
        border-radius: 0.5em;
        border: none;
        background-color: #000;
        color: #fff;
        cursor: pointer;
        box-shadow: 2px 2px 3px #000000b4;
        position: relative;
        z-index: 1;
        width: auto; /* Allow button to size based on content */
        margin-top: 0.5rem;
    }
    .container {
        position: relative;
        padding: 3px;
        background: linear-gradient(90deg, #03a9f4, #f441a5);
        border-radius: 0.9em;
        transition: all 0.4s ease;
        display: inline-block; /* Ensure container fits button size */
    }
    .container::before {
        content: "";
        position: absolute;
        inset: 0;
        margin: auto;
        border-radius: 0.9em;
        z-index: -10;
        filter: blur(0);
        transition: filter 0.4s ease;
    }
    .container:hover::before {
        background: linear-gradient(90deg, #03a9f4, #f441a5);
        filter: blur(1.2em);
    }
    .container:active::before {
        filter: blur(0.2em);
    }
    
    /* Strength meter with neon effect */
    .strength-meter {
        background: rgba(40, 40, 40, 0.9);
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 2rem;
        display: flex;
        align-items: center;
        gap: 1.5rem;
        box-shadow: 0 0 20px rgba(0, 255, 127, 0.2);
        animation: slideIn 0.5s ease-out;
    }
    .strength-label {
        font-size: 1.3rem;
        font-weight: 600;
        min-width: 100px;
        color: #FFFFFF;
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
    }
    .score-bar {
        flex-grow: 1;
        height: 14px;
        background: #222222;
        border-radius: 7px;
        overflow: hidden;
        box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5);
    }
    .score-fill {
        height: 100%;
        transition: width 0.5s ease-in-out, background-color 0.5s ease-in-out;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
    }
    
    /* Feedback box with gradient border */
    .feedback-box {
        background: rgba(28, 28, 28, 0.9);
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 2rem;
        color: #FFFFFF;
        font-size: 1rem;
        border: 2px solid transparent;
        background-clip: padding-box;
        position: relative;
        animation: fadeInUp 0.5s ease-out;
    }
    .feedback-box::before {
        content: '';
        position: absolute;
        top: -2px; left: -2px; right: -2px; bottom: -2px;
        background: linear-gradient(90deg, #03a9f4, #f441a5);
        z-index: -1;
        border-radius: 14px;
    }
    .feedback-box ul {
        padding-left: 1.5rem;
        margin: 0;
    }
    .feedback-box li {
        margin: 0.5rem 0;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideIn {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    @keyframes fadeInUp {
        from { transform: translateY(10px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app
def main():
    add_custom_design()
    
    with st.container():
        st.markdown('<h1>Password Strength Meter</h1>', unsafe_allow_html=True)
        
        # Tabs for Password Check and Generator
        tab1, tab2 = st.tabs(["Check Password", "Generate Password"])
        
        # Tab 1: Password Checker
        with tab1:
            password = st.text_input("", placeholder="Enter your password", type="password", key="password_input")
            # Wrap the button in a container div for the gradient effect
            st.markdown('<div class="container">', unsafe_allow_html=True)
            analyze = st.button("Analyze", key="analyze_button")
            st.markdown('</div>', unsafe_allow_html=True)
            
            if password:  # Real-time feedback
                score, strength, feedback, bar_color = check_password_strength(password)
                fill_width = (score / 5) * 100
                st.markdown(f"""
                <div class="strength-meter">
                    <span class="strength-label">{strength}</span>
                    <div class="score-bar">
                        <div class="score-fill" style="width: {fill_width}%; background-color: {bar_color};"></div>
                    </div>
                    <span class="strength-label">{score}/5</span>
                </div>
                """, unsafe_allow_html=True)
                
                if strength == "Strong":
                    st.markdown('<div class="feedback-box"><p style="font-weight: 600;">Awesome! Your password is rock-solid.</p></div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="feedback-box"><p style="font-weight: 600;">Tips to strengthen:</p><ul>', unsafe_allow_html=True)
                    for suggestion in feedback:
                        st.markdown(f"<li>{suggestion}</li>", unsafe_allow_html=True)
                    st.markdown('</ul></div>', unsafe_allow_html=True)
            elif analyze:
                st.markdown('<div class="feedback-box"><p style="font-weight: 600;">Please enter a password first!</p></div>', unsafe_allow_html=True)
        
        # Tab 2: Password Generator
        with tab2:
            length = st.slider("Password Length", 8, 32, 12)
            # Wrap the button in a container div for the gradient effect
            st.markdown('<div class="container">', unsafe_allow_html=True)
            generate = st.button("Generate", key="generate_button")
            st.markdown('</div>', unsafe_allow_html=True)
            
            if generate:
                new_password = generate_password(length)
                st.code(new_password, language="text")
                st.markdown('<div class="feedback-box"><p style="font-weight: 600;">Copy this and test it in the checker!</p></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()