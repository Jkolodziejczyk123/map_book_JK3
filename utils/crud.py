def read(user_list: list[dict]) -> None:
    for user in user_list:
        print(f'Twój znajomy {user["name"]} opublikował: {user["post"]} postów')

def add_user(users: list) -> None:
    user_name = input('Podaj imie')
    user_surname = input('Podaj nazwisko')
    user_post = input('Podaj liczbe postów')


