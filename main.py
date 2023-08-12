from Views.MainView import MainView
import customtkinter as ctk

if __name__=="__main__":
    app=ctk.CTk(title="San Pedro")
    main=MainView(app)
    app.mainloop()