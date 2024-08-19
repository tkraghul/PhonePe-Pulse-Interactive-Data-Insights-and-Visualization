import requests
import pandas as pd
import json
import mysql.connector
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

def get_db():
    # Establish connection to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="3690",
        database="phonepe_data"
    )
    # Create a cursor object
    mycursor = mydb.cursor()
    # Return both the connection and cursor
    return mydb, mycursor

    

# Function to load GeoJSON data
def load_geojson():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response = requests.get(url)
    return json.loads(response.content)

# Functions for different visualizations
def transaction_locations_amount_all(Year):
    conn, _ = get_db()
    query = f"SELECT states, SUM(transaction_amount) AS Transaction, SUM(Transaction_count) AS count FROM aggregated_transaction WHERE years={Year} GROUP BY states ORDER BY Transaction DESC"
    df = pd.read_sql(query, conn)
    geojson_data = load_geojson()
    fig = px.choropleth(df, geojson=geojson_data, locations="states", featureidkey="properties.ST_NM",
                        color="Transaction", color_continuous_scale="Sunsetdark", range_color=(0, 400000000000),
                        hover_name="states", title="TRANSACTION AMOUNT")
    fig.update_geos(fitbounds="locations", visible=False)
    conn.close()
    return st.plotly_chart(fig)

def transaction_locations_animation_year(Year, Quarter):
    conn, _ = get_db()
    query = f"SELECT states, SUM(transaction_amount) AS Transaction, SUM(Transaction_count) AS count FROM aggregated_transaction WHERE years={Year} AND quarter={Quarter} GROUP BY states ORDER BY Transaction DESC"
    df = pd.read_sql(query, conn)
    geojson_data = load_geojson()
    fig = px.choropleth(df, geojson=geojson_data, locations="states", featureidkey="properties.ST_NM",
                        color="Transaction", color_continuous_scale="Sunsetdark", range_color=(0, 400000000000),
                        hover_name="states", title="TRANSACTION AMOUNT")
    fig.update_geos(fitbounds="locations", visible=False)
    conn.close()
    return st.plotly_chart(fig)

def transaction_locations_count_all(Year):
    conn, _ = get_db()
    query = f"SELECT states, SUM(transaction_amount) AS Transaction, SUM(Transaction_count) AS count FROM aggregated_transaction WHERE years={Year} GROUP BY states ORDER BY count DESC"
    df = pd.read_sql(query, conn)
    geojson_data = load_geojson()
    fig = px.choropleth(df, geojson=geojson_data, locations="states", featureidkey="properties.ST_NM",
                        color="count", color_continuous_scale="Sunsetdark", range_color=(0, 3000000),
                        hover_name="states", title="TRANSACTION COUNT")
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(title_font_size=20)
    conn.close()
    return st.plotly_chart(fig)

def transaction_count_animation_year(Year, Quarter):
    conn, _ = get_db()
    query = f"SELECT states, SUM(transaction_amount) AS Transaction, SUM(Transaction_count) AS count FROM aggregated_transaction WHERE years={Year} AND quarter={Quarter} GROUP BY states ORDER BY count DESC"
    df = pd.read_sql(query, conn)
    geojson_data = load_geojson()
    fig = px.choropleth(df, geojson=geojson_data, locations="states", featureidkey="properties.ST_NM",
                        color="count", color_continuous_scale="Sunsetdark", range_color=(0, 400000000000),
                        hover_name="states", title="TRANSACTION COUNT")
    fig.update_geos(fitbounds="locations", visible=False)
    conn.close()
    return st.plotly_chart(fig)

def payment_transc_type_amount(Year):
    conn, _ = get_db()
    query = f"SELECT transaction_name, SUM(transaction_amount) AS Amount FROM aggregated_transaction WHERE years={Year} GROUP BY transaction_name ORDER BY Amount DESC"
    df = pd.read_sql(query, conn)
    fig = px.bar(df, x="transaction_name", y="Amount", title="TRANSACTION TYPE and TRANSACTION AMOUNT",
                 color_discrete_sequence=px.colors.sequential.Blues_r)
    fig.update_layout(width=600, height=500)
    conn.close()
    return st.plotly_chart(fig)

