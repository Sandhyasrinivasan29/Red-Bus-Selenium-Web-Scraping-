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

df=pd.read_csv("finaltable.csv")


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
    col1,col2=st.columns(2)
    with col1:
        st.write("Welcome to the Red Bus Scraped Data app!")
        st.write("""redBus is India’s largest online bus ticketing platform that has transformed bus travel in the 
                country by bringing ease and convenience to millions of Indians who travel using buses. Founded 
                in 2006, redBus is part of India’s leading online travel company MakeMyTrip Limited (NASDAQ: MMYT). 
                By providing widest choice, superior customer service, lowest prices and unmatched benefits, 
                redBus has served over 18 million customers. redBus has a global presence with operations across 
                Indonesia, Singapore, Malaysia, Colombia and Peru apart from India.""")
        st.header("NOW, GET MORE THAN JUST BUS TICKETS WITH REDBUS!")
        st.write("Book IRCTC Train Tickets on redRail simple & superfast booking process with no service fee + no payment gateway charge.")
        st.write("1.Authorised IRCTC Partner")
        st.write("2.Instant refunds on UPI payments")
        st.write("3.Hassle- free customer support")

            

    with col2:
        st.image(r"C:/Users/sandh/OneDrive/Desktop/doditsolutions-bus-booking-clone-app.gif")
        if st.button('Open RedBus Railways'):
                st.markdown('<a href="https://www.redbus.in/railways" target="_blank">Click here to open RedBus Railways</a>', unsafe_allow_html=True)
            
        if st.button('Open RedBus Tickets'):
            st.markdown('<a href="https://www.redbus.in/" target="_blank">Click here to open RedBus Tickets</a>', unsafe_allow_html=True)
        if st.button('⬇️ Download Red Bus App on Google Play'):
            st.markdown('<a href="https://play.google.com/store/apps/details?id=in.redbus.android&hl=en_IN&gl=US&pli=1" target="_blank">Click here to Download the Red Bus App</a>', unsafe_allow_html=True)
        
    
    


elif selected == "Search Buses":
    # Page layout for search
    col1, col2 = st.columns(2)

    with col1:
        # Select state
        state = st.selectbox("Select State", ["Kerala", "Andhra Pradesh", "Telangana", "Goa", "Rajasthan", 
                                              "South Bengal", "Chandigarh", "Assam", "Uttar Pradesh", "West Bengal"])
    
    with col2:    
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
            route_name = st.selectbox("Select The Route", Uttrapradesh_list)
        elif state == "West Bengal":
            route_name = st.selectbox("Select The Route", Westbengal_list)
        
    col1, col2 = st.columns(2)
    
    with col1:
        # Select price range
        price = st.radio("Select Price", ["40-500", "500-1000", "1000-3000", "above 3000"])

    with col2:
        # Select time with a 2-hour gap
        start_time = st.selectbox("Select time", [
            "00:00 to 01:59", "02:00 to 03:59", "04:00 to 05:59", "06:00 to 07:59",
            "08:00 to 09:59", "10:00 to 11:59", "12:00 to 13:59", "14:00 to 15:59",
            "16:00 to 17:59", "18:00 to 19:59", "20:00 to 21:59", "22:00 to 23:59"
        ])
        
        # Map start_time selection to SQL time ranges with a 2-hour gap
        if start_time == "00:00 to 01:59":
            start_time_range = ("00:00:00", "01:59:59")
        elif start_time == "02:00 to 03:59":
            start_time_range = ("02:00:00", "03:59:59")
        elif start_time == "04:00 to 05:59":
            start_time_range = ("04:00:00", "05:59:59")
        elif start_time == "06:00 to 07:59":
            start_time_range = ("06:00:00", "07:59:59")
        elif start_time == "08:00 to 09:59":
            start_time_range = ("08:00:00", "09:59:59")
        elif start_time == "10:00 to 11:59":
            start_time_range = ("10:00:00", "11:59:59")
        elif start_time == "12:00 to 13:59":
            start_time_range = ("12:00:00", "13:59:59")
        elif start_time == "14:00 to 15:59":
            start_time_range = ("14:00:00", "15:59:59")
        elif start_time == "16:00 to 17:59":
            start_time_range = ("16:00:00", "17:59:59")
        elif start_time == "18:00 to 19:59":
            start_time_range = ("18:00:00", "19:59:59")
        elif start_time == "20:00 to 21:59":
            start_time_range = ("20:00:00", "21:59:59")
        elif start_time == "22:00 to 23:59":
            start_time_range = ("22:00:00", "23:59:59")
        else:
            start_time_range = ("00:00:00", "23:59:59")  # Default to include all times

        # Unpack the start_time_range tuple
        start_time_min, start_time_max = start_time_range

    col1,col2 = st.columns(2)   

    with col1:
        Bus_type = st.radio("Select Bus Type", ["A/C", "NON-AC", "ALL"])

   

       

    with col2:
        ratings_min = df["Ratings"].min()
        ratings_max = df["Ratings"].max()

        ratings = st.slider(
            "Select Ratings",
            min_value=ratings_min,
            max_value=ratings_max,
            value=(ratings_min, ratings_max)  # Default value range
    )
        
    def fetch_bus_data(state, route_name, price_range, ratings, Bus_type, start_time_min, start_time_max):
        conn = mysql.connector.connect(host="localhost", user="root", password="nura@29", database="project")
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

        # Extract minimum and maximum ratings from the slider value
        ratings_min, ratings_max = ratings
        
        # Prepare the Bus_type filter for SQL LIKE
        if Bus_type == "A/C":
            Bus_type_filter = "%A/C%"
        elif Bus_type == "NON-AC":
            Bus_type_filter = "%NON-AC%"
        else:
            Bus_type_filter = "%"

        # SQL Query to fetch data based on selected filters
        query = '''
            SELECT * FROM BUS_DATA
            WHERE Price BETWEEN %s AND %s
            AND Ratings BETWEEN %s AND %s
            AND Route_name = %s
            AND Bus_type LIKE %s
            AND Start_time BETWEEN %s AND %s
            ORDER BY Price;
        '''

        # Execute the query with unpacked parameters
        my_cursor.execute(query, (min_price, max_price, ratings_min, ratings_max, route_name, Bus_type_filter, start_time_min, start_time_max))
        out = my_cursor.fetchall()
        conn.close()

        # Convert the fetched data to a DataFrame
        df = pd.DataFrame(out, columns=[
            "Id", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
            "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
        ])

        return df

    # Fetch and display the data
    if route_name:
        df_data = fetch_bus_data(state, route_name, price, ratings, Bus_type, start_time_min, start_time_max)
        st.dataframe(df_data)