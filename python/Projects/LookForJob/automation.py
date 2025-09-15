import os
import time
from chrome_link import ChromeLink
from gui_control import GuiControl


class GuiAutomation:
    
    def __init__(self, chrome_path, url):
        # Launch Chrome
        self.browser = ChromeLink(chrome_path)
        self.browser.chrome(url)
        
        # Initialize GUI control
        self.gui_control = GuiControl()
        
    def get_screenshots(self):
        return self.gui_control.get_screenshots()

    def run(self, steps, default_delay=5):
        """
        Run a list of automation steps.
        Each step is a dictionary with keys:
        - 'resource': path to image (or None)
        - 'action': "write", "press", or "scroll"
        - 'input': text for write, key(s) for press, scroll value for scroll
        """
            
        if not isinstance(steps, list):
            return
        
        
        for step in steps:
            curr_res = True
            print(f"Executing step: {step}")
            
            # Wait after each step
            time.sleep(5)
            
            if step['dependent'] is True and curr_res is False:
                continue
            
            # Locate the element if a resource is provided
            if step.get('resource'):
                curr_res = self.gui_control.click_on_image(step['resource'])
                if not curr_res:
                    print(f"Element not found: {step['resource']}")
                    if step['mandatory'] is True:
                        return
            else:
                curr_res = True

            # Perform the action
            action = step.get('action')
            user_input = step.get('input')

            if action == "write" and user_input:
                self.gui_control.write_text(user_input)

            elif action == "press" and user_input:
                print("Pressing key:", user_input)
                self.gui_control.press_key(user_input)

            elif action == "scroll":
                if user_input == 0:
                    self.gui_control.scroll_to_end()
                elif user_input is not None:
                    self.gui_control.scroll(user_input)
            
            elif action == "snapshot":
                self.gui_control.take_screenshot()
                

            
