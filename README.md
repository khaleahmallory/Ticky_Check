# Ticky_Check
Ticky_Check is a script used to parse and organize log files using some Python tools. The repo will include the script and supporting files.

Imagine you are trying to parse a huge log file and organize it. How would you do that through automation? That is what ticky_check.py is for. It takes a log file, syslog.log, and parses it using Python's regex. After parsing the file it organizes it into two seperate csv files that will later be transformed into tables. The first table visualizes the count for each error that exists in the log, this table will be names "Error Message". The second table takes an alysis of each user's statistics for the INFO and ERROR logs, this is the "User Statistics" table. The ticky_check.py script will only organize the log files into seperate csv files. The csv_to_html.py script will be responsible for converting the csv files to HTML, visualizing the data in a table. To view the HTML pages, type the following URL into your browser: [local-IP]/[html-filename].html

(This project is apart of a course issued by Google and Coursera : Using Python to Interact with the Operating System) 
