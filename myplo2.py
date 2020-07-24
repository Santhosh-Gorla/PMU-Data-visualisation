import matplotlib.pyplot as pit
import pandas as pd
#import datetime as datetime
from datetime import datetime

workbook1 = '10002.xls'

df = pd.read_excel(workbook1)
df

pit.plot(df['Time'],df[''])

pit.xlabel('Time')
pit.ylabel('Frequency')
pit.title('Time v/s Frequency')
pit.legend()

pit.show()

# worked out some other methods
#workbook1 = 'Book1.xlsx'

#df = pd.read_excel(workbook1)

   #dates = matplotlib.dates.date2num(df['Time'])
   #pit.pyplot.plot_date(df['Time'], df['Frequency'])



#df

#times = datetime.time(dt)

# Read Excel and select a single cell (and make it a header for a column)

#data = pd.read_excel(workbook1, 'Sheet1', index_col=None, usecols = "C", header = 2, nrows=6000)
#now = data.values[1]
#date_time = now.strftime(" %H:%M:%S")
#print("date and time:",date_time)

#times = datetime.time(data)
#times

             # Extract a value from a list (list of headers)
             #ata = data.columns.values[0]
             #print (data)
#dt_str1 = str(data.values[0])
#dt_str = dt_str1.str.slice(9,26)
#print(dt_str)
#dt_obj = datetime.strptime(str(data.values[0]), "%H, %M, %S" )
#print(dt_obj)
#type(df['Frequency'])

#times = data.values[0]
#print(type(times))

#df.Time.slice(-5,-3)
#df.dtypes
#df['Time'] = pd.to_datetime(df.Frequency)
#df.dtypes

#pd.to_datetime('00:24:00.100000')

#now = datetime.now()

#timestamp = datetime.timestamp(now)
#print("timestamp =", timestamp)
#print("timestamp type =", type(now))

