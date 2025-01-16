import customtkinter


class UiCore:

    def __init__(self):

        self.app = customtkinter.CTk()

        general_frame = customtkinter.CTkFrame(self.app, fg_color=('#fff3e0', '#34495e'))
        general_frame.pack(padx=1, pady=1, fill='both', expand=True)

        sup_frame = customtkinter.CTkFrame(general_frame, fg_color=('#FFAFCC', '#808b96'))
        sup_frame.pack(padx=2, pady=2, fill='x')

        app_title_label = customtkinter.CTkLabel(sup_frame,
                                                 text="LITTLEREGRESS REBIRTH",
                                                 font=('Arial', 20)
                                                 )
        app_title_label.pack(padx=2, pady=2, fill='x')

        app_subtitle_label = customtkinter.CTkLabel(sup_frame,
                                                    text="⚒ Devtools for babies 🍼")

        app_subtitle_label.pack(padx=2, pady=2, fill='x')
        self.app.mainloop()

        pass
