# 🏋️‍♂️ FitSport AI

**FitSport AI** is a comprehensive AI-powered fitness assistant built using **Streamlit**, offering features such as workout tracking, real-time training with pose detection, nutrition analysis, video tutorials, and an interactive chatbot to guide users through personalized workout routines.

---
## 🚀 Features

### 🔐 Authentication
- Secure login/signup using Firebase Authentication.
- Session management with persistent user tracking.

### 🏠 Home Page
- Introduction to FitSport AI with engaging Lottie animations.
- Links to motivational **music** and **podcasts**.
- Contact form to reach the developer.

### 📘 Tutorials
- Exercise-specific video tutorials with images and links.
- Tutorials included:
  - Bicep Curls
  - Squats
  - Pushups
  - Shoulder Press

### 🏃 AI-Powered Training
- Real-time webcam-based posture tracking using **cvzone PoseModule** and **OpenCV**.
- Repetition counter and live form feedback.
- Calorie burn estimation based on user's body weight and reps.
- Supported exercises:
  - Left Dumbbell
  - Right Dumbbell
  - Squats
  - Pushups
  - Shoulder Press
- Visual feedback and analytics with **Plotly**.

### 🍎 Nutrition Tracker
- Interactive food selection from a dataset with calories per serving.
- Pie chart visualization of calorie distribution using Plotly.

### 👟 Workout History
- Stores user-specific workouts in Firebase Firestore.
- Displays history with dates, reps, calories burned, and goal comparison.
- Insights:
  - Total workouts
  - Total calories burned
  - Calories vs Goal Bar Chart
  - Exercise distribution pie chart

### 🤖 AI Chatbot - "Donnie"
- Built using **Gemini AI API** (Google Generative AI).
- Friendly fitness assistant to help build personalized workout plans.
- Maintains a conversational tone and memory of the chat.
---
## 📂 Project Structure

```plaintext
.
├── 1_🏠_HomePage.py         # Landing page with authentication and intro
├── /pages/
    ├── 2_📘_Tutorials.py        # Workout video tutorials
    ├── 3_🏃_Train.py            # Live exercise detection & training
    ├── 4_🤖_Chatbot.py          # Gemini-powered fitness assistant
    ├── 5_🍎_Nurition.py         # Nutrition calorie tracking
    ├── 6_👟_WorkoutHistory.py   # Progress analytics from Firestore
├── /images/                # Static images used in the app
├── /gif/                   # Animated exercise gifs
├── /styles/                # Custom CSS styling
└── food1.csv               # Nutrition data file

```
---
## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit, Plotly, Matplotlib, Lottie  
- **AI/ML & CV:** OpenCV, Pose Detection (cvzone)  
- **Authentication & Database:** Firebase, Firestore  
- **Chatbot:** Gemini AI (Google Generative AI)  
- **Data Visualization:** Plotly, Pandas, NumPy  

---

## ✅ Prerequisites

- Python 3.8+
- Webcam access for training module
- Firebase Project Setup
- Gemini API Key

---

## 📦 Installation

```bash
git clone https://github.com/YashPatel5652/FitSportAI.git
cd FitSportAI
pip install -r requirements.txt
```
---
