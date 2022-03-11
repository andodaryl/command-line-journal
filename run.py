'''
Module that starts app.
'''
from python_modules.display_api import display_api as display

def main():
    '''
    Container for main behaviour for application start.
    '''
    # Behaviour
    display.greet_user()
    display.go_to_main_menu()

main()
