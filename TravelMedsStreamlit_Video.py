"""first prototype for a website that could show the innovation"""
import pandas as pd
import streamlit as st

df = pd.read_csv("/home/valentin_werner/Team2_BPI/DrugBank_AvailableOnly.csv")

st.title("TravelMeds - Your travel health care buddy :pill:")
st.subheader("Find the medication you are familiar with in foreign countries")

home = st.selectbox("From which country do you know this medication?", tuple(df.country.unique())) #select home country

arr = df[df.country == home]["product"].unique().tolist() #returns list of every product known in that home country
arr.sort() #sort alphabetically so its easier to navigate
meds = tuple(arr) #necessary for streamlit, medication selecter

if home != 0: #only loads after selecting home
    med = st.selectbox("What medication are you familiar with?", meds) #select medication
    place = st.selectbox("In which country are you looking for a similar product?", tuple(df.country.unique())) #select foreign country

if med != "" and home != "" and place != "":
    drugs = df[(df["product"] == med) & (df.country == home)]["drug"].unique() #find key chemical / drug based on product name
    if len(drugs) == 0:
        st.text("Sorry, we cannot find a fitting medication in our data base") #if there are no products with that chemical / drug in the foreign country
    else:
        for drug in drugs:
            final_prods = []
            prod = df[(df["drug"] == drug) & (df.country == place)]["product"].unique() #only return every possible product once
            for i in prod:
                final_prods.append(i) #create proper list for final products
        if len(final_prods) == 0: #in case there are fitting no products in the place they are at
            st.text(f"Sorry, we cannot find a fitting medication in our data base. However, the relevant ingredient you are looking for is either of these: {drugs}!")
        else: st.text(f"You should ask for any of these products: \n{final_prods}!") #should return top3 + confidence score (based on other variables, such as dosis, form, etc.)
else: print("Please enter values for the medication, the country you know it from and the country you are looking at")