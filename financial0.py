import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pypickle
#Load the model
loaded_model = pypickle.load('Financials.pkl')

#preprocessing
#create a function for the prediction taking in the data(the columns to be entered by the user)

def prediction(data):
     

#create a dataframe for the data 
     df = pd.DataFrame(data)
 #convert the row to numerical form
    
     label = LabelEncoder()
 #Create a list for the categorical columns    
     rowitems = [0,3,4,7,8,9,10,11]

     for i in rowitems:
         df.iloc[i] = label.fit_transform(df.iloc[i])
          #craete a variable that will convert the data to a numpy array and reshape it to a one dimensional
     num_data = df.drop([2]).values.reshape(1,-1)  
 #prediction the model
     pred = loaded_model.predict(num_data)     

     if  pred[0] == 0:
          return "The indivdaul without bank account"
     else:
          return "The individual with bank account"    
     
def main ():
     st.title("Financial Inclusion in Africa Prediction Model")
     country = st.radio("Please select your country",("kenya","Rewanda","Tanzian","Uganda"))
     year = st.radio("Please select your year",("2018","2017","2016"))
     uniqueid = st.number_input("Please enter your id number:")
     location_type = st.radio("please select your location",("Rural","Urban"))
     cellphone_access = st.radio("Please enter cellphone access",("yes","No"))
     household_size = st.number_input("Please enter the size of your household:")
     age_of_respondent = st.number_input("how old are you?:")
     gender_of_respondent = st.radio("Enter your gender", ("male","female"))
     relationship_with_head = st.selectbox("Enter your relationship type:", ('Spouse', 'Head of Household', 'Other relative', 'Child', 'Parent',
       'Other non-relatives'))
     marital_status = st.selectbox("Please enter your marital status:",('Married/Living together', 'Widowed', 'Single/Never Married',
       'Divorced/Seperated', 'Dont know'))
     education_level = st.selectbox("Please enter your educational level:",('Secondary education', 'No formal education',
       'Vocational/Specialised training', 'Primary education',
       'Tertiary education', 'Other/Dont know/RTA'))
     job_type = st.selectbox("Please enter your job type:",('Self employed', 'Government Dependent',
       'Formally employed Private', 'Informally employed',
       'Formally employed Government', 'Farming and Fishing',
       'Remittance Dependent', 'Other Income',
       'Dont Know/Refuse to answer', 'No Income'))
     

     bank_account= ""

     if st.button("Result"):
        bank_account= prediction([country, year, uniqueid, location_type, cellphone_access,household_size, age_of_respondent,gender_of_respondent,
        relationship_with_head, marital_status, education_level, job_type])

        st.success(bank_account)

if  __name__ == "__main__":
            main()

        

     

     
