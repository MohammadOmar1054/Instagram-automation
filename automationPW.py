import asyncio
from playwright.async_api import async_playwright

async def send_instagram_message(username, password, recipients, message):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Navigate to Instagram login page
        await page.goto('https://www.instagram.com/accounts/login/', timeout=60000)
        await page.wait_for_load_state('networkidle')

        # Wait for the login fields to load
        await page.fill('input[name="username"]', username)
        await page.fill('input[name="password"]', password)
        await page.click('button[type="submit"]')

        # Wait for the home page to load
        await page.wait_for_load_state('networkidle')

        # Navigate to the Instagram homepage
        await page.goto('https://www.instagram.com/')

        # Wait for the message icon to be visible and click it
        try:
            # Wait for the message icon (DM icon) to be visible
            await page.wait_for_selector('a[aria-label="Direct"]', timeout=60000)  # Adjust selector if necessary
            await page.click('a[aria-label="Direct"]')
        except Exception as e:
            print(f"Could not find message icon: {e}")
            await page.screenshot(path="message_icon_error.png")
            return  # Exit if we can't find the message icon

        # Wait for the message page to load
        await page.wait_for_load_state('networkidle')

        for recipient in recipients:
            # Click the new message button
            try:
                await page.wait_for_selector('button[aria-label="New Message"]', timeout=60000)
                await page.click('button[aria-label="New Message"]')
            except Exception as e:
                print(f"Could not find new message button: {e}")
                await page.screenshot(path="new_message_button_error.png")
                continue

            # Type the recipient's username in the search box
            try:
                await page.wait_for_selector('input[placeholder="Search..."]', timeout=60000)
                await page.fill('input[placeholder="Search..."]', recipient)
            except Exception as e:
                print(f"Could not find search input: {e}")
                await page.screenshot(path="search_input_error.png")
                continue

            # Wait for the recipient to appear in the search results and click it
            try:
                await page.wait_for_selector(f'text="{recipient}"', timeout=60000)
                await page.click(f'text="{recipient}"')
            except Exception as e:
                print(f"Could not find recipient {recipient}: {e}")
                await page.screenshot(path=f"{recipient}_not_found.png")
                continue

            # Type the message and send it
            try:
                await page.wait_for_selector('textarea[aria-label="Message..."]', timeout=60000)
                await page.fill('textarea[aria-label="Message..."]', message)
                await page.keyboard.press('Enter')  # Send the message
            except Exception as e:
                print(f"Could not send message to {recipient}: {e}")
                await page.screenshot(path=f"{recipient}_send_error.png")
                continue

            # Optionally, wait for a brief moment before sending the next message
            await page.wait_for_timeout(2000)  # Wait 2 seconds

        # Close the browser
        await browser.close()

# Replace with your Instagram credentials and the recipients
username = 'lunaticallyyyy'
password = 'omar12345'
recipients = ['_.3rzxii']
message = 'Hello! This is a test message.'

# Run the function
asyncio.run(send_instagram_message(username, password, recipients, message))