def payment_transc_type_all_amount(Year, Quarter):
    conn, _ = get_db()
    query = f"SELECT transaction_name, SUM(transaction_amount) AS Amount FROM aggregated_transaction WHERE years={Year} AND quarter={Quarter} GROUP BY transaction_name ORDER BY Amount DESC"
    df = pd.read_sql(query, conn)
    fig = px.bar(df, x="transaction_name", y="Amount", title="TRANSACTION TYPE and TRANSACTION AMOUNT",
                 color_discrete_sequence=px.colors.sequential.Blues_r)
    fig.update_layout(width=600, height=500)
    conn.close()
    return st.plotly_chart(fig)

def registered_user(Year):
    conn, _ = get_db()
    query = f"SELECT states, SUM(registerd_users) AS Users FROM map_user WHERE years={Year} GROUP BY states ORDER BY Users DESC"
    df = pd.read_sql(query, conn)
    geojson_data = load_geojson()
    fig = px.choropleth(df, geojson=geojson_data, locations="states", featureidkey="properties.ST_NM",
                        color="Users", color_continuous_scale="Sunsetdark", range_color=(0, 400000000000),
                        hover_name="states", title="REGISTERED USERS")
    fig.update_geos(fitbounds="locations", visible=False)
    conn.close()
    return st.plotly_chart(fig)

def registered_user_all(Year, Quarter):
    conn, _ = get_db()
    query = f"SELECT states, SUM(registerd_users) AS Users FROM map_user WHERE years={Year} AND quarter={Quarter} GROUP BY states ORDER BY Users DESC"
    df = pd.read_sql(query, conn)
    geojson_data = load_geojson()
    fig = px.choropleth(df, geojson=geojson_data, locations="states", featureidkey="properties.ST_NM",
                        color="Users", color_continuous_scale="Sunsetdark", range_color=(0, 400000000000),
                        hover_name="states", title="REGISTERED USERS")
    fig.update_geos(fitbounds="locations", visible=False)
    conn.close()
    return st.plotly_chart(fig)

def payment_transc_type_count(Year):
    conn, _ = get_db()
    query = f"SELECT transaction_name, SUM(transaction_count) AS Count FROM aggregated_transaction WHERE years={Year} GROUP BY transaction_name ORDER BY Count DESC"
    df = pd.read_sql(query, conn)
    fig = px.bar(df, x="transaction_name", y="Count", title="TRANSACTION TYPE and TRANSACTION COUNT",
                 color_discrete_sequence=px.colors.sequential.Blues_r)
    fig.update_layout(width=600, height=500)
    conn.close()
    return st.plotly_chart(fig)

def payment_transc_type_count_all(Year, Quarter):
    conn, _ = get_db()
    query = f"SELECT transaction_name, SUM(transaction_count) AS Count FROM aggregated_transaction WHERE years={Year} AND quarter={Quarter} GROUP BY transaction_name ORDER BY Count DESC"
    df = pd.read_sql(query, conn)
    fig = px.bar(df, x="transaction_name", y="Count", title="TRANSACTION TYPE and TRANSACTION COUNT",
                 color_discrete_sequence=px.colors.sequential.Blues_r)
    fig.update_layout(width=600, height=500)
    conn.close()
    return st.plotly_chart(fig)

# Setting the Streamlit application
st.set_page_config(page_title="PhonePe Visualization", layout="wide")

