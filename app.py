"""
Simple Internet Browser built with BeeWare library in Python
Follow us on Twitter @PY4ALL
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER


class SimpleInternetBrowser(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        search_box = toga.Box(style=Pack(direction=ROW))
        self.set_url_button = toga.Button("Browse", style=Pack(alignment=CENTER, background_color="blue", color='white'), on_press=self.set_url)
        self.url_input = toga.TextInput(style=Pack(flex=1, alignment=CENTER), placeholder='enter website url here')
        self.url_input.MIN_WIDTH = 20
        search_box.add(self.url_input)
        search_box.add(self.set_url_button)
        self.webview1 = toga.WebView(style=Pack(flex=1, padding=2), on_webview_load=self.on_webview_load)
        main_box.add(search_box)
        main_box.add(self.webview1)

        
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def set_url(self, widget):
        if any([self.url_input.value.startswith("http"), self.url_input.value.startswith("file://")]):
            url = self.url_input.value
        else:
            url = "https://" + self.url_input.value
            
        self.webview1.url = url
        #self.content.refresh()


    def on_webview_load(self, _interface):
        self.url_input.value = self.webview1.url



def main():
    return SimpleInternetBrowser()
