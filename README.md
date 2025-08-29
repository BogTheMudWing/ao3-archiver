# ao3-archiver

A tool to help archive works from Archive of our Own.

```
$ python ./ao3-archiver.py "Peter Pan - J. M. Barrie"
What format would you like to save in?
1) AZW3
2) EPUB
3) HTML
4) MOBI
5) PDF
6) Skip saving
Type a number: 2
Searching for works with fandom Peter Pan - J. M. Barrie...
Found 848 works in 0.2 seconds.


Getting results of page 1
Got works of page 1 in 0.2 seconds.

Downloading work 68745061...
Saved to Never Never Land: Impaler - MikeyM.html in 21.3 seconds.
Downloading work 68723741...
Saved to Second to the right - Trovi03.html in 2.0 seconds.
Downloading work 68650251...
Saved to Fox in Kensington Gardens - CalliopeWayne.html in 1.7 seconds.
Downloading work 68617221...
Saved to Peter and I - dakotathehuman.html in 1.7 seconds.
```

 > [!NOTE]
 > This repository is mirrored to [GitHub](https://github.com/BogTheMudWing/ao3-archiver) for visibility. Issues and pull requests should be made on [Macver Code Athenaeum](https://code.macver.org/Bog/ao3-archiver).

## About

I built utility this for the Warrior Cats MAP Archives, which you can find [here](https://wcmaparchives.macver.org/). It can generate a list of all works from a certain Fandom to a text file. You can also choose to save all works at AZW3, EPUB, HTML, MOBI, or PDF.

## Preparation

First, install Python 3: https://wiki.python.org/moin/BeginnersGuide/Download

Download this repository by clicking **Code**, then **Download ZIP**. Extract it to a convenient location.

In a terminal, navigate to the extracted repository using the `cd` command. You can usually just type `cd ` and then drag and drop the folder into the terminal window. Press enter.

Install ao3_api using pip:

```
pip install ao3_api
```

## Usage

```
python ./ao3-archiver.py <fandom>
```

Replace `<fandom>` with the name of the fandom you want to get the works of. This should be the same as it appears on the Archive of our Own website. Examples:

```
python ./ao3-archiver.py "Peter Pan & Related Fandoms"
python ./ao3-archiver.py "Wings of Fire - Tui T. Sutherland"
python ./ao3-archiver.py Homestuck
```

When prompted, type a number and press enter to choose a save format.

The operation could take as many as a few hours depending on the size of the collection. The list of URLs will be written to `saves/<fandom>.txt` and the HTML saves will be located in the `saves` folder.

---

[![Bog The MudWing](https://blog.macver.org/content/images/2025/07/Stamp-Colored-Small-Shadow.png)](https://blog.macver.org/about-me)
