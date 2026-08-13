import os
import asyncio
from playwright.async_api import async_playwright

async def take_screenshots():
    # Ensure screenshots directory exists
    screenshots_dir = os.path.join(os.path.dirname(__file__), 'screenshots')
    os.makedirs(screenshots_dir, exist_ok=True)
    
    # URL of the local file
    file_url = f"file:///{os.path.abspath('index.html').replace(os.sep, '/')}"
    print(f"Loading {file_url}")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # 1. Desktop Screenshots (1440x900)
        context_desktop = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context_desktop.new_page()
        await page.goto(file_url, wait_until='networkidle')
        
        # Wait a bit for animations
        await page.wait_for_timeout(1000)
        
        # 01-home-hero.png
        hero_section = await page.query_selector('#home')
        if hero_section:
            await hero_section.screenshot(path=os.path.join(screenshots_dir, '01-home-hero.png'))
            print("Captured 01-home-hero.png")
            
        # 02-about.png
        about_section = await page.query_selector('#about')
        if about_section:
            await about_section.screenshot(path=os.path.join(screenshots_dir, '02-about.png'))
            print("Captured 02-about.png")
            
        # 03-skills.png
        skills_section = await page.query_selector('#skills')
        if skills_section:
            await skills_section.screenshot(path=os.path.join(screenshots_dir, '03-skills.png'))
            print("Captured 03-skills.png")
            
        # 04-projects.png
        projects_section = await page.query_selector('#projects')
        if projects_section:
            await projects_section.screenshot(path=os.path.join(screenshots_dir, '04-projects.png'))
            print("Captured 04-projects.png")
            
        # 05-education-learning.png
        education_section = await page.query_selector('#education')
        if education_section:
            await education_section.screenshot(path=os.path.join(screenshots_dir, '05-education-learning.png'))
            print("Captured 05-education-learning.png")
            
        # 06-contact.png
        contact_section = await page.query_selector('#contact')
        if contact_section:
            await contact_section.screenshot(path=os.path.join(screenshots_dir, '06-contact.png'))
            print("Captured 06-contact.png")
            
        # 07-footer.png
        footer_section = await page.query_selector('.footer')
        if footer_section:
            await footer_section.screenshot(path=os.path.join(screenshots_dir, '07-footer.png'))
            print("Captured 07-footer.png")
            
        # 09-full-page.png
        await page.screenshot(path=os.path.join(screenshots_dir, '09-full-page.png'), full_page=True)
        print("Captured 09-full-page.png")
        
        await context_desktop.close()
        
        # 2. Mobile Screenshot (390x844 - iPhone 12/13)
        context_mobile = await browser.new_context(viewport={'width': 390, 'height': 844})
        mobile_page = await context_mobile.new_page()
        await mobile_page.goto(file_url, wait_until='networkidle')
        
        # Wait a bit
        await mobile_page.wait_for_timeout(1000)
        
        # 08-mobile-responsive.png (full page mobile)
        await mobile_page.screenshot(path=os.path.join(screenshots_dir, '08-mobile-responsive.png'), full_page=True)
        print("Captured 08-mobile-responsive.png")
        
        await context_mobile.close()
        await browser.close()
        print("All screenshots captured successfully!")

if __name__ == "__main__":
    asyncio.run(take_screenshots())
