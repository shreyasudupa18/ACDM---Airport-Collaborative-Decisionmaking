#importing the libraries
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit as st
from PIL import Image
#current time
from datetime import datetime
import time
#importing the dataset in csv format
sampledata=pd.read_csv("SAMPLEDATA2.csv")

from datetime import datetime

now = datetime.now()
df = pd.read_csv("SAMPLEDATA2.csv") #displaying the entire dataset
st.title("FLIGHT DATA")  # add a title
st.write(df)
current_time = now.strftime("%H:%M:%S") #displaying the current time in hh:mm:ss
st.write("Current Time: ", current_time)


Flight_name = st.text_input("Enter Your FLIGHT number here.") #creating the textbox to input the flight number
sampledata=pd.read_csv("SAMPLEDATA2.csv")

def start_fun(F_name):
    sampledata["TOBT"] = sampledata["TOBT"].astype('datetime64[ns]')


    sampledata.dropna(inplace=True)
    time_delta = timedelta(hours=0, minutes=5, seconds=0, microseconds=0)
    df = pd.DataFrame(sampledata, columns=["FLIGHT","TOBT", "TSAT",])
    data = pd.DataFrame(df, columns=["FLIGHT","TOBT", "TSAT", "five+","five-" ])


    for item in df["TOBT"]:
        df["fivep"] = df["TOBT"] + time_delta
        df["fivem"] = df["TOBT"] - time_delta

    # print(df)

    comparison_column = np.where(((data.TSAT <= df.fivep ) & (data.TSAT >= df.fivem )) ,"GREEN",
    "-")
    comparison_column1= np.where((data.TSAT < df.fivem),"BLUE","-")
    comparison_column2= np.where((data.TSAT > df.fivep),"RED","-")


def boarding_status(F_name): #displaying the data for the entered flight number
    df = pd.DataFrame(sampledata, columns=["FLIGHT","STATUS (EST DEP)","BAY","REVISED TOBT","TSAT","DEBOARDING", "DOORS CLOSED","REFUELING","DOORS CLOSED"])
    df['FLIGHT'] = df['FLIGHT'].astype('str')
    name = str(F_name)
    df1 = df[df["FLIGHT"].str.contains(name)]
    return df1



#def refresher(seconds):



#    while True:
#
#        updated_time = now + timedelta(seconds=5)
#        print( updated_time )

      # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

      # visualize my dataframe in the Streamlit app
#        time.sleep(seconds)
#    rerun()
#refresher(5)
def getTimeValues(first_var, second_var): #logic to display the flight for the next 30 minutes based on tobt
    if second_var + 30 >60:
        second_bar = second_var +30
        rem = second_bar % 60
        first_fin = first_var +1
        second_fin = rem
    else:
        first_fin = first_var
        second_fin = second_var + 30
    return first_fin,second_fin



def getList(F_name, row_numm): #information which are displayed for the flights (next 30 mins)
    df2=pd.read_csv("SAMPLEDATA2.csv")

    # , index_col = "Sl_no"
    df2['FLIGHT'] = df2['FLIGHT'].astype('str')
    name = str(F_name)
    long_df = df2[df2["FLIGHT"].str.contains(name)]
    number_list = long_df['Sl_no'].tolist()
    number = number_list[0]
    # st.write(number_list)
    dff = pd.DataFrame(data=None, columns=["Sl_no","FLIGHT","BAY","TOBT","REVISED TOBT","TSAT","DEBOARDING","REFUELING","CLEANING","DOORS CLOSED"])
    tobt_val = long_df["TOBT"].values[0]
    st.write("TOBT OF THE PRESENT FLIGHT IS: ")
    st.write(tobt_val)
    split_list = tobt_val.split(":")
    first_var = int(split_list[0])
    second_var = int(split_list[1])

    res1, res2 = getTimeValues(first_var, second_var)

    fff = []

    for i in range(number, number+row_numm+1):
        # df3 = df2[df2["Sl_no"] == i]
        # df3 = df2.loc[i]
        # st.write(df2.loc[i])
        dfg = df2.loc[i]
        tobt_val1 = dfg["TOBT"]
        tobt_val1 = str(tobt_val1)
        split_list1 = tobt_val1.split(":")
        first_var1 = int(split_list1[0])
        second_var1 = int(split_list1[1])


        if first_var1 <= res1:
            if second_var1 <= res2:
                fff.append(df2.loc[i])

        else:
            continue


        # fff.append(df2.loc[i])

    new_df = dff.append(fff, ignore_index=True)


    return new_df


if(st.button('Submit',key="r")):


    F_name = Flight_name.title()
    if F_name =='':
        st.write("enter the flight name ")
    elif F_name =='':
        st.write("enter the flight name and try again!!")

    else:
        output = start_fun(F_name)
    if output == "FLIGHT DELAYED":
        st.error(output)

    elif output == "FLIGHT ON TIME":
        st.success(output)
    elif output == "FLIGHT EARLY":
        st.info(output)
    else:
        st.write("")

        bs = boarding_status(F_name)
        st.write(bs)

        # row_numm = row_num.title()
        # row_numm = int(row_numm)
        row_numm = 8

        li = getList(F_name, row_numm)

        st.write("THE FLIGHTS WITHIN THE NEXT 30 MINUTES ARE: ")
        st.write(li)
#import keyboard

#timer = 0

#auto updating the user interface every 2 mins
#while timer < 1000:
#    time.sleep(120)
#    timer += 1
#   keyboard.press('r')

# it rrrblocks until rctrl is pressedrr

#import time
#from datetime import datetime
#while True:r
#    now = datetime.now()
#    st.write(now.strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True),
#    st.write("\r", end="", flush=True),
#    time.sleep(1)
#while True:r
#    with st.spinner():

#import rpdb2; rpdb2.start_embedded_debugger('# REVIEW: ')
#        time.sleep(5)r
#st.success("done")
#errorrrrrrrrrrr
