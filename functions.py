def show_signup_page(signup_frame, login_frame):
    signup_frame.pack(fill="both", expand=True)
    login_frame.pack_forget()
    # home_frame.pack_forget()


def show_login_page(signup_frame, login_frame):
    login_frame.pack(fill="both", expand=True)
    signup_frame.pack_forget()
    # home_frame.pack_forget()
