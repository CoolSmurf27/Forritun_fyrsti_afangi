def main():
    data = get_data()
    if data is None:
        return

    players_by_name = organize_data(data)
    display_tables(players_by_name)

def get_data() -> list[str] | None:
    filename = input()
    try:
        with open(filename) as file:
            return file.readlines()
    except FileNotFoundError:
        return None

def organize_data(lines: list[str]) -> dict[str, tuple[int, str, int, int]]:
    players_by_name = {}

    for line in lines:
        rank, name, country, rating, year = line.strip().split(';')
        last_name, first_name = name.split(',')
        rank = int(rank)
        last_name = last_name.strip()
        first_name = first_name.strip()
        country = country.strip()
        rating = int(rating)
        year = int(year)
        full_name = f'{first_name} {last_name}'
        player_info = (rank, country, rating, year)
        players_by_name[full_name] = player_info

    return players_by_name

def display_tables(players_by_name: dict[str, tuple[int, str, int, int]]) -> None:
    display_by_country(players_by_name)
    print()
    display_by_birth_year(players_by_name)

def display_by_country(players_by_name: dict[str, tuple[int, str, int, int]]) -> None:
    print_header('Players by country:')
    players_by_country = organize_by_country(players_by_name)
    for country in sorted(players_by_country):
        player_list = players_by_country[country]
        print_subheader(country, player_list)
        for player in player_list:
            print(f'{player[0]:>40}{player[1]:>10}')

def display_by_birth_year(players_by_name: dict[str, tuple[int, str, int, int]]) -> None:
    print_header('Players by birth year:')
    players_by_year = organize_by_birth_year(players_by_name)
    for birth_year in sorted(players_by_year):
        player_list = players_by_year[birth_year]
        print_subheader(birth_year, player_list)
        for player in player_list:
            print(f'{player[0]:>40}{player[1]:>10}')

def print_header(header: str) -> None:
    print(header)
    print('-' * len(header))

def organize_by_country(players_by_name: dict[str, tuple[int, str, int, int]]) -> dict[str, list[tuple[str, int]]]:
    players_by_country = {}
    for name, player_info in players_by_name.items():
        rank, country, rating, year = player_info
        if country not in players_by_country:
            players_by_country[country] = []
        players_by_country[country].append((name, rating))
    return players_by_country

def organize_by_birth_year(players_by_name: dict[str, tuple[int, str, int, int]]) -> dict[int, list[tuple[str, int]]]:
    players_by_year = {}
    for name, player_info in players_by_name.items():
        rank, country, rating, year = player_info
        if year not in players_by_year:
            players_by_year[year] = []
        players_by_year[year].append((name, rating))
    return players_by_year

def print_subheader(category: str, players: list[tuple[str, int]]) -> None:
    number_of_players = len(players)
    ratings = [player[1] for player in players]
    average_rating = average(ratings)
    print(f'{category} ({number_of_players}) ({average_rating:.1f}):')

def average(numbers: list) -> float:
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == "__main__":
    main()





