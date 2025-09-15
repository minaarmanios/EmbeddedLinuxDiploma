from chrome_link import ChromeLink

chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
browser = ChromeLink(chrome_path)
favourite_list = browser.show_favourite_menu()
link = input("please select a value:")
browser.chrome(favourite_list[link])
