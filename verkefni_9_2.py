import sys

COUNTRIES_OF_THE_WORLD = "countries.txt"
INPUT_PROMPT = "Enter a suffix for a country: "


def main():
    country_suffix = get_suffix()
    country_names = find_countries_with_suffix(country_suffix)
    print_country_names(country_names, country_suffix)


def get_suffix():
    sys.stderr.write(INPUT_PROMPT)
    return input()


def find_countries_with_suffix(suffix):
    country_names = []

    with open(COUNTRIES_OF_THE_WORLD, "r") as file:
        for line in file:
            line = line.strip()
            if line.endswith(suffix):
                country_names.append(line)

    return country_names


def print_country_names(country_names, suffix):
    for country in country_names:
        print(country)

    print(f"{len(country_names)} countries with suffix {suffix} in total")


if __name__ == "__main__":
    main()



























































