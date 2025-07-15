"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Dušan Machů
email: dumadum@centrum.cz
"""

import sys
import csv
import requests
from bs4 import BeautifulSoup as bs

def format_link(part_link: str) -> str:
    return f"https://www.volby.cz/pls/ps2017nss/{part_link}"

def get_parsed_response(url: str) -> bs:
    return bs(requests.get(url).text, features="html.parser")

def url_list(url: str, start_arg: str) -> list:
    """
    Getting list of commplete selected (started with) urls from links in the given url.
    """
    links = get_parsed_response(url).find_all("a", href=True)
    filtered_links = [link["href"] for link in links if link["href"].startswith(start_arg)]
    return [format_link(part_link) for part_link in filtered_links]

def check_args() -> None:
    """
    Check the inserted arguments:
    1. Whether there are both 2 required arguments.
    2. Whether the first argument contains correct url.
    3. Whether the second argument is of required '.csv' file type.
    """
    url = "https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    
    if len(sys.argv) != 3:
        print("Incorrect number of arguments.")
        print("Required: python main.py 'argument1' 'argument2'")
        sys.exit(1)
    elif not [url for url in url_list(url, "ps32") if url in sys.argv[1]]:
        print("The url in the first argument is not correct.")
        sys.exit(1)
    elif not sys.argv[2].endswith(".csv"):
        print("The second argument is not of required '.csv' file type.")
        sys.exit(1)
    else:
        print(f"DOWNLOADING DATA FROM THE CHOSEN URL: {sys.argv[1]}")

def unique_url_list() -> list:
    """
    Assures that each link will be only once in the resulting list.
    """
    unique_url_list = []
    [unique_url_list.append(url) for url in url_list(sys.argv[1], "ps311") if url not in unique_url_list]
    return unique_url_list

def get_row_attr(tr_tag_1: "bs.element.ResultSet", tr_tag_2: "bs.element.ResultSet") -> dict:
    """
    Assign data from certain cells in table rows and give dictionary.
    """
    return {
        "code": tr_tag_1[0].get_text(),
        "location": tr_tag_1[1].get_text(),
        "registered": tr_tag_2[3].get_text(),
        "envelopes": tr_tag_2[4].get_text(),
        "valid": tr_tag_2[7].get_text()
    }

def data_entry(data: list) -> None:
    """
    Writing data from parameter "data" into csv file given as a second system argument.
    """
    with open(sys.argv[2], mode="w", newline="", encoding="UTF-8-sig") as csv_file:
        columns = data[0].keys()
        entry = csv.DictWriter(csv_file, fieldnames=columns, delimiter=";")
        entry.writeheader()
        entry.writerows(data)
    
    print("ENDING electoral scraper")

def electoral_scraper() -> None:
    check_args()
    
    results = []
    tables_1 = get_parsed_response(sys.argv[1]).find_all("table", {"class": "table"})
    for table in tables_1:
        all_tr_1 = table.find_all("tr")
        for tr in all_tr_1[2:]:
            td_1 = tr.find_all("td")
            code = td_1[0].text
            for link in unique_url_list():
                if code in link:
                    tables_2 = get_parsed_response(link).find("table", {"id": "ps311_t1"})
                    all_tr_2 = tables_2.find_all("tr")
                    for tr in all_tr_2[2:]:
                        td_2 = tr.find_all("td")
                        data = get_row_attr(td_1, td_2)
                    tables_3 = get_parsed_response(link).find_all("table", {"class": "table"})
                    for table in tables_3[1:]:
                        all_tr_3 = table.find_all("tr")
                        for tr in all_tr_3[2:]:
                            td_3 = tr.find_all("td")
                            key = td_3[1].get_text()
                            value = td_3[2].get_text()
                            if key != "-":
                                data.update({key: value})
                    results.append(data)

    print(f"SAVING DATA INTO THE FILE: {sys.argv[2]}")

    data_entry(results)

if __name__ == "__main__":
    electoral_scraper()