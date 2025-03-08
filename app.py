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

# Custom CSS with black tab labels, cooler buttons, and eye button
def add_custom_design():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #FFFFFF 0%, #E6F0FA 100%);
        font-family: 'Poppins', sans-serif;
        color: #1A1A1A;
    }
    
    /* Main container */
    .main {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 0 10px 40px rgba(0, 149, 255, 0.1);
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
        background: linear-gradient(90deg, #0095FF, #00DDEB);
        -webkit-background-clip: text;
        color: transparent;
        text-shadow: 0 2px 10px rgba(0, 149, 255, 0.3);
        animation: fadeIn 1s ease-in-out;
    }
    
    /* Make tab labels black */
    .stTabs [role="tab"] {
        color: #1A1A1A !important;
        font-weight: 600;
    }
    .stTabs [role="tab"][aria-selected="true"] {
        color: #0095FF !important;
    }
    
    /* Input field with subtle glow */
    .stTextInput > div > div > input {
        background: rgba(245, 249, 255, 0.9);
        color: #1A1A1A;
        border: 2px solid #D6E6FF;
        border-radius: 12px;
        padding: 0.9rem;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        width: 85%; /* Leave space for eye button */
    }
    .stTextInput > div > div > input:focus {
        border-color: #0095FF;
        box-shadow: 0 0 15px rgba(0, 149, 255, 0.5);
    }
    
    /* Eye button styling */
    .eye-button {
        position: absolute;
        right: 10px;
        top: 50%;
        transform: translateY(-50%);
        background: none;
        border: none;
        cursor: pointer;
        font-size: 1.2rem;
        color: #0095FF;
        transition: color 0.3s ease;
    }
    .eye-button:hover {
        color: #00DDEB;
    }
    
    /* Cooler Button Design with Pulsating Glow */
    .stButton > button {
        font-size: 1em;
        padding: 0.7em 1.4em;
        border-radius: 0.7em;
        border: none;
        background: linear-gradient(135deg, #0095FF, #00DDEB);
        color: #FFFFFF;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 6px 20px rgba(0, 149, 255, 0.5);
        animation: pulse 2s infinite;
    }
    .stButton > button::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: rgba(255, 255, 255, 0.3);
        transform: rotate(30deg);
        transition: all 0.5s ease;
        pointer-events: none;
    }
    .stButton > button:hover::before {
        top: 100%;
        left: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 30px rgba(0, 149, 255, 0.7);
    }
    .stButton > button:active {
        transform: translateY(2px);
        box-shadow: 0 4px 15px rgba(0, 149, 255, 0.4);
    }
    
    /* Strength meter with light blue accents */
    .strength-meter {
        background: rgba(245, 249, 255, 0.9);
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 2rem;
        display: flex;
        align-items: center;
        gap: 1.5rem;
        box-shadow: 0 0 20px rgba(0, 149, 255, 0.2);
        animation: slideIn 0.5s ease-out;
    }
    .strength-label {
        font-size: 1.3rem;
        font-weight: 600;
        min-width: 100px;
        color: #1A1A1A;
        text-shadow: 0 0 5px rgba(0, 149, 255, 0.5);
    }
    .score-bar {
        flex-grow: 1;
        height: 14px;
        background: #D6E6FF;
        border-radius: 7px;
        overflow: hidden;
        box-shadow: inset 0 0 5px rgba(0, 149, 255, 0.2);
    }
    .score-fill {
        height: 100%;
        transition: width 0.5s ease-in-out, background-color 0.5s ease-in-out;
        box-shadow: 0 0 10px rgba(0, 149, 255, 0.3);
    }
    
    /* Feedback box with light blue gradient border */
    .feedback-box {
        background: rgba(245, 249, 255, 0.9);
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 2rem;
        color: #1A1A1A;
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
        background: linear-gradient(90deg, #0095FF, #00DDEB);
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
    @keyframes pulse {
        0% { box-shadow: 0 6px 20px rgba(0, 149, 255, 0.5); }
        50% { box-shadow: 0 6px 20px rgba(0, 149, 255, 0.8); }
        100% { box-shadow: 0 6px 20px rgba(0, 149, 255, 0.5); }
    }
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
        
        # Tab 1: Password Checker with Eye Button
        with tab1:
            # Use a container to position the input and eye button
            col1, col2 = st.columns([9, 1])
            with col1:
                if "show_password" not in st.session_state:
                    st.session_state.show_password = False
                password_type = "default" if st.session_state.show_password else "password"  # Changed "text" to "default"
                password = st.text_input("", placeholder="Enter your password", type=password_type, key="password_input")
            with col2:
                eye_icon = "👁️" if not st.session_state.show_password else "👁️‍🗨️"
                if st.button(eye_icon, key="toggle_password", help="Toggle password visibility"):
                    st.session_state.show_password = not st.session_state.show_password
                    st.rerun()  # Rerun to update the input type
            
            analyze = st.button("Analyze", key="analyze_button")
            
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
            generate = st.button("Generate", key="generate_button")
            
            if generate:
                new_password = generate_password(length)
                st.code(new_password, language="text")
                st.markdown('<div class="feedback-box"><p style="font-weight: 600;">Copy this and test it in the checker!</p></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()