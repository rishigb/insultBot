import openpyxl

''' Create an excel sheet, give it headers and save it'''
wb=openpyxl.Workbook()
s=wb.get_sheet_by_name('Sheet')

InpFileName = "tweetsSaved"

colNames= ["Name","Tweet","PersonDescription","Following","Followers","statusCount","retweet_count","verified","LocationOfOriginOfTweet","lang"]
print (len(colNames))

s['A1'] = colNames[0]
s['B1'] = colNames[1]
s['C1'] = colNames[2]
s['D1'] = colNames[3]
s['E1'] = colNames[4]
s['F1'] = colNames[5]
s['G1'] = colNames[6]
s['H1'] = colNames[7]
s['I1'] = colNames[8]
s['J1'] = colNames[9]


print ("Column names assigned")

for i in range(2,10000):
	s['A'+str(i)] = i
	s['B'+str(i)] = i+100
	s['C'+str(i)] = i+200
	s['D'+str(i)] = i+300
	s['E'+str(i)] = i+400
	s['F'+str(i)] = i+500
	s['G'+str(i)] = i+600
	s['H'+str(i)] = i+700
	s['I'+str(i)] = i+800
	s['J'+str(i)] = i+900
	

wb.save('testExcel.xlsx')
print ("Done")


