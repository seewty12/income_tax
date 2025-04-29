def create_account(name,phone_no,password):
    if len(password) >= 8:
        if password.isalnum:
            print(password)
        else:
            print("the password should alpha numeric")

    else:
        print("the password should be have minimum 8values")

name="Yashwanth s"
phone_no=97896356157
password="keer@12543"
create_account(name,phone_no,password)












