import pandas as pd
import urllib2
import os
import datetime
import time
import glob

def readcsv():
	df1 = pd.read_csv("household_power_consumption.txt", ";", low_memory=False)
	#file = glob.glob('household_power_consumption.txt')
	#df1 = pd.DataFrame()
	#dfile = pd.read_csv(file,index_col=False, sep=';', names=['Date', 'Time', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'], engine = 'python')
	#df1 = df1.append(dfile)
	now = datetime.datetime.now().strftime("%Y%m%d-%H%M")
	df1.to_csv('datetime_' + now + '_vhi.csv', encoding='utf-8', index=False)
	#search(result)

def analyze():
	sindex = int(input("1 - Potujnist perevishue 5 kVt,\n2 - Voltaj perevishue 235 V,\n3 - Sila strumu v mejah 19-20 A,	sub_metering_2 > sub_metering_3,\n4 - Vipadkovi 500000 i znaitu seredne dlya troh grup\n5 - U kogo > 6 kVt pisla 18-00 i do 24-00 u serednomu, sered nih obratu > sub_metering_2, a potim obratu kojen 3 iz pershoi polovunu i kojen 4 iz drugoii polovunu\n"))
	if sindex == 1:
		df = pd.read_csv("household_power_consumption.txt", ";", low_memory=False)
		print df[df.Global_active_power>5]
	elif sindex == 2:
		df = pd.read_csv("household_power_consumption.txt", ";", low_memory=False)
		print df[df.Voltage>235]
	elif sindex == 3:
		df = pd.read_csv("household_power_consumption.txt", ";", low_memory=False)
		df = df[df.Global_intensity>=19]
		df = df[df.Global_intensity<=20]
		df = df[df.Sub_metering_2>df.Sub_metering_3]
		print df
	
def search(df):
	#province=int(input("Enter province ID for analyze:"))
	#year=str(input("Enter year:"))
	#df=df[(df['year'] == year) & (df['province'] == province)]
	print df[df.VHI<15]
	print "Maximum VHI", df['VHI'].max()
	print "Minimum VHI", df['VHI'].min()

analyze()