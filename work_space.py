from playwright.sync_api import Playwright, sync_playwright, expect
from playwright_recaptcha import recaptchav2
from time import sleep
import random
from string import ascii_lowercase 
from playwright_stealth import stealth_sync , StealthConfig
names=open('nam.txt','r').readlines()
def run(playwright: Playwright) -> None:
    password=''.join(random.choice(ascii_lowercase) for iqq in range(13))
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://workspace.google.com/essentials/signup/verify/emailstart")
    stealth_sync(page=page,config=StealthConfig(webdriver=False,nav_platform=False,nav_user_agent=False,navigator_hardware_concurrency=False,chrome_runtime=False))

    page1 = context.new_page()
    page1.goto("https://tempmail.plus/ar/#!")
    stealth_sync(page=page1)
    email=page1.locator('xpath=/html/body/div[8]/div[1]/div[2]/div[1]/form/div/input').input_value()
    email2=page1.locator('xpath=/html/body/div[8]/div[1]/div[2]/div[1]/form/div/div[2]/button').text_content()
    email3=f"{email}{email2}"
    page.bring_to_front()
    page.get_by_label("Work email address").click()
    page.get_by_label("Work email address").fill(f"{email3}")
    page.get_by_role("button", name="Next").click()
    page1.get_by_text("The Google Workspace Team <workspace-noreply@google.com>").click()
    with page1.expect_popup() as page2_info:
        page1.get_by_role("link", name="Verify email address").click()
    page2 = page2_info.value
    stealth_sync(page=page2)
    page2.get_by_label("First name").fill(f"{random.choice(names)}")
    page2.get_by_label("Last name").click()
    page2.get_by_label("Last name").fill(f"{random.choice(names)}")
    sleep(3)
    page2.get_by_label("Create your password").click()
    page2.get_by_label("Create your password").fill(f"{password}")
    with recaptchav2.SyncSolver(page2) as solver:
        try:
            sleep(1)
            token = solver.solve_recaptcha(wait=True,attempts=15)
        except:
            pass
    sleep(5)

    print((f"{email3}:{password}"))
   # sleep(2223)
    page2.get_by_role("button", name="Continue").click()
    #sleep(33333)
    page2.get_by_label("Agree to terms of services and continue").click()
    sleep(5)
    page2.get_by_role("button", name="Create account").click()
    sleep(4)
    #sleep(222222222)
    #page2.goto("https://workspace.google.com/essentials/signup/verified/appsprogress?userToken=AbDmZehMbwXwDgYz7UZBlIrrnp1tUGjZX1gwv1ke0ZKYbUB4tkQafaBK0COoRAFH2Luv4FqxbsUuZOs4uLc3A1fqzTYcsU84If4-GGWTB18FFzHapCn9VRnZF2uaptbV79y5jqz9vqTIlsLT1ZQXzuC219WBt3522de34bM&hl=en_US")
    #page2.goto("https://workspace.google.com/essentials/signup/verified/outro?userToken=AbDmZehMbwXwDgYz7UZBlIrrnp1tUGjZX1gwv1ke0ZKYbUB4tkQafaBK0COoRAFH2Luv4FqxbsUuZOs4uLc3A1fqzTYcsU84If4-GGWTB18FFzHapCn9VRnZF2uaptbV79y5jqz9vqTIlsLT1ZQXzuC219WBt3522de34bM&hl=en_US")
    page2.get_by_role("button", name="Let's go").click()
    em=open('gmail.txt','w+')
    em.write(f"{email3}:{password}")
    em.close()
    sleep(10)


    # ---------------------
    context.close()
    browser.close()

while 1:
    try:
        with sync_playwright() as playwright:
            run(playwright)
    except:
        pass
