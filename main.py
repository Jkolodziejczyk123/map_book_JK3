users: list[dict] = [
    {'name': 'Jakub', 'surname': 'Kołodziejczyk', 'post':2},
    {'name': 'Kacper', 'surname': 'Macioch', 'post':5},
    {'name': 'Dominik', 'surname': 'Kuźnik', 'post':8},
    {'name': 'Michał', 'surname': 'Krzywiński', 'post':10},

]
def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f'Twój znajomyuser {user["name"]} opublikował: {user["post"]} postów')

if __name__ == '__main__':
    print("Witaj użytkowniku")
    while True:

        print("Menu:")
        print("1. Wyświetl co u znajomych")
        menu_option:str=input("Dokonaj wybory")
        if menu_option == "0":
            print("Program kończy pracę")
            break
        if menu_option == "1":
            show_users(users)


