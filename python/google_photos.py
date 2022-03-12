import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime
import time

#get files and names
path = os.path.abspath("/Volumes/USB-SAM/10 December 2019 SD-kaart (16GB) kopie/WhatsApp/Media/WhatsApp Images tot 19 augustus/Sent")
picture_names = os.listdir(path)
if ('.DS_Store' in picture_names):
    picture_names.remove('.DS_Store')
if ('Sent' in picture_names):
    picture_names.remove('Sent')
if ('.nomedia' in picture_names):
    picture_names.remove('.nomedia')


#choose a picture
for i in range(len(picture_names)):
    print(picture_names[i])
    total_path = path + "/" + picture_names[i]
    wrong_timestamp = os.path.getmtime(total_path)
    wrong_date = datetime.fromtimestamp(wrong_timestamp)

    right = picture_names[i].split('-')[1]
    year, month, day = int(right[:4]), int(right[4:6]), int(right[6:])
    # get the order of pictures of one day
    counter = [int(picture_names[i].split('-')[2][2:6]),0]
    if counter[0] > 23: #if there are more than 24 pictures in a day set the minutes
        counter[1] = counter[0]%24 + 1
        counter[0] = int((counter[0]-counter[1])/24)

    #make the datetime objects
    right_date = datetime(year,month,day,counter[0],counter[1],0)
    right_timestamp = time.mktime(right_date.timetuple())
    access_time = os.stat(total_path).st_atime

    os.utime(total_path,(access_time,right_timestamp))




# # fill in manually for one picture
# total_path = "/Volumes/USB-SAM/26 December 2020 SD-kaart (16GB) kopie/Afbeeldingen/Animated GIF/SmartSelect_20200811-000513_Snapchat.gif"
# right_date = datetime(2020,8,11,0,0,0)
# right_timestamp = time.mktime(right_date.timetuple())
# access_time = os.stat(total_path).st_atime
# # os.utime(total_path,(access_time,right_timestamp))




# #example Screenshot_20201227_082359 for 2020-12-27 08:23:59
# for i in range(len(picture_names)):
#     print(picture_names[i])
#     picture_names[i] = picture_names[i][11:]
#     total_path = path + "/" + "Screenshot_" + picture_names[i]
#     wrong_timestamp = os.path.getmtime(total_path)
#     wrong_date = datetime.fromtimestamp(wrong_timestamp)

#     # right = picture_names[i].split('_')[0]
#     year, month, day, hour, minute, second = int(picture_names[i][0:4]), int(picture_names[i][4:6]), int(picture_names[i][6:8]), int(picture_names[i][9:11]), int(picture_names[i][11:13]), int(picture_names[i][13:15])
#     print(picture_names[i],year,month,day,hour,minute,second)

#     # # make the datetime objects
#     right_date = datetime(year,month,day,hour,minute,second)
#     right_timestamp = time.mktime(right_date.timetuple())
#     access_time = os.stat(total_path).st_atime

#     # os.utime(total_path,(access_time,right_timestamp))