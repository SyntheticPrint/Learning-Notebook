import customtkinter

app = customtkinter.CTk()
app.title("Learning Notebook")

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

main_label = customtkinter.CTkLabel(master=app, text="Learning Notebook",
                                    font=customtkinter.CTkFont(size=120, weight="bold"), text_color="blue")
main_label.place(relx=0.5, rely=0.02, anchor=customtkinter.N)

frame = customtkinter.CTkFrame(master=app,
                               width=800,
                               height=1100,
                               corner_radius=8)
frame.place(relx=0.385, rely=0.15)

open_notebook_button = customtkinter.CTkButton(master=app,
                                               width=670,
                                               height=200,
                                               border_width=0,
                                               corner_radius=8,
                                               text="OPEN",
                                               font=customtkinter.CTkFont(size=80, weight="bold")
                                               # TODO: Program command to open notebook/database page and close main
                                               #  window.
                                               )
open_notebook_button.place(relx=0.405, rely=0.2)

option_button = customtkinter.CTkButton(master=app,
                                        width=675,
                                        height=200,
                                        border_width=0,
                                        corner_radius=8,
                                        text="OPTIONS",
                                        font=customtkinter.CTkFont(size=80, weight="bold")
                                        # TODO: Program command to open options menu and close main window.
                                        )
option_button.place(relx=0.405, rely=0.47)

quit_button = customtkinter.CTkButton(master=app,
                                      width=675,
                                      height=200,
                                      border_width=0,
                                      corner_radius=8,
                                      text="QUIT ",
                                      font=customtkinter.CTkFont(size=80, weight="bold")
                                      # TODO: Program command to close program.
                                      )
quit_button.place(relx=0.405, rely=0.75)

app.mainloop()
