import sys
import os
import time
import datetime
from automation import GuiAutomation
from mail_sender import MailSender

def main(): 
    """
    Main entry point for the LinkedIn job search automation script.

    This function expects three command-line arguments:
        1. linkedin_url (str): A LinkedIn URL (e.g., job search or profile page).
        2. job_name (str): The job title or role to search/filter for.
        3. region (str): The geographic region/location for the search.

    It launches Chrome using the specified path, navigates to the LinkedIn URL,
    and then uses ElementLocator to locate relevant elements on the page.

    Usage:
        python script.py <linkedin_url> <job_name> <region>

    Example:
        python script.py "https://www.linkedin.com/jobs" "Software Engineer" "UK"
    """
    #if len(sys.argv) == 3:
    url = sys.argv[0]
    linkedin_url = 'https://www.linkedin.com/feed/'
    job_title = "embedded software engineer"
    country = "United Kingdom"
        
    chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    gui_automation = GuiAutomation(chrome_path,linkedin_url)
    
    next_job_steps = [
        {'resource':os.path.abspath(r'./resources/next_job.JPG'),'action':'click','input':None,'dependent':False},
        {'resource':os.path.abspath(r'./resources/contact_info.JPG'),'action':'click','input':None,'dependent':False},
        {'resource':None,'action':'scroll','input':-150,'dependent':False},
        {'resource':os.path.abspath(r'./resources/auto_apply.JPG'),'action':'click','input':None,'dependent':False},
        {'resource':None,'action':'scroll','input':0,'dependent':True},
        {'resource':os.path.abspath(r'./resources/submit_application.JPG'),'action':'click','input':None,'dependent':True}
    ]
    
    next_snapshot = [
        {'mandatory':True,'resource':None,'action':'snapshot','input':None,'dependent':False},
        {'mandatory':True,'resource':None,'action':'scroll','input':-800,'dependent':False},

    ]
    
    steps = [
        {'mandatory':True,'resource':None,'action':'snapshot','input':None,'dependent':False},
        {'mandatory':True,'resource':os.path.abspath(r'./resources/jobs.JPG'),'action':'click','input':None,'dependent':False},
        {'mandatory':True,'resource':os.path.abspath(r'./resources/title.JPG'),'action':'write','input':job_title,'dependent':False},
        {'mandatory':True,'resource':os.path.abspath(r'./resources/country.JPG'),'action':'write','input':country,'dependent':False},
        {'mandatory':True,'resource':None,'action':'press','input':'enter','dependent':False},
        {'mandatory':True,'resource':os.path.abspath(r'./resources/scroll_bar.JPG'),'action':'click','input':None,'dependent':False},
        *(next_snapshot * 3)
    ]
    
    gui_automation.run(steps)
    time.sleep(10)
    
    screenshots = gui_automation.get_screenshots()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Ensure the screenshots folder exists
    os.makedirs('./screenshots', exist_ok=True)

    screenshot_paths = []
    for idx, screenshot in enumerate(screenshots):
        # Save
        screenshot_path = os.path.abspath(f'./screenshots/screenshot_{timestamp}_{idx}.png')
        screenshot.save(screenshot_path)
        screenshot_paths.append(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
        
    mail_sender = MailSender()
    mail_sender.send_email_with_image(screenshot_paths)
    
        
        
if __name__ == "__main__":
    main()