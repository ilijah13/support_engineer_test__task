from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def test_shopping(driver):
   wait = WebDriverWait(driver, 10)
   product = 'samsung galaxy s22'
   
   amazon_link = 'https://www.amazon.com/'
   driver.get(amazon_link)
   amazon_search_input = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
   amazon_search_input.send_keys(product)
   driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()
   driver.find_element(By.XPATH, '//*[@id="p_72/2491149011"]/span/a').click()
   driver.find_element(By.CSS_SELECTOR, 'a[href*="B09MVYVBR6"]').click()
   amazon_price = (float(driver.find_element(By.CSS_SELECTOR, 'span[class*="a-price-whole"]').text.replace(',', '')) 
                   + float(driver.find_element(By.CSS_SELECTOR, 'span[class*="a-price-fraction"]').text)/100)
   
   bestbuy_link = 'https://www.bestbuy.com/'
   driver.get(bestbuy_link)
   
   try:
	    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/a[2]').click()		            	
   except NoSuchElementException:
       print('The element could not be found on the page')   
       	
   bestbuy_search_input = driver.find_element(By.XPATH, '//*[@id="gh-search-input"]')   
   bestbuy_search_input.send_keys(product)
   bestbuy_search_input.send_keys(Keys.ENTER)
   bestbuy_sort = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sort-by-select"]')))
   bestbuy_sort.click()
   driver.find_element(By.XPATH, '//*[@id="sort-by-select"]/option[6]').click() 
   driver.find_element(By.CSS_SELECTOR, "a[href*='skuId=6494419']").click()
   driver.find_element(By.CSS_SELECTOR, "img[alt='Green']").click()
   bestbuy_price_element = driver.find_element(By.CSS_SELECTOR,'[data-sticky-media-gallery] .priceView-hero-price span')
   bestbuy_price = float(bestbuy_price_element.text.replace('$', '').replace(',', ''))
				
   assert amazon_price > bestbuy_price

	