import pandas as pd
import os
from pytz import timezone,utc
from datetime import datetime
import datetime as dt

def timestamp_to_pst_converter(timestamp):
    your_dt = dt.datetime.utcfromtimestamp(int(timestamp)/1000)
    convert_date = your_dt.strftime("%Y-%m-%d %H:%M:%S")
    datetime_obj = datetime.strptime(convert_date,"%Y-%m-%d %H:%M:%S")
    pst_tz = timezone('US/Pacific')
    datetime_obj_utc = datetime_obj.replace(tzinfo=utc).astimezone(pst_tz)
    return datetime_obj_utc.strftime("%Y-%m-%d %H:%M:%S %Z")

def jmeter_modify(file_name):
    curr_dir = os.getcwd()
    df = pd.read_csv(curr_dir+"/"+file_name, sep=',')
    pd.set_option('display.width', 200)
    pd.set_option('display.max_columns', None)
    result_col = [i for i in df.columns if i == 'timeStamp' or i == 'label' or i == 'responseCode' or i == 'responseMessage' or i == 'failureMessage']
    result_df = df[df['responseCode'] == 504]
    result_df['timeStamp'] = result_df['timeStamp'].apply(timestamp_to_pst_converter)
    final = result_df[result_col]
    print("\n\n <---------Result dataframe in PST timezone format------------> \n {}".format(final))

jmeter_modify("Jmeter_log1.jtl")
