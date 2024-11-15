from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

def send_message_to_accounts(accounts, message):
    service = Service(executable_path="C:\\Users\omaro\Downloads\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    # Open Instagram
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    # Log in to Instagram
    username_input = driver.find_element(By.NAME, "your_usernme")
    password_input = driver.find_element(By.NAME, "your_pw")

    username_input.send_keys('your_usernme')  # Replace with your username
    password_input.send_keys('your_pw')    # Replace with your password

    time.sleep(5)  # Wait for the login process to complete

    # Send messages to each account
    for account in accounts:
        try:
            # Go to the direct messages page
            driver.get(f"https://www.instagram.com/{account}/")
            time.sleep(3)

            # Click on the message button (the paper plane icon)
            message_button = driver.find_element(By.XPATH, "//a[contains(@href, '/direct/inbox/')]")
            message_button.click()
            time.sleep(3)

            # Click on the new message button
            new_message_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Send Message')]")
            new_message_button.click()
            time.sleep(3)

            # Enter the username of the recipient
            recipient_input = driver.find_element(By.NAME, "queryBox")
            recipient_input.send_keys(account)
            time.sleep(3)
            recipient_input.send_keys(Keys.RETURN)
            time.sleep(2)

            # Enter the message
            message_input = driver.find_element(By.TAG_NAME, "textarea")
            message_input.send_keys(message)
            message_input.send_keys(Keys.RETURN)  # Send the message
            print(f"Message sent to {account}: {message}")
            time.sleep(10)  # Adjust the sleep time as needed

        except Exception as e:
            print(f"Error sending message to {account}: {e}")

    # Close the browser
    driver.quit()

def main():
    x = input("Enter the number of minutes you are busy: ")
    
    # Message to send
    message = f"I am busy for {x} minutes, call me after {x} minutes."
    
    # List of accounts to send the message to
    accounts = ['receipient']  # Replace with actual usernames
    
    send_message_to_accounts(accounts, message)

if __name__ == "__main__":
    main()
