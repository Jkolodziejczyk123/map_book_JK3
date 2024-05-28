def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f'Twój znajomyuser {user["name"]} opublikował: {user["post"]} postów')

