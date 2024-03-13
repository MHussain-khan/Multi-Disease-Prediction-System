import json
import pickle
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


#loading the saved models 

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# sidebar for navigation

with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',
                           ['Health Assistant','Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],

                            icons = ['activity','heart','person'],

                            default_index = 0)
    
#welcome Page

if(selected == 'Health Assistant'):
    def load_lottiefile(filepath:str):
        with open(filepath,"r") as f:
            return json.load(f)
        
    def load_lottieurl(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    

    
    st.title('Welcome to Health Assistant')
    lottie_health2 = load_lottiefile("lottie_animation.json")
    
    # st_lottie(
    #     lottie_health,
    #     speed=1,
    #     loop=True,
    #     height=100,
    #     width=100,
        
    # )
    st_lottie(
        lottie_health2,
        height=100,
        width=100,
        
    )
    st.header('  Health Assistant  help you to Predict you have disease or not')
    st.subheader('Steps to use Health Assistant')
    st.divider()
    st.write('Kindly choose the disease you want to check in the option menu ')
    st.write('Enter the required fields for diagnosis')
    st.write('Press the check button')
    st.write('Result will be displayed')
    st.divider()

    
#Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    #defining lottie
    def load_lottiefile(filepath:str):
        with open(filepath,"r") as f:
            return json.load(f)
    #page title
    st.title('Diabetes Prediction using ML')
    lottie_diab = load_lottiefile("lottie_animation2.json")
    st_lottie(
        lottie_diab,
        height=150,
        width=150
    )


    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies')
    with col2:
        Glucose = st.number_input('Number of Glucose')
    with col3:
        BloodPressure = st.number_input('Number of BloodPressure')
    with col1:
        SkinThickness = st.number_input('Number of SkinThickness')
    with col2:
        Insulin = st.number_input('Number of Insulin')
    with col3:
        BMI = st.number_input('Number of BMI')
    with col1:
        DiabetesPedigreeFunction = st.number_input('Number of DiabetesPedigreeFunction')
    with col2:
        Age = st.number_input('Age')

        #code for prediction
        diab_diagnosis = ''

        #creating button
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
            if(diab_prediction[0]==1):
                diab_diagnosis = 'The Person is diabetic'

            else:
                diab_diagnosis = 'The Person is not diabetic'

        st.success(diab_diagnosis)






    

#Heart disease Page

if(selected == 'Heart Disease Prediction'):
        #defining lottie
    def load_lottiefile(filepath:str):
        with open(filepath,"r") as f:
            return json.load(f)
    st.title('Heart Disease Prediction using ML')

    lottie_heart = load_lottiefile("lottie_animation3.json")
    st_lottie(
        lottie_heart,
        height=150,
        width=150
    )


    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age')
    with col2:
        sex = st.number_input('Sex')
    with col3:
        cp = st.number_input('Chest Pain Types')
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
    with col2:
        chol = st.number_input('Cholestrol')
    with col3:
        fbs = st.number_input('Fasting Blood Sugar')
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.number_input('Maximum Heart rate Achieved')
    with col3:
        exang = st.number_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        #code for prediction
        heart_diagnosis = ''

        #creating button
        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
            if(heart_prediction[0]==1):
                heart_diagnosis = 'The Person has heart disease'

            else:
                heart_diagnosis = 'The Person does not has heart disease'

        st.success(heart_diagnosis)
        

if(selected == 'Parkinsons Prediction'):
    #defining lottie
    def load_lottiefile(filepath:str):
        with open(filepath,"r") as f:
            return json.load(f)
    st.title("Parkinsons Disease prediction")

    lottie_Parkinsons = load_lottiefile("Animation.json")
    st_lottie(
        lottie_Parkinsons,
        height=150,
        width=150
    )



    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.number_input('MDVP:RAP')

    with col2:
        PPQ = st.number_input('MDVP:PPQ')

    with col3:
        DDP = st.number_input('Jitter:DDP')

    with col4:
        Shimmer = st.number_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.number_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.number_input('Shimmer:APQ5')

    with col3:
        APQ = st.number_input('MDVP:APQ')

    with col4:
        DDA = st.number_input('Shimmer:DDA')

    with col5:
        NHR = st.number_input('NHR')

    with col1:
        HNR = st.number_input('HNR')

    with col2:
        RPDE = st.number_input('RPDE')

    with col3:
        DFA = st.number_input('DFA')

    with col4:
        spread1 = st.number_input('spread1')

    with col5:
        spread2 = st.number_input('spread2')

    with col1:
        D2 = st.number_input('D2')

    with col2:
        PPE = st.number_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs,RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])


        if(parkinsons_prediction[0]==1):
                parkinsons_diagnosis = 'The Person has Parkinsons disease'

        else:
                parkinsons_diagnosis = 'The Person does not has Parkinsons disease'

    st.success(parkinsons_diagnosis)


    


 