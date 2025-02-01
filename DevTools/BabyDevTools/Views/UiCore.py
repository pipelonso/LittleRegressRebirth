import os

import customtkinter
from Controllers.BabyBottleController import BabyBottleController
from PIL import Image, ImageTk
from Views.Modules.SelectWorld import SelectWorld
from Views.Modules.EditorMain import EditorMain


class UiCore:

    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.minsize(500, 400)

        self.show_start_menu = True

        general_frame = customtkinter.CTkFrame(self.app, fg_color=('#eadbcb', '#34495e'))
        general_frame.pack(padx=0, pady=0, fill='both', expand=True)

        self.general_frame_canvas = customtkinter.CTkCanvas(general_frame,
                                                            width=100, height=100,
                                                            bg='#eadbcb')
        self.general_frame_canvas.place(x=0, y=0)

        general_frame.bind('<Configure>', self.redraw_bg_canvas_content)

        actual_folder = os.path.dirname(__file__)
        image_path = os.path.join(actual_folder, "resources", "welcome_pose.png")

        imagen = Image.open(image_path)
        # imagen = imagen.resize((375, 601))
        self.welcome_image = ImageTk.PhotoImage(imagen)

        self.side_frame = customtkinter.CTkFrame(general_frame, fg_color='#e3ceb9',
                                                 border_color='#C1BAA1',
                                                 border_width=2,
                                                 height=300,
                                                 width=300)
        self.side_frame.place(x=100, y=100)

        lr_title = customtkinter.CTkLabel(self.side_frame, text='LITTLEREGRESS REBIRTH', font=('Arial', 20))
        lr_title.pack(padx=10, pady=5, fill='x')

        dev_tools_text = customtkinter.CTkLabel(self.side_frame, text='devtools for babies')
        dev_tools_text.pack(padx=5, pady=5, fill='x')

        enter_editor_button = customtkinter.CTkButton(self.side_frame, text='Enter into editor', fg_color='#C1BAA1',
                                                      text_color='gray', hover_color='#eadbcb',
                                                      command=lambda: self.show_select_world_module())
        enter_editor_button.pack(padx=5, pady=5, fill='both', expand=True)

        self.select_world_module = SelectWorld(general_frame, self)

        self.editor_main = EditorMain(general_frame, self)

        self.app.mainloop()

        pass

    def init_editor_in_world(self, world: str):
        self.editor_main.set_world(world)
        self.editor_main.pack(padx=10, pady=10, fill='both', expand=True)
        pass

    def place_initial_menu_item(self, event):
        middle_y = event.height / 2
        corner_y_location = middle_y - (self.side_frame.winfo_height() / 2)
        if event.width < 600:
            middle_x = event.width / 2
        else:
            middle_x = (event.width / 3) * 2
            pass

        corner_location = middle_x - (self.side_frame.winfo_width() / 2)
        self.side_frame.place(x=corner_location, y=corner_y_location)
        pass

    def show_select_world_module(self):
        self.select_world_module.pack(padx=10, pady=10, fill='both', expand=True)

    def redraw_bg_canvas_content(self, event):
        self.general_frame_canvas.configure(width=event.width, height=event.height)
        self.general_frame_canvas.delete('all')
        self.general_frame_canvas.create_polygon(
            [
                0, (event.height / 3),
                event.width, (event.height / 3) + (event.height / 3),
                event.width, event.height,
                0, event.height
            ],
            fill='#e3ceb9'
        )

        self.general_frame_canvas.create_image(250, 400, image=self.welcome_image)
        if self.show_start_menu:
            self.place_initial_menu_item(event)
