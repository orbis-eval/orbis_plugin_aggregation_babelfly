import os


def run():
    print("working")

    try:
        key = os.environ['BABELNET_API_KEY']
    except KeyError:
        key = "False"

    if not key:
        print("BABELNET_API_KEY environment variable not set.")
