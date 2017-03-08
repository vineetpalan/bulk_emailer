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
    $ vim config.py

Windows Machine
  Edit config.py using notepad
    
~~~~~~~~~~~
Commandline

The simplest method of sending out a bulk email.

Run a test to predefined test_recipients::

    $ ./BulkEmail
