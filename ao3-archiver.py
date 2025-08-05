import argparse
from time import time, sleep
from pathlib import Path

import AO3


def fetch(args):

    save_mode = input(
        "What format would you like to save in?\n1) AZW3\n2) EPUB\n3) HTML\n4) MOBI\n5) PDF\n6) Skip saving\nType a number: "
    )

    save_type = None

    if save_mode == "1":
        save_type = "AZW3"
    elif save_mode == "2":
        save_type = "EPUB"
    elif save_mode == "3":
        save_type = "HTML"
    elif save_mode == "4":
        save_type = "MOBI"
    elif save_mode == "5":
        save_type = "PDF"

    try:
        # Search for all works with a given fandom
        start = time()
        print(f"Searching for works with fandom {args.fandom}...")
        search = AO3.Search(fandoms=args.fandom)
        search.update()

        print(
            f"Found {search.total_results} works in {round(time()-start, 1)} seconds.\n"
        )

        found = 0
        page = 1

        Path("saves").mkdir(parents=True, exist_ok=True)

        # Run until all search results have been found
        while found < search.total_results:
            print(f"\nGetting results of page {page}")
            start = time()

            # Get the works of this page
            search.page = page
            search.update()
            print(f"Got works of page {page} in {round(time()-start, 1)} seconds.\n")

            # Add each to the file
            for result in search.results:
                found += 1
                with open(f"saves/{args.fandom}.txt", "a+", encoding="utf-8") as myfile:
                    myfile.write(
                        f"https://archiveofourown.org/works/{result.id}?view_adult=true&view_full_work=true\n"
                    )
                if save_type is not None:
                    with open(
                        f"saves/{result.title} - {result.authors[0].username}.{save_type.lower()}",
                        "wb",
                    ) as file:
                        print(f"Downloading work {result.id}...")
                        start = time()
                        work = AO3.Work(result.id)
                        file.write(work.download(save_type))
                        print(
                            f"Saved to {result.title} - {result.authors[0].username}.html in {round(time()-start, 1)} seconds."
                        )

            print(
                f"That's {found} works found out of {search.total_results} total works."
            )
            # Go to next page
            page += 1
            # Wait half a second to prevent overloading or rate limiting
            sleep(0.5)

    except KeyboardInterrupt:
        print("Operation canceled.")


parser = argparse.ArgumentParser(
    description="A tool to help archive works from Archive of our Own."
)
parser.add_argument("fandom", type=str, help="the name of the fandom to search for")
parser.set_defaults(func=fetch)

args = parser.parse_args()

args.func(args)
