import pyautogui
import time
import logging


class GuiControl:
    def __init__(self):
        self.screenshots = []
    
    def get_screenshots(self):
        return self.screenshots
        
    # -----------------------------
    # Element location
    # -----------------------------
    def locate(self, element_image_path, timeout=10, confidence=0.7, min_search_time=1):
        """
        Locate an image on screen and return its center coordinates.
        Returns None if not found within timeout.
        """
        start_time = time.time()
        point_xy = None

        while (time.time() - start_time) < timeout:
            try:
                point_xy = pyautogui.locateOnScreen(
                    element_image_path,
                    confidence=confidence,
                    minSearchTime=min_search_time
                )
                if point_xy:
                    center = pyautogui.center(point_xy)
                    return center
            except pyautogui.ImageNotFoundException:
                pass  # keep trying
            
            time.sleep(0.5)

        return None

    # -----------------------------
    # Mouse actions
    # -----------------------------
    def move_to(self, coords, duration=0.5, wait_after=0.1):
        if coords:
            pyautogui.moveTo(coords.x, coords.y, duration=duration)
            time.sleep(wait_after)
            return True
        return False

    def click(self, coords=None, duration=0.5, wait_after=0.1):
        """
        Click at the given coordinates or current mouse position.
        """
        if coords:
            self.move_to(coords, duration, wait_after)
        pyautogui.click()

    def click_on_image(self, element_image_path, timeout=10):
        coords = self.locate(element_image_path, timeout)
        if coords:
            self.click(coords)
            return True
        return False

    # -----------------------------
    # Keyboard actions
    # -----------------------------
    def write_text(self, text):
        if text:
            pyautogui.typewrite(text, interval=0.05)

    def press_key(self,key):
        pyautogui.click()
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        pyautogui.press(key)
        pyautogui.hotkey(key)

    # -----------------------------
    # Scrolling actions
    # -----------------------------
    def scroll(self, scroll_value):
        pyautogui.scroll(scroll_value)

    def scroll_to_end(self):
        pyautogui.hotkey("ctrl", "end")
        

    def scroll_to_top(self):
        pyautogui.hotkey("ctrl", "home")
        
    def take_screenshot(self):
        self.screenshots.append(pyautogui.screenshot())
