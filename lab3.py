import pandas as pd
import numpy as np
import urllib2
import os
import datetime
import time
import glob

def readcsv():
	df = pd.DataFrame()
	df = pd.read_csv("household_power_consumption.txt", sep=';')
	now = datetime.datetime.now().strftime("%Y%m%d-%H%M")
	df.to_csv('household_power_consumption.csv', encoding='utf-8', sep=';', index=False)
	
def clear_csv():
	now = datetime.datetime.now().strftime("%Y%m%d-%H%M")
	with open('household_power_consumption.csv','r') as raw, open('HPC_' + now + '.csv','w') as clear:
		for line in raw:
			if '?' not in line:
				clear.write(line)

def analyze():
	f = glob.glob('HPC_*.csv')[0]
	i=1
	while i:
		sindex = int(input("\n1 - Potujnist perevischue 5 kVt,\n2 - Voltaj perevischue 235 V,\n3 - Sila strumu v mejah 19-20 A, sub_metering_2 > sub_metering_3,\n4 - Vipadkovi 500000 i znaitu seredne dlya troh grup\n5 - U kogo > 6 kVt pisla 18-00 i do 24-00 u serednomu, sered nih obratu > sub_metering_2, a potim obratu kojen 3 iz pershoi polovunu i kojen 4 iz drugoii polovunu\n6 Zakinchitu robotu\n"))
		if sindex == 1:
			start_df = time.time()
			df = pd.read_csv(f, ";", low_memory=False)
			df = df[df['Global_active_power']>5]
			start_df = time.time() - start_df
			start_arr = time.time()
			df_arr = pd.read_csv(f, sep=";", low_memory=False)
			array = df_arr.as_matrix()
			array = array[array[:,2]>5]
			start_arr = time.time() - start_arr
			print df.head(),"\n\n",array, "\nChas robotu dataframy: ", start_df, "\nChas robotu spusky: ", start_arr
		elif sindex == 2:
			start_df = time.time()
			df = pd.read_csv(f, ";", low_memory=False)
			df = df[df['Voltage']>235]
			start_df = time.time() - start_df
			start_arr = time.time()
			df_arr = pd.read_csv(f, sep=";", low_memory=False)
			array = df_arr.as_matrix()
			array = array[array[:,4]>235]
			start_arr = time.time() - start_arr
			print df.head(), "\nChas robotu dataframy: ", start_df, "\nChas robotu spusky: ", start_arr
		elif sindex == 3:
			start_df = time.time()
			df = pd.read_csv(f, ";", low_memory=False)
			df = df[(df['Global_intensity']>18) & (df['Global_intensity']<20) & (df['Sub_metering_2']>df['Sub_metering_3'])]
			start_df = time.time() - start_df
			start_arr = time.time()
			df_arr = pd.read_csv(f, sep=";", low_memory=False)
			array = df_arr.as_matrix()
			array = array[(array[:,5] > 19) & (array[:,5] < 20) & (array[:,7] > array[:,8])]
			start_arr = time.time() - start_arr
			print df.head(), "\nChas robotu dataframy: ", start_df, "\nChas robotu spusky: ", start_arr
		elif sindex == 4:
			start_df = time.time()
			df = pd.read_csv(f, ";", low_memory=False)
			df=df.drop_duplicates(keep=False)
			df=df.sample(n=500000)
			df['Average'] = (df['Sub_metering_1'] + df['Sub_metering_2'] + df['Sub_metering_3'])/3
			start_df = time.time() - start_df
			start_arr = time.time()
			df_arr = pd.read_csv(f, sep=";", low_memory=False)
			array = df_arr.as_matrix()
			array = array[np.random.randint(array.shape[0],size=50000), :]
			average = np.array((array[:,6] + array[:,7]  + array[:,8])/3)
			average = average.reshape((50000,1))
			array = np.concatenate((array, average), axis=1)
			start_arr = time.time() - start_arr
			print df.head(), "\nChas robotu dataframy: ", start_df, "\nChas robotu spusky: ", start_arr
		elif sindex == 5:
			start_df = time.time()
			df = pd.read_csv(f, ";", low_memory=False)
			df = df[(df['Time'] > '18:00:00') & (df['Global_active_power'] > 5) &(df['Sub_metering_2'] > df['Sub_metering_1']) & (df['Sub_metering_2'] > df['Sub_metering_3'])]
			start_df = time.time() - start_df
			start_arr = time.time()
			df_arr = pd.read_csv(f, sep=";", low_memory=False)
			array = df_arr.as_matrix()
			array = array[(array[:,1]>'18:00:00')&(array[:,2]>5)&(array[:,7]>array[:,6])&(array[:,7]>array[:,8])]
			array1 = array[::2]
			array2 = array[::4]
			array = np.concatenate((array1, array2), axis=0)
			start_arr = time.time() - start_arr
			print df.head(), "\nChas robotu dataframy: ", start_df, "\nChas robotu spusky: ", start_arr
		elif sindex == 6:
			i=0

#readcsv()
#clear_csv()
analyze()