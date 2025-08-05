import argparse
from time import time, sleep
from pathlib import Path

import AO3

def fetch(args):

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
                with open(f"saves/{result.title} - {result.authors[0].username}.html", "wb") as file:
                    print(f"Downloading work {result.id}...")
                    start = time()
                    work = AO3.Work(result.id)
                    file.write(work.download("HTML"))
                    print(f"Saved to {result.title} - {result.authors[0].username}.html in {round(time()-start, 1)} seconds.")
            print(
                f"\nThat's {found} works found out of {search.total_results} total works."
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
parser.add_argument(
    "fandom", type=str, help="the name of the fandom to search for"
)
parser.set_defaults(func=fetch)

args = parser.parse_args()

args.func(args)
