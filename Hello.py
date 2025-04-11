import streamlit as st

# Exercises Available To Do Classified by Exercise Group
workouts = {
    "Running on Treadmill": (["Cardio"], 15, "Run at a moderate pace for 4 minutes, Sprint for 1 minute, Repeat the cycle until 15 minutes is reached", "https://youtu.be/K6I24WgiiPw?si=cC3ll8dbe8ZgZy3N"),
    "Stairmaster": (["Cardio"], 20, "Climb stairs at a moderate pace until 20 minutes are reached", "https://youtu.be/R5i62iA4ONA?si=SdANKrYXSRv22d8z7"),
    "Cable Row Machine": (["Cardio"], 15, "Row at a moderate pace until 15 minutes are reached", "https://youtu.be/MnGwdJD8enU?si=-FCJzdyMNO_7Mh50"),
    "Jumping Jacks": (["Cardio"], 10, "Do jumping jacks until 10 minutes are reached", "https://youtu.be/uLVt6u15L98?si=x-xbnnX776ht3FWw"),
    "Dumbbell Curl": (["Arms"], 15, "4 Sets of 8-10 Repetitions", "https://youtu.be/XE_pHwbst04?si=mFXuErHdq4GRYxj0"),
    "Cable Tricep Extension": (["Arms"], 15, "4 Sets of 8-10 Repetitions", "https://youtu.be/ns-RGsbzqok?si=ZAUNhkDoy0nBrSsV"),
    "Dumbbell Hammer Curl": (["Arms"], 10, "3 Sets of 8-10 Repetitions", "https://youtu.be/zC3nLlEvin4?si=rxnXLp4oeJZPzuQH"),
    "Cable Tricep Kickback": (["Arms"], 10, "3 Sets of 8-10 Repetitions", "https://youtu.be/ZvF4Oi_6Vtg?si=P-I7bpGlG28_xQKk"),
    "Preacher Curl Machine": (["Arms"], 10, "3 Sets of 8-10 Repetitions", "https://youtu.be/jGhd1pIcQ74?si=wYIhrF1gYvObI_5Y"),
    "Barbell Skullcrusher": (["Arms"], 10, "3 Sets of 8-10 Repetitions", "https://youtu.be/d_KZxkY_0cM?si=AQLOD9tstxUp4nH_"),
    "Dumbbell Bench Press": (["Chest", "Arms"], 20, "4 Sets of 8-10 Repetitions", "https://youtu.be/t1iaVBMItPo?si=WCiHIBO2_AZwqmix"),
    "Incline Press Machine": (["Chest", "Arms"], 20, "4 Sets of 8-10 Repetitions", "https://youtu.be/I_dcachDaRI?si=OpGrm2OvNqz4qIXP"),
    "Push Ups": (["Chest", "Arms"], 10, "4 Sets of 20 Repetitions", "https://youtu.be/IODxDxX7oi4?si=sYsPdg-x6aonaqeo"),
    "Chest Fly Machine": (["Chest"], 15, "3 Sets of 8-10 Repetitions", "https://youtu.be/eGjt4lk6g34?si=QdCHhNrE7qgQuv5g"),
    "Wide Chest Press Machine": (["Chest", "Arms"], 15, "3 Sets of 8-10 Repetitions", "https://youtu.be/Wb2vWUO1GMU?si=QvOQXR2WJqxIh23C"),
    "Low-to-High Cable Flys": (["Chest"], 15, "3 Sets of 8-10 Repetitions", "https://youtu.be/M1N804yWA-8?si=ToqsPM2rxauNYz81"),
    "Dips": (["Chest", "Arms"], 10, "3 Sets of 10 Repetitions", "https://youtu.be/l41SoWZiowI?si=WJ6ZMczWgX37Ztjw"),
    "Lateral Raises": (["Shoulders"], 15, "4 Sets of 8-10 Repetitions", "https://youtu.be/kDqklk1ZESo?si=v_EUwjXhwOMAxy68"),
    "Dumbbell Shoulder Press": (["Shoulders", "Arms"], 20, "4 Sets of 8-10 Repetitions", "https://youtu.be/qEwKCR5JCog?si=FRdXqDsmOgDIet-2"),
    "Front Raises": (["Shoulders"], 10, "3 Sets of 8-10 Repetitions", "https://youtu.be/-t7fuZ0KhDA?si=-UzdmGZ0PcEkR-ns"),
    "Power Cleans": (["Shoulders", "Back"], 20, "4 Sets of 8-10 Repetitions", "https://youtu.be/5vVSGITznQk?si=gMRDSUCGlQtd0Pu8"),
    "Rear Deltoid Fly": (["Shoulders"], 15, "3 Sets of 8-10 Repetitions", "https://youtu.be/EA7u4Q_8HQ0?si=YEnqR_bqyjZU494u"),
    "Cable Face Pulls": (["Shoulders", "Back"], 20, "4 Sets of 8-10 Repetitions", "https://youtu.be/V8dZ3pyiCBo?si=EANM4LE9NkhpHX09"),
    "Pull Ups": (["Back", "Arms"], 15, "4 Sets of 8-10 Repetitions", "https://youtu.be/eGo4IYlbE5g?si=XghM706NA5QmWy2cE"),
    "Deadlift": (["Back", "Legs"], 25, "4 Sets of 8-10 Repetitions", "https://youtu.be/XxWcirHIwVo?si=B1E__ziWpAzLUVaK"),
    "T-Bar Row": (["Back"], 15, "3 Sets of 8-10 Repetitions", "https://youtu.be/ajlRByifoJE?si=9XMpBYvj5rtQ6lbb"),
    "Bent-over Row": (["Back"], 20, "4 Sets of 8-10 Repetitions", "https://youtu.be/FWJR5Ve8bnQ?si=JNtebioROgAJlX6A"),
    "Lat Pulldown Machine": (["Back"], 15, "3 Sets of 8-10 Repetitions", "https://youtu.be/SALxEARiMkw?si=1mQ4oK67KQLJQTKH"),
    "Back Extension": (["Back"], 15, "3 Sets of 8-10 Repetitions", "https://youtu.be/ph3pddpKzzw?si=eHtj8t1GM6rIpRjl"),
    "Back Squat": (["Legs"], 15, "3 Sets of 8-10 Repetitions", "https://youtu.be/VZ90qWlfQUE?si=cOJ_gucOM41o-efu"),
    "Leg Extension Machine": (["Legs"], 15, "3 Sets of 8-10 Repetitions", "https://youtu.be/swZQC689o9U?si=VAq7CjBub8WEd6tc"),
    "Hamstring Curl Machine": (["Legs"], 15, "3 Sets of 8-10 Repetitions", "https://youtu.be/oFxEDkppbSQ?si=sIyxj8iNu0a4Tr1z"),
    "Weighted Calf-Raise": (["Legs"], 15, "4 Sets of 12 Repetitions", "https://youtu.be/wxwY7GXxL4k?si=9xoVpK1sDNK8fKYp"),
    "Weighted Sled": (["Legs", "Cardio"], 20, "Push moderate resistance sled back and forth 5 times", "https://youtu.be/QaTrePoCT4g?si=9177GgCtF2zneGd4"),
    "Romanian Deadlift": (["Legs"], 15, "3 Sets of 8-10 Repetitions", "https://youtu.be/hQgFixeXdZo?si=addDstLkMYR3zWnV"),
    "Bulgarian Split Squat": (["Legs"], 15, "3 Sets of 8-10 Repetitions", "https://youtu.be/hPlKPjohFS0?si=JKcO-N_gkDj88lTc"),
    "Plank": (["Abdominal"], 10, "Hold plank for 1:30 minutes, Rest for 30 seconds, Repeat the cycle until 10 minutes is reached", "https://youtu.be/6LqqeBtFn9M?si=LDegzaZ-z5x3Ztjc"),
    "Sit Ups": (["Abdominal"], 5, "4 Sets of 15 Repetitions", "https://youtu.be/jDwoBqPH0jk?si=LJdxPcxwg-vGTCFZ"),
    "Leg Lifts": (["Abdominal"], 15, "4 Sets of 20 Repetitions", "https://youtu.be/l4kQd9eWclE?si=KZhSCJOjvRlH09X9"),
    "Medicine Ball Slams": (["Abdominal, Cardio"], 15, "4 Sets of 25 Repetitions", "https://youtu.be/QxYhFwMd1Ks?si=Qip0gn5wVYM5j7Kf"),
    "Knee-to-Elbow Crunches": (["Abdominal"], 15, "4 Sets of 25 Repetitions", "https://youtu.be/FcjwuLMdGyM?si=r4yV5RC5Zn0gI3-V"),
    }
