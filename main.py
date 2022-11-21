###SETTINGS###
ZOOM_URL = "https://nyp-sg.zoom.us/j/88526538027?pwd=V1UvY1Y3elRwRUhtSXZIQ1hrOHZBdz09"
ZOOM_TIME = '09:01:00' #HH:MM:SS format
ZOOM_DAY = 'Monday'

###CODE (DON'T TOUCH IF YOU DONT KNOW WHAT YOU ARE DOING!)###
import schedule,time,webbrowser,sys
def openMeeting():
    webbrowser.open(ZOOM_URL)
    sys.exit('Successfully opened Zoom Meeting!')
try:
    match ZOOM_DAY.lower():
        case 'monday'|'mon':schedule.every().monday.at(ZOOM_TIME).do(openMeeting)
        case 'tuesday'|'tues':schedule.every().tuesday.at(ZOOM_TIME).do(openMeeting)
        case 'wednesday'|'wed':schedule.every().wednesday.at(ZOOM_TIME).do(openMeeting)
        case 'thursday'|'thurs':schedule.every().thursday.at(ZOOM_TIME).do(openMeeting)
        case 'friday'|'friday':schedule.every().friday.at(ZOOM_TIME).do(openMeeting)
        case 'saturday'|'sat':schedule.every().saturday.at(ZOOM_TIME).do(openMeeting)
        case 'sunday'|'sun':schedule.every().sunday.at(ZOOM_TIME).do(openMeeting)
        case _:raise TypeError('Enter a correct day!')
except schedule.ScheduleValueError:exit
while 1:
    schedule.run_pending()
    if time.strftime("%H:%M:%S")==ZOOM_TIME:raise NameError('Error opening Zoom Meeting')
    elif len(ZOOM_TIME)!=8:raise TypeError('Input time in HH:MM:SS format!')
    time.sleep(1)
    print(f'﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏\n︴Current Time: {time.strftime("%H:%M:%S")} ︴\n︴Meeting Time: {ZOOM_TIME} ︴\n﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋')
