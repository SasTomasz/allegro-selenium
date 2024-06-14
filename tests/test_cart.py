from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Setup Chrome driver
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

# Navigate to the main page
driver.get('https://allegro.pl.allegrosandbox.pl/')

# Find an item and click on it
item = driver.find_element(By.CSS_SELECTOR, 'selector-for-item')  # Replace 'selector-for-item' with the actual CSS selector for an item
item.click()

# Click the "DODAJ DO KOSZYKA" button
add_to_cart_button = driver.find_element(By.CSS_SELECTOR, 'selector-for-add-to-cart-button')  # Replace 'selector-for-add-to-cart-button' with the actual CSS selector for the "DODAJ DO KOSZYKA" button
add_to_cart_button.click()

# Check if there's an icon indicating that one item is in the cart
cart_icon = driver.find_element(By.CSS_SELECTOR, 'selector-for-cart-icon')  # Replace 'selector-for-cart-icon' with the actual CSS selector for the cart icon
assert cart_icon is not None

# Navigate to the cart page and check if the added item is there
driver.get('https://allegro.pl.allegrosandbox.pl/cart')  # Replace with the actual URL of the cart page
added_item = driver.find_element(By.CSS_SELECTOR, 'selector-for-added-item')  # Replace 'selector-for-added-item' with the actual CSS selector for the added item in the cart
assert added_item is not None

# Close the browser
driver.quit()