# Define the background style with purple and black combination
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-color: #000000; /* Black background */
    color: #FFFFFF; /* White text for better readability */
}
[data-testid="stSidebar"] {
    background-color: #4B0082; /* Dark purple for sidebar */
}
[data-testid="stHeader"] {
    background-color: #6A0D91; /* Lighter purple for header */
}
</style>
'''

# Apply the background style
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: violet;'>PhonePe Pulse Data Insights</h1>", unsafe_allow_html=True)
st.subheader(":black[This is a User-Friendly Tool to know the insights about PhonePe]")

SELECT = option_menu(
        menu_title = None,
        options = ["About","Top Insights","Facts"],
        icons =["house","map","bar-chart"],
        default_index=2,
        orientation="horizontal",
        styles={"container": {"padding": "0!important", "background-color": "white","size":"cover", "width": "100%"},
                "icon": {"color": "black", "font-size": "20px"},
                "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#9334CD"},
                "nav-link-selected": {"background-color": "#9334CD"}})
if SELECT=="About":
        col1, col2 = st.columns(2)
        with col1:
                st.header("**PhonePe**")
                st.subheader("_India's Best Transaction App_")
                st.write("""_PhonePe is a digital wallet and mobile payment platform in India.It uses the Unified Payment Interface (UPI) system to allow users to send and receive money recharge mobile, DTH, data cards,make utility payments,pay at shops,invest in tax saving funds,buy insurance, mutual funds and digital gold._""")
                st.write("****FEATURES****")
                st.write("   **- Fund Transfer**")
                st.write("   **- Payment to Merchant**")
                st.write("   **- Recharge and Bill payments**")
                st.write("   **- Autopay of Bills**")
                st.write("   **- Cashback and Rewards and much more**")
                st.link_button(":violet[**DOWNLOAD THE APP NOW**]", "https://www.phonepe.com/app-download/")
        
        with col2:
                st.subheader("Video about PhonePe")
                st.video("https://youtu.be/aXnNA4mv1dU?si=HnSu_ETm4X29Lrvf")
                st.write("***To know more about PhonePe click below***")
                st.link_button(":violet[**PhonePe**]", "https://www.phonepe.com/")

if SELECT == "Top Insights":
    listTabs = ["***Transaction Amount***", "***Transaction Count***", "***PhonePe Users***", "***Transaction Type***"]
    whitespace = 33
    tabs = st.tabs([s.center(whitespace, "\u2001") for s in listTabs])
    
    # Tab 1: Transaction Amount
    with tabs[0]:
        Year = st.selectbox("Year", ("Select Year to know Transaction Amount", 2018, 2019, 2020, 2021, 2022))
        Quarter = st.selectbox("Quarter", ("Select Quarter to know Transaction Amount", "All", 1, 2, 3, 4))
        if Year != "Select Year" and Quarter == "All":
            transaction_locations_amount_all(Year)
        elif Quarter in [1, 2, 3, 4]:
            transaction_locations_animation_year(Year, Quarter)
    
    # Tab 2: Transaction Count
    with tabs[1]:
        Year = st.selectbox("Year", ("Select to know Transaction Count", 2018, 2019, 2020, 2021, 2022))
        Quarter = st.selectbox("Quarter", ("Select Quarter to know Transaction Count", "All", 1, 2, 3, 4))
        if Year != "Select" and Quarter == "All":
            transaction_locations_count_all(Year)
        elif Quarter in [1, 2, 3, 4]:
            transaction_count_animation_year(Year, Quarter)
    
    # Tab 3: PhonePe Users
    with tabs[2]:
        Year = st.selectbox("Year", ("Select Year to know about Users", 2018, 2019, 2020, 2021, 2022))
        Quarter = st.selectbox("Quarter", ("Select Quarter to know about Users", "All", 1, 2, 3, 4))
        if Year != "Select" and Quarter == "All":
            registered_user(Year)
        elif Quarter in [1, 2, 3, 4]:
            registered_user_all(Year, Quarter)
    
    # Tab 4: Transaction Type
    with tabs[3]:
        col1, col2 = st.columns(2)
        
        with col1:
            Year = st.selectbox("Year", ("Select Year to know transaction Type Amount", 2018, 2019, 2020, 2021, 2022))
            Quarter = st.selectbox("Quarter", ("Select Quarter to know Transaction Type Amount", "All", 1, 2, 3, 4))
            if Year != "Select" and Quarter == "All":
                payment_transc_type_amount(Year)
            elif Quarter in [1, 2, 3, 4]:
                payment_transc_type_all_amount(Year, Quarter)
        
        with col2:
            Year = st.selectbox("Year", ("Select Year to know transaction Type Count", 2018, 2019, 2020, 2021, 2022))
            Quarter = st.selectbox("Quarter", ("Select Quarter to know Transaction Type Count", "All", 1, 2, 3, 4))
            if Year != "Select" and Quarter == "All":
                payment_transc_type_count(Year)
            elif Quarter in [1, 2, 3, 4]:
                payment_transc_type_count_all(Year, Quarter)


if SELECT == "Facts":
    st.subheader("Choose the options below to know about facts of the data_")
    options = st.selectbox(":violet[_Insights_]", ("---------------------------------------------------------------------------------------------Select The Facts You Want To Know-------------------------------------------------------------------------------------------",
                        "Top 10 District With Lowest Transaction Amount",
                        "Top 10 District With Highest Transaction Amount",
                        "PhonePe users from 2018 to 2023",
                        "Top 10 States with Highest PhonePe User",
                        "Top 10 States with Lowest PhonePe User",
                        "Top 10 Districts with Highest PhonePe User",
                        "Top 10 Districts with Lowest PhonePe User",
                        "Top 10 District with Highest Transaction Count",
                        "Top 10 District With Lowest Transaction Count",
                        ))
    mydb, mycursor = get_db()


    
    if options == "Top 10 District With Lowest Transaction Amount":
        Year = st.selectbox("Year", ("Select Year for lowest transaction", 2018, 2019, 2020, 2021, 2022))
        if Year != "Select Year for lowest transaction":
            query2 = (f"select district_name, sum(district_amount) as Amount from map_transaction where years={Year} group by district_name order by Amount asc")
            mycursor.execute(query2)
            table = mycursor.fetchall()
            table2 = pd.DataFrame(table, columns=["District", "Transaction Amount"])
            tab = table2.head(10)
            fig = px.pie(tab, values="Transaction Amount", names="District", title="Top 10 Lowest Transactions")
            st.plotly_chart(fig)
    elif options == "Top 10 District With Highest Transaction Amount":
        Year = st.selectbox("Year", ("Select Year for highest transaction", 2018, 2019, 2020, 2021, 2022))
        if Year != "Select Year for highest transaction":
            query3 = (f"select district_name, sum(district_amount) as Amount from map_transaction where years={Year} group by district_name order by Amount desc")
            mycursor.execute(query3)
            table = mycursor.fetchall()
            table2 = pd.DataFrame(table, columns=["District", "Transaction Amount"])
            tab = table2.head(10)
            fig = px.pie(tab, values="Transaction Amount", names="District", title="Top 10 Highest Transactions")
            st.plotly_chart(fig)
    elif options == "PhonePe users from 2018 to 2023":
        query4 = ("select years, sum(registerd_users) as users from map_user group by years order by years")
        mycursor.execute(query4)
        table = mycursor.fetchall()
        table2 = pd.DataFrame(table, columns=["Years", "PhonePe Users"])
        fig = px.line(table2, x="Years", y="PhonePe Users", title="No. of Users")
        st.plotly_chart(fig)
    elif options == "Top 10 States with Highest PhonePe User":
        Year = st.selectbox("Year", ("Select Year for highest PhonePe User", 2018, 2019, 2020, 2021, 2022))
        if Year != "Select Year for highest PhonePe User":
            query5 = (f"select states, sum(registerd_users) as users from map_user where years={Year} group by states order by users desc")
            mycursor.execute(query5)
            table = mycursor.fetchall()
            table2 = pd.DataFrame(table, columns=["State", "Registered Users"])
            tab = table2.head(10)
            fig = px.pie(tab, values="Registered Users", names="State", title="Top 10 Highest PhonePe Users")
            st.plotly_chart(fig)
    elif options == "Top 10 States with Lowest PhonePe User":
        Year = st.selectbox("Year", ("Select Year for lowest PhonePe User", 2018, 2019, 2020, 2021, 2022))
        if Year != "Select Year for lowest PhonePe User":
            query5 = (f"select states, sum(registerd_users) as users from map_user where years={Year} group by states order by users asc")
            mycursor.execute(query5)
            table = mycursor.fetchall()
            table2 = pd.DataFrame(table, columns=["State", "Registered Users"])
            tab = table2.head(10)
            fig = px.pie(tab, values="Registered Users", names="State", title="Top 10 Lowest PhonePe Users")
            st.plotly_chart(fig)
    elif options == "Top 10 Districts with Highest PhonePe User":
        Year = st.selectbox("Year", ("Select Year for highest PhonePe User", 2018, 2019, 2020, 2021, 2022))
        if Year != "Select Year for highest PhonePe User":
            query3 = (f"select district_name, sum(registerd_users) as users from map_user where years={Year} group by district_name order by users desc")
            mycursor.execute(query3)
            table = mycursor.fetchall()
            table2 = pd.DataFrame(table, columns=["District", "Registered Users"])
            tab = table2.head(10)
            fig = px.pie(tab, values="Registered Users", names="District", title="Top 10 Highest PhonePe Users")
            st.plotly_chart(fig)
    elif options == "Top 10 Districts with Lowest PhonePe User":
        Year = st.selectbox("Year", ("Select Year for lowest PhonePe User", 2018, 2019, 2020, 2021, 2022))
        if Year != "Select Year for lowest PhonePe User":
            query3 = (f"select district_name, sum(registerd_users) as users from map_user where years={Year} group by district_name order by users asc")
            mycursor.execute(query3)
            table = mycursor.fetchall()
            table2 = pd.DataFrame(table, columns=["District", "Registered Users"])
            tab = table2.head(10)
            fig = px.pie(tab, values="Registered Users", names="District", title="Top 10 Lowest PhonePe Users")
            st.plotly_chart(fig)
    elif options == "Top 10 District with Highest Transaction Count":
        Year = st.selectbox("Year", ("Select Year for highest Count", 2018, 2019, 2020, 2021, 2022))
        if Year != "Select Year for highest Count":
            mycursor.execute("select * from map_transaction")
            table = mycursor.fetchall()
            table2 = pd.DataFrame(table, columns=["State", "Year", "Quarter", "District Name", "Transaction Amount", "Transaction Count"])
            tab = table2[["State", "Year", "District Name", "Transaction Count"]]
            t1 = tab.loc[tab["Year"] == Year]
            a = t1.groupby(["State", "District Name"])["Transaction Count"].sum().sort_values(ascending=False)
            map2 = pd.DataFrame(a).reset_index()
            m = map2.head(10)
            fig = px.sunburst(m, path=['State', 'District Name'], values='Transaction Count')
            st.plotly_chart(fig)
    elif options == "Top 10 District With Lowest Transaction Count":
        Year = st.selectbox("Year", ("Select Year for lowest Count", 2018, 2019, 2020, 2021, 2022))
        if Year != "Select Year for lowest Count":
            mycursor.execute("select * from map_transaction")
            table = mycursor.fetchall()
            table2 = pd.DataFrame(table, columns=["State", "Year", "Quarter", "District Name", "Transaction Amount", "Transaction Count"])
            tab = table2[["State", "Year", "District Name", "Transaction Count"]]
            t1 = tab.loc[tab["Year"] == Year]
            a = t1.groupby(["State", "District Name"])["Transaction Count"].sum().sort_values(ascending=True)
            map2 = pd.DataFrame(a).reset_index()
            m = map2.head(10)
            fig = px.sunburst(m, path=['State', 'District Name'], values='Transaction Count', color_continuous_scale='RdBu')
            st.plotly_chart(fig)
