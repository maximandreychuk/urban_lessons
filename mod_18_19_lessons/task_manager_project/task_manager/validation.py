def validate_data(email, password):
    if '@' not in email:
        return f'Неверный формат email'
    elif len(password) < 8:
        return f'Пароль слишком короткий'
    else:
        return "Данные прошли валидацию"
