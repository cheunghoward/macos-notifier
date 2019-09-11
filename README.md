# macos-notifier
Python code to create a custom text notification on MacOS.

Specifically, this code counts down the number of business days until a designated date. 

Tested using Python 3.7

To run on a business day basis, run `crontab -e` and add the following line: 

`0 10 * * 1-5 python ~/notifier.py`




