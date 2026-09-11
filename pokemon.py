import requests
import sys
from pyfiglet import Figlet
import random
import inflect


def get_pokemon_data(prompt):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{prompt}')
        response.raise_for_status()
        json_text = response.json()
        name = json_text['forms'][0]['name']
        pok_id = json_text['id']
        skill_list = []

        for ability in json_text['abilities']:
            skill = ability['ability']
            name_skill = skill['name']
            skill_list.append(name_skill)

    except (requests.HTTPError, requests.JSONDecodeError):
        sys.exit('Couldn\'t reach the server')
    except (requests.ConnectionError, requests.ConnectTimeout):
        sys.exit('Couldn\'t connect to the server')

    return name, pok_id, skill_list


def choose_font(pname, font_name):
    f = Figlet()
    f.setFont(font=font_name, width=200)

    return f.renderText(pname)


def format_text(skills):
    p = inflect.engine()

    return p.join(skills)


def main():
    f = Figlet()
    all_fonts = f.getFonts()
    selected_font = random.choice(all_fonts)

    if len(sys.argv) < 2:
        sys.exit('Too few arguments')

    poke_data = get_pokemon_data(sys.argv[1])

    try:
        name, pok_id, skill_list = poke_data
        result_skill = format_text(skill_list)

        name_convert = choose_font(name, selected_font)

        print('=' * 100)
        print(f'{name_convert}')
        print('=' * 100)
        print(f'* #{pok_id}')
        print(f'* {result_skill}')

    except ValueError:
        sys.exit('Invalid input')


if __name__ == '__main__':
    main()
