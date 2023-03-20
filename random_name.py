import os, sys
from random import randint
from string import capwords

UD_DATA = 'data/'
CFG_DIR = 'cfg/'
WHITELIST_FILE = CFG_DIR + 'whitelist.txt'
BLACKLIST_FILE = CFG_DIR + 'blacklist.txt'
CHARACTERS_FILE = CFG_DIR + 'character_names.txt'
DB_FILE = CFG_DIR + 'names.txt'


def add_names_in_file(filter_func, input_file_path, output_file):
    with open(input_file_path, encoding="utf8") as txt:
        lines = txt.readlines()

    for l in lines:
        if filter_func(l):
            output_file.write(l)


def read_lines(file_path):
    lines = []
    with open(file_path, encoding='utf-8') as white:
        for line in white.readlines():
            # remove white spaces, to lowercase, remove any double quotes
            line_normal = line.strip().lower().replace('"', '') 
            lines.append(line_normal)
    return lines



class NameGenerator:
    def generate() -> str:
        raise RuntimeError("Not Implemented")


class OffensiveNameGenerator(NameGenerator):
    def __init__(self) -> None:
        super().__init__()
        self._blacklist = []
        self._whitelist = []
        self._names = []

        self.__init_db()
    

    def __init_db(self):
        ## create db
        try:
            self.__create_db()
        except Exception as e:
            os.remove(DB_FILE)
            raise e

        # load db
        if not self._names:
            with open(DB_FILE, encoding="utf8") as f:
                self._names = f.readlines()


    def __create_db(self):
        if (os.path.exists(DB_FILE)):
            return

        # Load filters
        self._whitelist = read_lines(WHITELIST_FILE)
        self._blacklist = read_lines(BLACKLIST_FILE)        
        
        print("Creating names database...", file=sys.stderr)
        with open(DB_FILE, 'w', encoding="utf8") as names:
            for f in os.listdir(UD_DATA):
                if not f.endswith('.data'):
                    continue
                input = os.path.abspath(UD_DATA + "/" + f)
                add_names_in_file(self.__accept_line, input, names)
        print("Database creation complete!", file=sys.stderr)


    def __accept_line(self, line: str) -> bool:
        line = line.lower()
        # Filter out singulars
        if line.startswith('a ') or line.startswith('an '):
            return False

        # Filter out crap starting with non-alphanumeric characters
        if not line[0].isalnum():
            return False

        # Only select lines that are 2 or 3 words long
        words = line.count(' ') + 1
        if words < 2 or words > 3:
            return False
        
        # Filter out lines using words in blacklist.txt
        for b in self._blacklist:
            if b in line:
                return False

        # Filter in lines using words in whitelist.txt
        for w in self._whitelist:
            if w in line:
                return True

        return False
    

    def generate(self) -> str:
        max = len(self._names)-1
        choice = self._names[randint(0, max)].strip()
        return capwords(choice)
    


class OffensiveFromSoftNameGenerator(OffensiveNameGenerator):
    def __init__(self) -> None:
        super().__init__()
        self._characters = []
        self.__load_names()


    def __load_names(self):
        # load character names
        if not self._characters:
            with open(CHARACTERS_FILE, encoding='utf-8') as f:
                self._characters = list(set(f.readlines()))


    def generate(self) -> str:
        max = len(self._characters)-1
        character = self._characters[randint(0, max)].strip()
        return f"{super().generate()} {character}"




def print_random_name(gen: NameGenerator):
    name = gen.generate()
    print(f"{name}", end='')



def main():
    gen = OffensiveFromSoftNameGenerator()

    print("Generating names. Press enter to generate new names.")
    print_random_name(gen)
    while input("") == '':
        print_random_name(gen)


if __name__ == '__main__':
    main()