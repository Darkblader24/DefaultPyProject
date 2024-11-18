import argparse
import datetime
import sys
import time


def main(argv: list[str] | str) -> None:
    """
    The main function of the script.
    :param argv: The arguments passed to the script.
    :return: None
    """
    start_time = time.time()

    # Parse arguments
    print(f"Starting ... with arguments: {' '.join(argv)}\n")
    if argv and argv[0].endswith(".py"):
        argv = argv[1:]
    parser = argparse.ArgumentParser(description="This is such a cool app!")
    parser.add_argument("--string", type=str, help="A string!")
    parser.add_argument("--a-bool", action="store_true", help="A bool!")
    args = parser.parse_args(args=argv)

    # Do cool stuff
    ...

    # Finish script
    total_time = int(time.time() - start_time)
    print(f"\n-> Finished in {datetime.timedelta(seconds=total_time)}")


if __name__ == "__main__":
    """ This block is executed when the script is run from the command line. """
    main(sys.argv)
