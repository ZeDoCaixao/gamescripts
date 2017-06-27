Readme is in Russian because target audience is Russian-speaking. Sorry
for that. But you can still just read the code. Perhaps I'll make English
readme later.

Небольшие скрипты и утилиты, которые можно использовать для упрощения работы
с играми, а также их заливки на рутрекер, которые я использую сам.
Выкладывается в надежде, что кому-то окажется полезным, но без каких-либо
гарантий. Скорее всего, коллекция будет со временем пополняться.

## gogv

Показывает версию GOG-игры без установки/распаковки оной.

Примеры использования:
````
gogv gog_game_name_2.0.0.1.sh
gogv -v gog_game_name_2.0.0.1.sh

````
С ключом `-v` показывает только версию игры. Без него — версию игры, версию
инсталлера и название игры.

## starthere

Кладёт в каталог с игрой файлик start.sh, стараясь правильно заполнить его.
Требует дальнейшей проверки и редактирования, но это удобнее, чем создавать
каждый раз вручную.

## dlunity

Скачивает Unity3D-плеер заданной версии. Для портирования игр с винды и макоси.

Пример использования:
````
dlunity 5.4.1f1
````

## rutrasteam.py

Выдаёт красиво оформленное описание раздачи для рутрекера. В качестве аргумента
AppID игры в Steam. Заполняет не все поля, но те, которые может: языки,
название и описание игры, дату выпуска, разработчика, издателя и т. д.
Результат требует дальнейшего дозаполнения, но всё равно это удобнее,
чем с нуля.

Пример использования:
````
rutrasteam.py 9000
````

## steamshots.py

Выдаёт ссылки на все скриншоты игры в Steam, которые потом можно удобно
скопипастить например на lostpic.net. В качестве аргумента можно использовать
AppID или всю ссылку на игру в Steam.

Примеры использования:
````
steamshots.py http://store.steampowered.com/app/9000/Spear_of_Destiny/
steamshots.py 9000
````


# Скрипты, не входящие в этот пакет

## activate

Применяет таблетку от ACTiVATED, правильно заполняя activated.ini (интерфейсы
и т. д.). [Activate](https://github.com/ZeDoCaixao/activate).
