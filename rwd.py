#!/usr/bin/python
#import MySQLdb
import math
import time
import sched
from datetime import datetime
from datetime import timedelta
#import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins
#lcd = LCD.Adafruit_CharLCDPlate()
#lcd.set_color(0.0, 1.0, 0.0)
#lcd.clear()

def display_weather ():
	# db = MySQLdb.connect(host="192.168.1.3",user="weewx",passwd="weewx",db="weewx")
	# cur = db.cursor()

	# cur.execute("select inTemp from archive order by dateTime desc limit 1")
	# temp = cur.fetchone()
	# farenheit = float(temp[0])
	# inTemp = ((farenheit - 32)*0.5555555555555556)
	# print 'Inside Temp = %2.1f' % inTemp

	# cur.execute("select outTemp from archive order by dateTime desc limit 1")
	# temp = cur.fetchone()
	# farenheit = float(temp[0])
	# outTemp = ((farenheit - 32)*0.5555555555555556)
	# print 'Outside Temp = %2.1f' % outTemp

	# cur.execute("select sum from stats.rain order by dateTime desc limit 1")
	# temp = cur.fetchone()
	# rain_inches = float(temp[0])
	# rain = (rain_inches/0.039370)
	# print 'Rain = %3.1f' % rain

	# current_time = datetime.now()
	# print '%s:%s' % (current_time.hour,current_time.minute)

	# lcd.message('%2d:%02d' % (current_time.hour,current_time.minute))
	# lcd.message(' Rain %3.1f\n' % rain)
	# lcd.message('In %2.1f' % inTemp)
	# lcd.message(' Out %2.1f\n' % outTemp)

	# cur.close()
	# db.close()
	print "display_weather"

	
def display_seconds():
	d = datetime.now()
	print d
	d = d + timedelta(seconds=1)
	s.enterabs(time.mktime(d.timetuple()), 1, display_seconds, argument=())

def display_time():
	ct = datetime.now()
	print '%02d:%02d:%02d' % (ct.hour, ct.minute, ct.second)
	
def one_second_tick():
	#empty function
	print Hello

def five_minute_tick():
	#empty function
	print "Five Minutes"
	print ct
	
display_time()

s = sched.scheduler(time.time, time.sleep)

ct = datetime.now() + timedelta(seconds=1)
s.enterabs(time.mktime(ct.timetuple()), 1, display_seconds, argument=())

ct = datetime.now() + timedelta(minutes=5, seconds=5)
print ct
print int(5.0 * round(float(ct.minute+5.0/2.0)/5.0))
exit()
s.enterabs(time.mktime(ct.timetuple()), 1, five_minute_tick, argument=())

s.run()

exit()
