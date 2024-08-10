import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import time
import pandas as pd
import streamlit as st
import mysql.connector

#kerala route
kerala_list=[]

df_k=pd.read_csv("kerala_routes.csv")
for i,r in df_k.iterrows():
    k=r["Route_name"]
    kerala_list.append(k)



#Andhra route
andhra_list=[]

df_a=pd.read_csv("andhra_routes.csv")
for i,r in df_a.iterrows():
    a=r["Route_name"]
    andhra_list.append(a)


#Telangana route
Telangana_list=[]

df_t=pd.read_csv("telanga_routes.csv")
for i,r in df_t.iterrows():
    t=r["Route_name"]
    Telangana_list.append(t)


#Rajasthan route
Rajasthan_list=[]

df_r=pd.read_csv("rajasthan_route.csv")
for i,r in df_r.iterrows():
    R=r["Route_name"]
    Rajasthan_list.append(R)


#Goa route
Goa_list=[]

df_g=pd.read_csv("goa_route.csv")
for i,r in df_g.iterrows():
    g=r["Route_name"]
    Goa_list.append(g)


#Assam route

Assam_list=[]

df_a=pd.read_csv("assam_route.csv")
for i,r in df_a.iterrows():
    a=r["Route_name"]
    Assam_list.append(a)


#Chandigarh route

Chandigarh_list=[]

df_c=pd.read_csv("Chandigarh.csv")
for i,r in df_c.iterrows():
    c=r["Route_name"]
    Chandigarh_list.append(c)



#Uttrapradesh route

Uttrapradesh_list=[]

df_up=pd.read_csv("Uttrapradesh.csv")
for i,r in df_up.iterrows():
    up=r["Route_name"]
    Uttrapradesh_list.append(up)


#westbengal route

Westbengal_list=[]

df_wb=pd.read_csv("westbengal_route.csv")
for i,r in df_wb.iterrows():
    wb=r["Route_name"]
    Westbengal_list.append(wb)


#southbengal route

southbengal_list=[]

df_sb=pd.read_csv("south_bengal_route.csv")
for i,r in df_sb.iterrows():
    sb=r["Route_name"]
    southbengal_list.append(sb)

#read the final csv fileel

df=pd.read_csv("Finaldata.csv")


import streamlit as st
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu

# Set the layout for the Streamlit app
st.set_page_config(layout="wide")

st.image(r"c:/Users/sandh/Downloads/buspic-removebg-preview.png", width=80)

    # Display the main title
st.markdown("<h1 style='display: flex; align-items: center; font-size: 27px; margin: 0;'>RED BUS SCRAPED DATA</h1>", unsafe_allow_html=True)

# Sidebar menu for navigation
with st.sidebar:
    selected = option_menu(
        "Menu", ["Home", "Search Buses"], 
        icons=["house", "bus"],
        menu_icon="menu-button-wide",
        default_index=0,
        styles={
            "nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#f7f7f7"},
            "nav-link-selected": {"background-color": "#FF4B4B"}})
if selected == "Home":
    st.write("Welcome to the Red Bus Scraped Data app!")
    st.write("""redBus is India’s largest online bus ticketing platform that has transformed bus travel in the 
             country by bringing ease and convenience to millions of Indians who travel using buses. Founded 
             in 2006, redBus is part of India’s leading online travel company MakeMyTrip Limited (NASDAQ: MMYT). 
             By providing widest choice, superior customer service, lowest prices and unmatched benefits, 
             redBus has served over 18 million customers. redBus has a global presence with operations across 
            Indonesia, Singapore, Malaysia, Colombia and Peru apart from India.""")
    st.header("NOW, GET MORE THAN JUST BUS TICKETS WITH REDBUS!")
    if st.button('Open RedBus Tickets'):
        st.markdown('<a href="https://www.redbus.in/" target="_blank">Click here to open RedBus Tickets</a>', unsafe_allow_html=True)
    # Button to open the link
    
    st.write("Book IRCTC Train Tickets on redRail simple & superfast booking process with no service fee + no payment gateway charge.")
    st.write("1.Authorised IRCTC Partner")
    st.write("2.Instant refunds on UPI payments")
    st.write("3.Hassle- free customer support")
    if st.button('Open RedBus Railways'):
        st.markdown('<a href="https://www.redbus.in/railways" target="_blank">Click here to open RedBus Railways</a>', unsafe_allow_html=True)
    if st.button('⬇️ Download Red Bus App on Google Play'):
        st.markdown('<a href="https://play.google.com/store/apps/details?id=in.redbus.android&hl=en_IN&gl=US&pli=1" target="_blank">Click here to Download the Red Bus App</a>', unsafe_allow_html=True)
    



elif selected == "Search Buses":
    # Page layout for search
    col1, col2,col3 = st.columns(3)

    with col1:
        
        # Select state
        state = st.selectbox("Select State", ["Kerala", "Andhra Pradesh", "Telangana", "Goa", "Rajasthan", 
                                              "South Bengal", "Chandigarh", "Assam", "Uttar Pradesh", "West Bengal"])
    
    with col1:    
        # Select route based on the selected state
        if state == "Kerala":
            route_name = st.selectbox("Select The Route", kerala_list)
        elif state == "Andhra Pradesh":
            route_name = st.selectbox("Select The Route", andhra_list)
        elif state == "Telangana":
            route_name = st.selectbox("Select The Route", Telangana_list)
        elif state == "Goa":
            route_name = st.selectbox("Select The Route", Goa_list)
        elif state == "Rajasthan":
            route_name = st.selectbox("Select The Route", Rajasthan_list)
        elif state == "South Bengal":
            route_name = st.selectbox("Select The Route", southbengal_list)
        elif state == "Chandigarh":
            route_name = st.selectbox("Select The Route", Chandigarh_list)
        elif state == "Assam":
            route_name = st.selectbox("Select The Route", Assam_list)
        elif state == "Uttar Pradesh":
            route_name = st.selectbox("Select The Route",Uttrapradesh_list)
        elif state == "West Bengal":
            route_name = st.selectbox("Select The Route", Westbengal_list)
        
    
    with col1:
        # Select price range
        price = st.radio("Select Price", ["40-500", "500-1000", "1000-3000", "above 3000"])
        
       

    def fetch_bus_data(state, route_name, price_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="Sandy@2914", database="CAPSTONE1")
        my_cursor = conn.cursor()

        # Determine the price range
        if price_range == "40-500":
            min_price, max_price = 40, 500
        elif price_range == "500-1000":
            min_price, max_price = 500, 1000
        elif price_range == "1000-3000":
            min_price, max_price = 1000, 3000
        else:
            min_price, max_price = 3000, 20000

        # SQL Query to fetch data based on selected filters
        query = '''
                SELECT * FROM redbus_table
                WHERE Price BETWEEN %s AND %s
                AND Route_name = %s
                ORDER BY Price;
        '''

        my_cursor.execute(query, (min_price, max_price, route_name))
        out = my_cursor.fetchall()
        conn.close()

        # Convert the fetched data to a DataFrame
        df = pd.DataFrame(out, columns=[
            "Id", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
            "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
        ])

        return df

    # Assuming you have already gathered `price` and `route_name` earlier in your code.
    if route_name:
        df_data = fetch_bus_data(state, route_name, price)
        st.dataframe(df_data)
