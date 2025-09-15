import webbrowser

class ChromeLink: 
    def __init__(self,chrome_path):
        self.FAVOURITE_LINKS = {
            "facebook":"https://www.facebook.com",
            "youtube":"https://www.youtube.com",
            "github":"https://www.github.com",
            "reddit":"https://www.reddit.com"
        }
        self.chrome_browser = webbrowser.Chrome(chrome_path)

    def show_favourite_menu(self):
        for link in self.FAVOURITE_LINKS:
            print(link)
        return self.FAVOURITE_LINKS

    def chrome(self,url):
        self.chrome_browser.open_new(url)