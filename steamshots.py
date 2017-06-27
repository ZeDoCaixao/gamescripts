#!/usr/bin/python3
"""steamshots.py

Take screenshots URL for given Steam game.
"""
from sys import argv
import json
import requests

URL_T = "http://store.steampowered.com/api/appdetails?appids={appid}"


def end(mes, err):
    """Print message and finish program with error code err"""
    print(mes)
    exit(err)


def main():
    """Main program"""
    if len(argv) != 2:
        end("usage: steamshots.py AppID", 0)
    if argv[1].isdigit():
        appid = argv[1]
    else:
        try:
            appid = argv[1].split(
                "store.steampowered.com/app/", 1)[1].split("/", 1)[0]
        except IndexError:
            end("Invalid AppID. Use number from game URL or URL itself", 1)
    data = requests.get(URL_T.format(appid=appid))
    try:
        data = json.loads(data.text)[appid]["data"]
    except KeyError:
        end("Can't get game info. Is appid {} correct?".format(appid), 1)
    print(data["name"])
    print(
        "\n".join(i["path_full"].split("?", 1)[0] for i in data["screenshots"]))

main()
