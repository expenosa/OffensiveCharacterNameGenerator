# Offensive Character Name Generator

Generate offensive custom character names based on Urban Dictionary entries. Perfect for speedruns or races.

The default configuration generates names based on From Software characters from SoulsBorne games.

**Quality of names generated is not guaranteed. Offensiveness however is almost certain.**

## Examples

These are ten examples of normal output. More offensive names and stronger language could not be presented here.

```
Volcan Mind Wank Logarius
Sophisticated Bad Bitch Morgott
Honk Your Cock Isshin Ashina
Gay Basher Yuria
Anime Boobs Vamos
Dick Addict Kalameet
Crazy Psycho Bitch Ludwig
Quirky Queer Dragon God
Schloppy Boobs Latenna
Itchy Asshole Beastman
```

## Running (Simple)

You need:

- Python 3.8+

Double-click `run.bat` on Windows or `python3 random_name.py` on other platforms.

*The first run will generate a `cfg/names.txt` file that holds all the filtered entries the urban dictionary dump. Future runs will just read this file.*

Keep pressing Enter to generate new names.

## Running (Advanced)

Additional arguments can be provided for extra filtering. Run the program with a `-h` argument to see a full list.

```
$: python random_name.py -h
usage: Offensive Character Name Generator [-h] [-c CHARACTER_LIMIT] [-i INCLUDE] [-e EXCLUDE]

optional arguments:
  -h, --help            show this help message and exit
  -c CHARACTER_LIMIT, --character-limit CHARACTER_LIMIT
                        Max number of characters (excluding spaces) in the base UD name
  -i INCLUDE, --include INCLUDE
                        Filter to only generate names containing these words (separated by spaces)
  -e EXCLUDE, --exclude EXCLUDE
                        Filter out names containing these words (separated by spaces)
```

### Example

```
python random_name.py -i cum -e scum -c 13
```

## Full Customisation

From the `cfg` directory:
- Edit the `whitelist.txt` and `blacklist.txt` to contain character sequences that should be included/excluded from the urban dictionary dump.
- Delete `names.txt` if it exists. 
- Run the program normally. This will generate a new `names.txt` file conforming to the whitelist/blacklist. **Repeat these steps again if the whitelist/blacklist changes.**
- Edit `character_names.txt` as you see fit.

---

By default, Urban Dictionary entries between 2 to 4 words are selected when creating the `names.txt` file. This can be changed by creating a `config.ini` file in the `cfg` directory with the following contents. **`names.txt` must be deleted before running the program again for this change to apply.**

```
[URBANDICT]
MinWordsPerName = 4
MaxWordsPerName = 5
```

## About

This uses entries from Urban Dictionary scraped using [this tool](https://github.com/mattbierner/urban-dictionary-word-list). Use this tool to scrape more up to date entries. Last scrape was March 2023.

