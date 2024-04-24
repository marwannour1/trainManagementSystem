from home_gui import *
import sys
from controllers.home_controller import*

def main():
    root = tk.Tk()
    controller = HomeController()
    home_page = HomePage(root, controller)
    home_page.create_main_page()

    root.mainloop()

main()