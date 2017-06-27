#!/usr/bin/python3
"""Принимает ID игры из стима, выдаёт красивое описание для рутрекера"""

from sys import argv
import json

import requests


TEMPLATE = """
[b][font="Arial"][align=center][size=28]{name}[/size][/align][/font][/b]

[img=right][/img]

[b]Год Выпуска[/b]: {release_date[date]}
[b]Жанр[/b]: {Жанры}
[b]Разработчик[/b]: {Разработчик}
[b]Издательство[/b]: {Издатель} / Steam
[b]Используемые библиотеки[/b]: {libs}
[b]Мультиплеер[/b]:
[b]Архитектура[/b]:
[b]Версия[/b]:
[b]Лицензия[/b]: проприетарная
[b]Язык[/b]: {supported_languages}
[b]Таблэтка[/b]:

[font="Arial"][size=16][b]Системные требования[/b]:[/size][/font]
{reqs}
 
[font="Arial"][size=16][b]Описание[/b]:[/size][/font]

[align=justify][font="Georgia"][size=16]{desc}
[/size][/font][/align]
 

[font="Arial"][size=16][b]Доп. информация[/b]:[/size][/font]

УДАЛИВМЕСТЕСЗАГОЛОВКОМИЛИЗАМЕНИ
 

[font="Arial"][size=16][b]Порядок установки[/b]:[/size][/font]

РАСПАКУЙ @ ИГРАЙ

[align=center]
[font="Arial"][b][size=16]
[url=REPLACEME]Трейлер[/url] \
• [url=REPLACEME]Страничка игры[/url] \
• [url=REPLACEME]Купить в GOG[/url] \
• [url=REPLACEME]Купить в Humble Store[/url] \
[/size][/b][/font]

[hr]
[font="Arial"][color=darkgreen][size=20]Не уходите с раздачи после скачивания!
Поддержите разработчика, купив игру (ссылки выше)![/size][/color][/font]
[/align]
"""
# • [url={url}]Купить в Steam[/url]

URL_T = "http://store.steampowered.com/api/appdetails?l=russian&appids={appid}"


def pretty(s):
    s = s.replace(' - ', ' — ')
    for word in "в во к ко и из за под при на над от до с со не у".split():
        s = s.replace(" {} ".format(word), " {} ".format(word))
    for word in "$ — - ₽ г г. гг гг.".split():
        s = s.replace(" {} ".format(word), " {} ".format(word))
    s = s.replace(":[/b]", "[/b]:")
    s = s.replace(": [/b]", "[/b]: ")
    return s


def unhtml(s, serif_lists=False):
    s = s.strip()
    s = s.replace("<br>", "\n")
    s = s.replace('<ul class="bb_ul">', "[list]\n")
    s = s.replace('<ul>', "[list]\n")
    s = s.replace('</ul>', "\n[/list]")
    s = s.replace("<strong>", "[b]").replace("</strong>", "[/b]")
    s = s.replace("<em>", "[i]").replace("</em>", "[/i]")
    s = s.replace("<i>", "[i]").replace("</i>", "[/i]")
    s = s.replace("<li>", "[*]").replace("</li>", '')
    if serif_lists:
        s = s.replace("[*]", '[*][align=justify][size=16][font="Georgia"]')
        s = s.replace("\n[*]", "[/font][/size][/align]\n[*]")
        s = s.replace("\n[/list]", "[/font][/size][/align]\n[/list]")
    return s


def main():
    """Main Program"""
    appid = argv[1]
    data = requests.get(URL_T.format(appid=appid))
    data = json.loads(data.text)[str(appid)]["data"]
    data["Жанры"] = ", ".join(x["description"] for x in data["genres"])
    data["Разработчик"] = ", ".join(data["developers"])
    data["Издатель"] = ", ".join(data["publishers"])
    data["libs"] = "Native"
    reqs = unhtml("\n\n".join(data["linux_requirements"].values()))
    reqs = reqs.replace("Место на диске", "Жёсткий диск")
    reqs = reqs.replace("GB ОЗУ", "Гб")
    data["reqs"] = pretty(reqs)
    data["desc"] = pretty(unhtml(data["about_the_game"], serif_lists=True))

    print(TEMPLATE.format(**data))


main()
