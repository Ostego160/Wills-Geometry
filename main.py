from gui import *

def main():
    window = Tk()
    window.title('Will\'s Geometry Funtime')
    window.geometry('512x612')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()
