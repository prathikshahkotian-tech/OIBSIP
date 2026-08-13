import os
import asyncio
from playwright.async_api import async_playwright

async def take_screenshots():
    screenshots_dir = os.path.join(os.path.dirname(__file__), 'screenshots')
    os.makedirs(screenshots_dir, exist_ok=True)
    
    file_url = f"file:///{os.path.abspath('index.html').replace(os.sep, '/')}"
    print(f"Loading {file_url}")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context.new_page()
        await page.goto(file_url, wait_until='networkidle')
        
        await page.wait_for_timeout(1000)
        
        # 01-home.png
        hero_section = await page.query_selector('#home')
        await hero_section.screenshot(path=os.path.join(screenshots_dir, '01-home.png'))
        print("Captured 01-home.png")
        
        # 02-converter-empty-state.png
        converter_section = await page.query_selector('#converter-section')
        await converter_section.screenshot(path=os.path.join(screenshots_dir, '02-converter-empty-state.png'))
        print("Captured 02-converter-empty-state.png")
        
        # 03-valid-celsius-conversion.png
        await page.fill('#temp-input', '25')
        await page.select_option('#unit-select', 'celsius')
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(500)
        await converter_section.screenshot(path=os.path.join(screenshots_dir, '03-valid-celsius-conversion.png'))
        print("Captured 03-valid-celsius-conversion.png")
        
        # 04-valid-fahrenheit-conversion.png
        await page.fill('#temp-input', '98.6')
        await page.select_option('#unit-select', 'fahrenheit')
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(500)
        await converter_section.screenshot(path=os.path.join(screenshots_dir, '04-valid-fahrenheit-conversion.png'))
        print("Captured 04-valid-fahrenheit-conversion.png")
        
        # 05-valid-kelvin-conversion.png
        await page.fill('#temp-input', '300')
        await page.select_option('#unit-select', 'kelvin')
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(500)
        await converter_section.screenshot(path=os.path.join(screenshots_dir, '05-valid-kelvin-conversion.png'))
        print("Captured 05-valid-kelvin-conversion.png")
        
        # 06-invalid-input.png
        # HTML5 form validation might prevent submission if step="any" type="number" has bad input, 
        # but let's test empty submission
        await page.fill('#temp-input', '')
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(500)
        await converter_section.screenshot(path=os.path.join(screenshots_dir, '06-invalid-input.png'))
        print("Captured 06-invalid-input.png")
        
        # 07-absolute-zero-error.png
        await page.fill('#temp-input', '-300')
        await page.select_option('#unit-select', 'celsius')
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(500)
        await converter_section.screenshot(path=os.path.join(screenshots_dir, '07-absolute-zero-error.png'))
        print("Captured 07-absolute-zero-error.png")
        
        # 08-quick-reference.png
        quick_ref = await page.query_selector('#quick-reference')
        await quick_ref.screenshot(path=os.path.join(screenshots_dir, '08-quick-reference.png'))
        print("Captured 08-quick-reference.png")
        
        # 09-how-it-works.png
        how_it_works = await page.query_selector('#how-it-works')
        await how_it_works.screenshot(path=os.path.join(screenshots_dir, '09-how-it-works.png'))
        print("Captured 09-how-it-works.png")
        
        # 10-features.png
        features = await page.query_selector('#about')
        await features.screenshot(path=os.path.join(screenshots_dir, '10-features.png'))
        print("Captured 10-features.png")
        
        # 11-footer.png
        footer = await page.query_selector('.footer')
        await footer.screenshot(path=os.path.join(screenshots_dir, '11-footer.png'))
        print("Captured 11-footer.png")
        
        # 13-full-page.png (Capture this before resizing)
        # Revert to a valid state for full page
        await page.fill('#temp-input', '25')
        await page.select_option('#unit-select', 'celsius')
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(500)
        await page.screenshot(path=os.path.join(screenshots_dir, '13-full-page.png'), full_page=True)
        print("Captured 13-full-page.png")
        
        await context.close()
        
        # 12-mobile-responsive.png (390px)
        context_mobile = await browser.new_context(viewport={'width': 390, 'height': 844})
        mobile_page = await context_mobile.new_page()
        await mobile_page.goto(file_url, wait_until='networkidle')
        await mobile_page.wait_for_timeout(1000)
        await mobile_page.screenshot(path=os.path.join(screenshots_dir, '12-mobile-responsive.png'), full_page=True)
        print("Captured 12-mobile-responsive.png")
        
        await context_mobile.close()
        await browser.close()
        print("All screenshots captured successfully!")

if __name__ == "__main__":
    asyncio.run(take_screenshots())
