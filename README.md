[![Build Status](https://travis-ci.org/vineetpalan/bulk_emailer.svg?branch=master)](https://travis-ci.org/vineetpalan/bulk_emailer)
[![Coverage Status](https://coveralls.io/repos/github/vineetpalan/bulk_emailer/badge.svg?branch=master)](https://coveralls.io/github/vineetpalan/bulk_emailer?branch=master)
# bulk_emailer


**Python Script to send bulk emails using std libs.**

Send bulk emails to send bulk emails from the command line by specifying the recipients in a CSV file and a template having variable placeholders and a subject line.
Requirements
------------

* python >= 2.4

Usage
-----
Setup
~~~~~
Edit the config file before running the script::

Linux Based Machine
    $ vim config.py or pico config.py or gedit config.py

Windows Machine
  Edit config.py using notepad
    
~~~~~~~~~~~
Commandline

The simplest method of sending out a bulk email.

Run a test to predefined test_recipients::

    $ ./bulk_email

    OR
    
    $ python bulk_email emails.csv
    
    OR
    
    $ python bulk_email
