#!/usr/bin/env python3

import argparse
import sys
try:
    from selenium import webdriver
except Exception as e:
    print("Missing Python modules. Exiting...")
    print("    {}".format(str(e)))
    sys.exit(1)

DRIVER = None
URLS = []


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="File with a list of URLs")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", action="store_true", help="FirefoxDriver (Default). Requires 'firefox' and 'geckodriver'")
    group.add_argument("-c", action="store_true", help="ChromeDriver. (Not Implemented)")
    group.add_argument("-p", action="store_true", help="PhantomJS Driver. (Not Implemented)")

    args = parser.parse_args()
    print(args)

    try:
        with open(args.file, "r") as f:
           URLS = f.readlines() 
        URLS = [x.strip() for x in URLS]
    except Exception as e:
        print("Could not open file: {}".format(args.file))
        print("    {}".format(str(e)))
        sys.exit(1)
    for url in URLS:
        print(url)

    sys.exit(0)

    # FirefoxDriver (Default)
    if (not args.f and not args.c and not args.p) or args.f:
        print("Trying FirefoxDriver")
        options = webdriver.FirefoxOptions()
        #options.add_argument("-headless")
        options.add_argument("-private")
        try:
            DRIVER = webdriver.Firefox(firefox_options=options)
        except Exception as e:
            print("Could not use FirefoxDriver")
            print(e)
            sys.exit(1)
    elif args.c:
        print("chrome")
        print("Not Implemented")
        sys.exit(1)
    elif args.p:
        print("phantomjs")
        print("Not Implemented")
        sys.exit(1)

    print("...Successful")



    DRIVER.close()
