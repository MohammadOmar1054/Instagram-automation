from playwright.async_api import async_playwright, TimeoutError

async def send_instagram_message(username, password, recipient, message):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            await page.goto('https://www.instagram.com/accounts/login/', timeout=10000)
            await page.wait_for_load_state('networkidle')

            await page.fill('input[name="username"]', username)
            await page.fill('input[name="password"]', password)
            await page.click('button[type="submit"]')
            await page.wait_for_load_state('networkidle')

            await page.click('//a[contains(@aria-label, "Direct")]')
            await page.wait_for_load_state('networkidle')

            # await page.wait_for_selector('//*[@id="mount_0_0_SX"]', timeout=60000)  # Ensure the main container is loaded
            # await page.click('//*[@id="mount_0_0_SX"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[5]/div/div/div/div/div[2]/div/div[1]/span/span')
            await page.wait_for_selector('#mount_0_0_mU > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x1v4esvl.x8vgawa > section > main > section > div > div > div > div.xjp7ctv > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xeuugli.xvbhtw8 > div > div.x78zum5.xdt5ytf.x1iyjqo2.x6ikm8r.x10wlt62.x1n2onr6 > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div > div', timeout=60000)
            await page.click(f'//a[contains(@title, "{recipient}")]')
            await page.wait_for_timeout(20000)

            await page.wait_for_load_state('div[aria-label="Messenger"]', timeout=60000)
            message_input = page.locator('div[aria-label="Messenger"]')
            await message_input.fill(message)

            await page.click('div[role="button"]:has-text("Send")')
            print('Message sent')

        except TimeoutError as e:
            print(f"Operation timed out: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

async def main():
    await send_instagram_message('Yourusername', 'Yourpassword', 'recepient', 'Hello, this is a test message!')

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
