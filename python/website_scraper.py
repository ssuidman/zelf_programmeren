from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
driver = webdriver.Chrome(options=chrome_options)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.4daagse.nl/meedoen/ticket-overdragen"
driver.get(url)


iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
driver.switch_to.frame(iframe)

document_element = driver.find_element(By.XPATH, "/html/body")
# document_element = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[2]/div[2]/div/div/div[1]")  

# document_element = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div")
# /html/body/div/div/div[1]/div/div/div[2]/div[2]/div/div/div[1]/h5/span[1]
# element = driver.find_elements_by_xpath("/html/body")
element_class = document_element.text
print("Class of the element:", element_class)




# html_element = driver.find_element(By.XPATH, "/html/body/iframe/#document")

# xpath = "/html/body/div/div/div[1]/div/div/div[2]/div[2]/div/div/div[1]/h5/span[1]"
# span_element = driver.find_element(By.XPATH, xpath)

# # Get the text content of the span element
# text_content = span_element.text

# Output the text content
# print("Text Content:", text_content)