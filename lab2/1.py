def is_password_good(password:str) -> bool:
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True


if __name__ == '__main__':
    passoword = input("Введите пароль: ").strip()

    print("Надёжный" if is_password_good(passoword) else "Ненадёжный" )