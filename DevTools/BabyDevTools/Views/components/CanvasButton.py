import customtkinter
from typing import Any, Optional


class CanvasButton:

    def __init__(self, master: Any,
                 fg_color: Optional[str] = 'white',
                 width: Optional[int] = 32,
                 height: Optional[int] = 32,
                 command=None,
                 right_click_command=None
                 ):

        self._click_callback = command
        self._right_click_callback = right_click_command

        self.general_frame = customtkinter.CTkFrame(master, width=width, height=height, fg_color=fg_color)
        self._canvas = customtkinter.CTkCanvas(self.general_frame, bg=fg_color,
                                               width=width, height=height, highlightthickness=0)
        self._canvas.pack(padx=3, pady=3, fill='both', expand=True)

        self._canvas.bind('<Button-1>', self.on_click)
        self._canvas.bind('<Button-3>', self.on_right_click)

        pass

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)

    def get_canvas(self) -> customtkinter.CTkCanvas:
        return self._canvas

    def on_click(self, event):
        if self._click_callback is not None:
            return self._click_callback()

    def on_right_click(self, event):
        if self._right_click_callback is not None:
            self._right_click_callback()
