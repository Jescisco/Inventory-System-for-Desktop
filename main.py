from Resources.Includes.Modules import *
from Views.MainView import MainView

if __name__=="__main__":
    app=CTk()
    app.geometry("274x350")
    app.resizable(False, False)
    MainView(app)
    app.mainloop()