# pokemon-cli-generator

## Project Spotlight: Poké-Card CLI Generator

## Poké-Card CLI Generator

This project is an advanced implementation developed during **Week 4 (Libraries)** of Harvard's **CS50P**. It serves as a comprehensive capstone for the module, integrating command-line arguments, external APIs, and third-party styling libraries.

## Project Overview
The **Poké-Card Generator** is a CLI tool that fetches real-time data from the [PokéAPI](https://pokeapi.co/) and generates a stylized "info card" in the terminal. It transforms raw JSON data into a visually appealing layout using ASCII art and grammatically correct text formatting.

## Features

- **External API Integration:** Consumes RESTful data using the `requests` library, including robust error handling for network timeouts and 404 status codes.
- **Nested JSON Navigation:** Implements complex data mining to extract information from nested dictionaries and lists (e.g., retrieving specific ability names from multiple layers of nesting).
- **The Accumulator Pattern:** Utilizes loops and `.append()` to dynamically build lists of Pokémon skills.
- **Modular Architecture:** The program is divided into specialized "Worker" functions for data fetching, font rendering, and text formatting, orchestrated by a "Manager" (`main`) function.
- **Tuple Unpacking:** Efficiently handles multiple return values from functions to keep the code clean and "Pythonic."

### Libraries Used

| Library | Purpose |
| :--- | :--- |
| `requests` | To communicate with the PokéAPI and retrieve Pokémon data. |
| `pyfiglet` | To convert the Pokémon's name into stylized ASCII Art. |
| `inflect` | To format the list of abilities using the Oxford Comma. |
| `sys` | To handle command-line arguments. |
| `random` | To select a different font style for every search. |

### How to Use

**Install Dependencies:**
   pip install requests pyfiglet inflect
**Run the program:**
   python pokemon2.py pokemon name

<img width="484" height="290" alt="Screenshot 2026-04-15 124151" src="https://github.com/user-attachments/assets/7bd77eaf-6ff3-4b74-ad39-da49cdf4802d" />

<img width="969" height="372" alt="Screenshot 2026-04-15 124242" src="https://github.com/user-attachments/assets/fa715cf9-ef21-48bd-b90d-571aac7cd8fc" />

<img width="495" height="231" alt="Screenshot 2026-04-15 124035" src="https://github.com/user-attachments/assets/b464173e-58d8-44ba-a4d1-a8a83cfd436b" />
