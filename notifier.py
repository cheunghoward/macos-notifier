import subprocess
import numpy

def osx_notify(msg):
    subprocess.call("osascript -e 'display notification \"%s\" with title \"How Many Days Left\"'" % msg ,shell=True)


today = numpy.datetime64('today')

## Change date here
end_date = numpy.datetime64('2021-01-01')

days = numpy.busday_count(today,end_date) + 1
osx_notify('%d Business Days' % days)
