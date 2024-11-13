from playwright.async_api import async_playwright, TimeoutError

async def send_instagram_message(username, password, recipient, message):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto('https://calendar.google.com/calendar/u/0/r', timeout=10000)
        await page.wait_for_load_state('networkidle')
