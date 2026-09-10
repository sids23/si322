import requests
import json
from bs4 import BeautifulSoup


print("Enter your alpha: ")
alpha = input()
print("Enter your last name: ")
lastname = input()
url = "https://mids.usna.edu/ITSD/mids/drgwq010$mids.actionquery"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://mids.usna.edu",
    "Referer": "https://mids.usna.edu/ITSD/mids/drgwq010$.startup",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

parameters = {
    "P_ALPHA": alpha,
    "P_LAST_NAME": lastname,
    "P_MICO_CO_NBR": "",
    "P_SECOF_COOF_SEBLDA_AC_YR": "2027",
    "P_SECOF_COOF_SEBLDA_SEM": "FALL",
    "P_SECOF_COOF_SEBLDA_BLK_NBR": "1",
    "P_MAJOR_CODE": "",
    "P_NOMI_FORMATTED_NAME": "",
    "Z_ACTION": "QUERY",
    "Z_CHK": "0"
}

cookies = {
    "f5_cspm": "1234",
    "WSG$DGDWQ000$URL0": "/ITSD/mids/dgdwq000$.startup",
    "WSG$DGDWQ000$CAP0": "Academic_Information_-_Query",
    "WSG$DGDWQ000$URL1": "/ITSD/mids/dgdwq000$mids.startup?Z_CHK=0",
    "WSG$DGDWQ000$CAP1": "MIDS",
    "WSG$DRGWQ010$URL0": "/ITSD/mids/drgwq010$.startup",
    "WSG$DRGWQ010$CAP0": "Schedules_-_Query_Midshipmen",
    "WSG$DRGWQ010$URL2": "/ITSD/mids/drgwq010$mids.queryview?K_MIDS_ID=79509&K_SECOF_ID=215252&P_ALPHA=&P_LAST_NAME=&P_MICO_CO_NBR=&P_SECOF_COOF_SEBLDA_AC_YR=&P_SECOF_COOF_SEBLDA_SEM=&P_SECOF_COOF_SEBLDA_BLK_NBR=&P_MAJOR_CODE=&P_NOMI_FORMATTED_NAME=&Z_EXECUTE_QUERY=&Z_START=1&Z_ACTION=&Z_CHK=17540",
    "WSG$DRGWQ010$CAP2": "Schedule",
    "f5avraaaaaaaaaaaaaaaa_session_": "DHAICONIEGIGHAOEONFNNKALIFGAGBEJHGKLKBIAMOCEFOCGILOAEHNHLFJAPKFCEIPDHGKIPGFEIDPCBHLAGKGEBMOPELGEMCPMGCDHEBIHEGPBEOFIBFDFNIPCICHM",
    "_ga": "GA1.1.942230570.1789048806",
    "nmstat": "7048c4ab-b5f9-d7d0-ecbd-02a6626c478d",
    "_ga_LY79N0FLBS": "GS2.1.s1789048805$o1$g1$t1789049009$j59$l0$h0",
    "BIGipServermids_prod": "!PLIDQ1EEH2xqTcx94KzTDZcqOm0eD2fDA1b2XrY49/DjYXTOTGUtNuIa8VYY/k02tW5G8WGteFD3PK8=",
    "OAMAuthnCookie_mids.usna.edu:443": "HRJFrBfRG1xYCZz%2F7ve1mlPaEEErmtbHQXtf9ZV13eapJ5%2Bo58V0sM4Py4faxSrgRp%2Bltz2n9YdufOyVAuGaTTwl1KwNoG5StJ6jDt4GfSUA4DiS8VjGvL3LXMSwtNNo%2FkZcxGoPIzfE4PAT6HHQNqw9WHUtlqxwzbICBA6dq4fJovBLJkvqBpXhJQIuh5YRzJsD%2FK1IaoNOgvu2%2FbMoi3Psxhsem4ZczZbQDZRt8yOhl80a5dZkxuH%2BHdorV9%2FeMjrR75o8IXJ1dYdzLiC8rkLJdxw5SgKUvMqjfgSRel9PCJRMnS23pJQVvI%2F7OamCAmuemKEPoibjJkW8LZsp1PIw5BC14u5YBGgAPpXsZlNkcvkt0YIM4xIeiTDaDNcL2qlbqsRewA654UHSlX7qUFq9iY77h8sdBxr%2FaVLRgUR%2FQQg4z7N1HPz60bKLMnNdILyoi5%2BElLc3bbRJ5uvJp6D8NEErt6aBo%2BCQQmeyfHBQNAj1M%2F8h7anQb4ktv5VGzklrGKVYOvP4YkoxXk9Weyc0ggtN4yRcFJRZkP33PlCfi%2FUKfhfOUMzQn5IWppsWylvA2mf9Y8HuecLIy701eQ%3D%3D",
    "f5avr0528938678aaaaaaaaaaaaaaaa_cspm_": "MKEJCJDFOIFBMNIAGPJIFLHPEJOPGEMDHOHGIBPNCLNGAEFHCJNKFHCELDPGOGOJKPECBJHHFCHEJDHOBLMAMBMNAFIJCMDIFCBFKKDDBAHJCMIAJMMCCDGNAGDOCBOP"
}

response = requests.post(url, headers=headers, data=parameters, cookies=cookies)

#PART 5
soup = BeautifulSoup(response.text, "html.parser")

# Find all tables in the response
tables = soup.find_all("table")

for table in tables:
    for row in table.find_all("tr"):
        cells = row.find_all(["th", "td"])

        values = [cell.get_text(" ", strip=True) for cell in cells]

        if values:
            print(" | ".join(values))

    print("-" * 80)