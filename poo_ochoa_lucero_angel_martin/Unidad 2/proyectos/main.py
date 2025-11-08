#pip install -r requirements.txt
from tkinter import Tk
from login_viw import LoginApp

def main():
    root = Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()