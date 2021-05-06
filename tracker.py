import phonenumbers
import streamlit as st
from phonenumbers import geocoder
from phonenumbers import carrier

def main():
    st.title('Phone Number Location Tracker')
    st.subheader('Build with Python & Streamlit')
    mobile_number = st.text_input("Enter your phone number: ", type="password")
    if st.button('Track'):
        ch_number = phonenumbers.parse(mobile_number,'CH')
        st.success("Country name: {}".format(geocoder.description_for_number(ch_number,"en")))
        services_operator = phonenumbers.parse(mobile_number,'RO')
        st.success("Service Operator: {}".format(carrier.name_for_number(services_operator, "en")))

if __name__=="__main__":
    main()