import streamlit as st
import streamlit as st

st.markdown("""
    <style>
    .white-heading {
        color: white !important;
        font-size: 24px !important;
        font-weight: bold !important;
        line-height: 1.5 !important;
        margin-bottom: 1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Inject custom CSS
st.markdown("""
    <style>
        /* Set white background */
        .stApp {
            background-color: white;
        }

        html, body, [class*="css"] {
    color: #002B5B; /* Dark blue */
}

h1 {
    color: white !important;
}


        /* Headers - dark blue */
        h1, h2, h3, h4, h5, h6 {
            color: #002B5B !important;
        }

        /* Buttons - blue background, white text */
        .stButton > button {
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 8px;
        }

        .stButton > button:hover {
            background-color: #0056b3;
        }

        /* Text input borders - blue */
        .stTextInput > div > div > input {
            border: 2px solid #007BFF;
            border-radius: 8px;
            color: #002B5B;
        }

        /* Selectbox styling */
        .stSelectbox > div > div {
            border: 2px solid #007BFF;
            border-radius: 8px;
            color: #002B5B;
        }

        /* Markdown text */
        .stMarkdown {
            color: #002B5B;
        }
    </style>
""", unsafe_allow_html=True)



# Displays Exercises Based on User's Inputs 
def exercises(name, time):
    timeLeft = time
    totalTime = 0
    exerciseList = []
    for exerciseName, (exerciseType, exerciseTime, description, tutorial) in workouts.items():
        if name in exerciseType and timeLeft - exerciseTime >= 0:
            exerciseList.append(exerciseName)
            timeLeft -= exerciseTime
            totalTime += exerciseTime
    st.title(name + " Workout in " + str(totalTime) + " Minutes")
    st.header("Exercises:")
    for exercise in exerciseList:
        st.subheader(exercise)
        st.write(workouts[exercise][2])
        st.write("Time of Exercise: " + str(workouts[exercise][1]) + " Minutes")
        st.video(workouts[exercise][3], format="video", start_time=0) #NEW
        st.write("---")
        
# Sidebar for Navigation
# st.sidebar.title("**Workout Generator**")
# # st.sidebar.image("yellowjacket.png")
# st.sidebar.write("Please select a workout type and desired maximum time of workout.")
st.sidebar.markdown(
    '<div class="white-heading">Workout Generator</div>',
    unsafe_allow_html=True
)



st.sidebar.markdown(
    '<span style="color: white;">Please select a workout type and desired maximum time of workout.</span>',
    unsafe_allow_html=True
)


# User's Desired Workout Type
exerciseGroup = st.sidebar.selectbox("**Select an Exercise Group**", ["Cardio", "Chest", "Arms (Triceps and Biceps)", "Shoulders", "Back", "Legs", "Abdominal"]) #NEW

# User's Desired Workout Time
workoutTime = st.sidebar.number_input("**Allowed Time To Exercise (in Minutes)**", min_value=15, value=15) #NEW

# Calls Function Based on User's Inputs
if exerciseGroup == "Cardio":
    exercises("Cardio", workoutTime)
elif exerciseGroup == "Chest":
    exercises("Chest", workoutTime)
elif exerciseGroup == "Arms (Triceps and Biceps)":
    exercises("Arms", workoutTime)
elif exerciseGroup == "Shoulders":
    exercises("Shoulders", workoutTime)
elif exerciseGroup == "Back":
    exercises("Back", workoutTime)
elif exerciseGroup == "Legs":
    exercises("Legs", workoutTime)
elif exerciseGroup == "Abdominal":
    exercises("Abdominal", workoutTime)