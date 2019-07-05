from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from datetime import datetime

browser = webdriver.Chrome(executable_path=r'/home/pruthvi/Downloads/chromedriver_linux64/chromedriver')


bseIDs = [500285, 520139, 532617, 532773, 539448]




#Setting start date to 01/01/1950
def setStartDate():
	startDate = browser.find_element_by_id('ContentPlaceHolder1_txtFromDate')
	startDate.click()

	monthSelector = Select(browser.find_element_by_class_name('ui-datepicker-month'))
	monthSelector.select_by_value('0')

	year = 2010
	while (year>1949):
		yearSelector = Select(browser.find_element_by_class_name('ui-datepicker-year'))
		yearSelector.select_by_value(str(year))
		year -= 10

	calendarTable = browser.find_element_by_class_name('ui-datepicker-calendar')
	calendarRows = calendarTable.find_elements_by_tag_name('td')

	daySelector = calendarRows[0].find_element_by_tag_name('a')
	daySelector.click()


#Setting end date to today
def setEndDate():
	today = datetime.now()
	
	endDate = browser.find_element_by_id('ContentPlaceHolder1_txtToDate')
	endDate.click()
	
	monthSelector = Select(browser.find_element_by_class_name('ui-datepicker-month'))
	monthSelector.select_by_value(str(today.month - 1))

	yearSelector = Select(browser.find_element_by_class_name('ui-datepicker-year'))
	yearSelector.select_by_value(str(today.year))

	calendarTable = browser.find_element_by_class_name('ui-datepicker-calendar')
	calendarRows = calendarTable.find_elements_by_tag_name('a')
	
	daySelector = calendarRows[-1]
	daySelector.click()
	


def downloadStockHistoryCSV(bseIDs):
	for id in bseIDs:
		try:
			browser.get('https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.aspx?expandable=6&scripcode='+str(id)+'&flag=sp&Submit=G')
			setStartDate()
			setEndDate()
			submitForm = browser.find_element_by_id('ContentPlaceHolder1_btnSubmit')
			submitForm.click()
			downloadCSV = browser.find_element_by_id('ContentPlaceHolder1_btnDownload1')
			downloadCSV.click()
		except:
			print(id)


if __name__ == '__main__':
	downloadStockHistoryCSV(bseIDs)

