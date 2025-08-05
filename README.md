# ao3-archiver

A tool to help archive works from Archive of our Own.

```
$ python ./ao3-archiver.py "Peter Pan - J. M. Barrie"
Searching for works with fandom Peter Pan - J. M. Barrie...
Found 847 works in 24.4 seconds.

Getting results of page 1
Got works of page 1 in 0.3 seconds.
Downloading work 68723741...
Saved to Second to the right - Trovi03.html
Downloading work 68650251...
Saved to Fox in Kensington Gardens - CalliopeWayne.html
Downloading work 68617221...
Saved to Peter and I - dakotathehuman.html
Downloading work 68572356...
Saved to Lust and Pixie Dust - orphan_account.html
Downloading work 68305126...
Saved to Dread Mac Farlane - MarionPoinsot.html
```

## About

I built utility this for the Warrior Cats MAP Archives, which you can find here. It can generate a list of all works from a certain Fandom to a text file. It also saves all works in HTML format.

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

- Peter Pan & Related Fandoms
- Wings of Fire - Tui T. Sutherland
- Homestuck

The operation could take as many as a few hours depending on the size of the collection. The list of URLs will be written to `saves/<fandom>.txt` and the HTML saves will be located in the `saves` folder.

---

[![Bog The MudWing](https://blog.macver.org/content/images/2025/07/Stamp-Colored-Small-Shadow.png)](https://blog.macver.org/about-me)
