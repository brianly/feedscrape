RSS Scraper
===========

This is a simple tool written in Python showing how to consume an RSS feed and output it as JSON.

It is best to use a [virtualenv](http://www.virtualenv.org/en/latest/index.html) for managing dependencies. Anyone who
already knows about this tool shouldn't have a problem with installing the required libraries.

Dependencies on Linux
---------------------

Open a terminal or SSH into a remote machine as root, or with an account that can is member of the sudoers group. On
many machines you can execute pip immediately. If it is not installed then get it using easy_install:

    easy_install pip (if you are root) or sudo easy_install pip (if you need sudo)

Next install the dependencies using pip:

    sudo pip install feedparser

Dependencies on Windows
-----------------------
Open an administrator command prompt. Run easy_install to check if it is configured.

Install pip by executing the following command if you don't have pip already:

    easy_install pip

Next install the dependencies using pip:

    pip install feedparser

Usage
-----

To return output to the console run:

    python rss2json.py
