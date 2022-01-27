import csv
from selenium import webdriver

path = "classic_run3.csv"
file = open(path, 'w', newline='')
writer = csv.writer(file)
# writer.writerow(["backendPerformance_calc", "frontendPerformance_calc"])
# PATH = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
hyperlink = "https://stackoverflow.com"
# driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')

iterations = 4

for i in range(iterations):
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
    driver.get(hyperlink)

    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart

    print("Back End: %s" % backendPerformance_calc)
    print("Front End: %s" % frontendPerformance_calc)

    writer.writerow([backendPerformance_calc, frontendPerformance_calc])
    driver.close()
    print("start next iteration")
driver.quit()
file.close()
