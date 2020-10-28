"""
Utilities for POTUS info
"""
from datetime import date
DATA_FILE = 'DATA/presidents.txt'

from pprint import pprint

def main():
    for term in range(1, 46):
        data = get_info(term)
        pprint(data)
        print('-' * 60)


def get_info(term_wanted):
    """
    Retrieve info for one president

    Define keys here...

    :param term_wanted: Term number as integer
    :return: Dictionary of info, with keys "first_name", "last_name", etc.
    """
    if (term_wanted < 1) or (term_wanted > 45):
        raise ValueError("Term number must be in range 1-45")

    with open(DATA_FILE) as pres_in:
        for raw_line in pres_in:
            line = raw_line.rstrip()
            (raw_term_number, first_name, last_name, dob, dod, birthplace, birthstate, took_office, left_office,
             party) = line.split(':')
            term_number = int(raw_term_number)
            if term_number == term_wanted:
                return {
                    'term_number': term_number,
                    'first_name': first_name,
                    'last_name': last_name,
                    'party': party,
                    'birthdate': _convert_string_to_date(dob),
                    'deathdate': _convert_string_to_date(dod),
                    'tookoffice': _convert_string_to_date(took_office),
                    'leftoffice': _convert_string_to_date(left_office),
                    'birthstate': birthstate,
                    'birthplace': birthplace,
                }

def _convert_string_to_date(date_string):
    if date_string == 'NONE':
        return None

    year_str, month_str, day_str = date_string.split('-')
    new_date = date(int(year_str), int(month_str), int(day_str))
    return new_date

if __name__ == '__main__':
    main()





