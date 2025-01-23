def sign_up_user(first_name, last_name):
    return {"first_name": first_name, "last_name": last_name}

if __name__ == "__main__":
    user = sign_up_user("John", "Doe")
    print(user)