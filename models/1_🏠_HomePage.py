import streamlit as st
import firebase_admin
from firebase_admin import auth, credentials, firestore
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import pyrebase 

firebaseConfig = {
    "apiKey": "AIzaSyC7TtgGI5SnxZc4aDZHUd7fWH7M8H2KRsg",
    "authDomain": "your-project-id.firebaseapp.com",
    "databaseURL": "https://your-project-id.firebaseio.com",
    "projectId": "your-project-id",
    "storageBucket": "your-project-id.appspot.com",
    "messagingSenderId": "your-messaging-sender-id",
    "appId": "your-app-id"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

st.set_page_config(page_title="FitSport AI", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("./styles/styles.css")

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_FYx0Ph.json")
music = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ikk4jhps.json")
podcast = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_JjpNLdaKYX.json")


img_contact_form = Image.open("./images/home.jpg")
img_lottie_animation = Image.open("./images/home.jpg")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Welcome to FitSport AI! :wave:")
    st.title("AI Fitness Trainer")
    st.write("Track your workouts, analyze progress, and stay fit!")

# ---- USER AUTHENTICATION ----
choice = st.sidebar.selectbox("Login or Sign up", ["Login", "Sign up"])
email = st.sidebar.text_input("Enter Email")
password = st.sidebar.text_input("Enter Password", type="password")

if choice == "Sign up":
    if st.sidebar.button("Create Account"):
        try:
            user = auth.create_user_with_email_and_password(email, password)  # ✅ Correct method
            st.success("Account Created! Please log in.")
        except Exception as e:
            st.error(f"Error: {e}")

if choice == "Login":
    if st.sidebar.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)  # ✅ Verifies password
            st.success(f"Welcome {email}")
            st.session_state["user_id"] = user["localId"]  # Stores user session
        except Exception as e:
            st.error("Invalid credentials. Please try again.")

if "user_id" in st.session_state:
    st.sidebar.success("Logged in!")
    if st.sidebar.button("Logout"):
        st.session_state.pop("user_id")
        st.success("Logged out successfully!")

# ---- DASHBOARD ----
if "user_id" in st.session_state:
    with st.container():
        st.write("---")
        st.write("## About us :point_down:")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("")
            #st.write("##")
            st.write(
                """
                - We are thrilled to have you here on our platform dedicated to empowering and inspiring individuals on their journey towards a healthier and fitter lifestyle. Whether you're a seasoned fitness enthusiast or just starting your fitness journey, we have everything you need to reach your goals and achieve the best version of yourself.
                
                - What sets us apart is the fact that we provide personalized assistance at the comfort of your home or any place of your choice at a price that is both convenient and much cheaper that traditional gyms.

                Let your fitness journey start here!
                Join us today and embark on a transformative experience that will enhance your physical and mental well-being. Let's build strength, resilience, and a healthier future together!
                """
            )

        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

    # ---- PROJECTS ----
    with st.container():
        st.write("---")
        st.header("Get fit, Jam on, Repeat :headphones:")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            #st.image(img_lottie_animation)
            st_lottie(music, height=300, key="music")
        with text_column:
            st.write("##")
            st.subheader("Workout music")
            st.write(
                """
                Power up your workout with the ultimate music fuel!
                """
            )
            st.markdown("[Have a Listen...](https://open.spotify.com/playlist/6N0Vl77EzPm13GIOlEkoJn?si=9207b7744d094bd3)")
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            #st.image(img_contact_form)
            st_lottie(podcast, height=300, key="podcast")
        with text_column:
            st.write("##")
            st.subheader("Podcast")
            st.write(
                """
                Take your workouts to the next level with our immersive podcast that pumps you up from start to finish!
                """
            )
            st.markdown("[Have a listen...](https://open.spotify.com/playlist/09Ig7KfohF5WmU9RhbDBjs?si=jyZ79y3wQgezrEDHim0NvQ)")

    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/yp1102003@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
else:
    st.write("## Login to access your fitness data.")
