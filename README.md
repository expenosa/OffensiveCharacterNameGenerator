# Offensive Character Name Generator

Generate offensive custom character names based on urban dictionary entries. Perfect for speedruns or races.

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

## Running

You need:

- Python 3.8+

Double-click `run.bat` on Windows or `python3 random_name.py` on other platforms.

*The first run will generate a `cfg/names.txt` file that holds all the filtered entries the urban dictionary dump. Future runs will just read this file.*

Keep pressing Enter to generate new names.

## About

This uses entries from Urban Dictionary scraped using [this tool](https://github.com/mattbierner/urban-dictionary-word-list). Use this tool to scrape more up to date entries. Last scrape was March 2023.

