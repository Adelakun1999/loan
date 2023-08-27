import streamlit as st
import joblib 

import sklearn

model=joblib.load('loan.pkl')

@st.cache()


# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender,Married,ApplicantIncome,LoanAmount,Credit_History):
    if Gender=='Male':
        Gender=1
    else:
        Gender=0

    if Married=="Unmarried":
        Married=0
    else:
        Married=1

    if Credit_History=='Unclear debts':
        Credit_History=0
    else:
        Credit_History=1

    LoanAmount=LoanAmount/1000

    #Making Predictions

    prediction=model.predict([[Gender,Married,ApplicantIncome,LoanAmount,Credit_History]])

    if prediction==0:
        pred='rejected'
    else:
        pred='accepted'
    
    return pred

# this is the main function in which we define our webpage 

def main():

    st.title('Streamlit Loan Prediction ML App')
    Gender=st.selectbox('Gender',('Male','Female'))
    Married=st.selectbox('Marital Status',('Unmarried','Married'))
    ApplicantIncome=st.number_input('Applicant monthly income')
    LoanAmount=st.number_input('Total loan Amount')
    Credit_History=st.selectbox('Credit_History',('Unclear debts','No unclear debts'))
    

    if st.button('Predict'):
        result=prediction(Gender,Married,ApplicantIncome,LoanAmount,Credit_History)
        st.success('Your loan is {}'.format(result))
    
if __name__=='__main__':
    main()