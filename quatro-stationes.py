#!/usr/bin/python

# python quatro-stationes.py

import calendar, time
import sys
import os

dirname, filename = os.path.split(
  os.path.abspath(sys.argv[0]))

file1 = dirname + os.path.sep + "seasons-utc-list.txt"

intervals = (
  ('d', 86400),   # 60 * 60 * 24
  ('h', 3600),    # 60 * 60
  ('min', 60),
)

def days_hours_mins (seconds):
  seconds = int (seconds)
  result = []
  for name, count in intervals:
    value = seconds // count
    seconds = seconds - value * count
    result.append (value)
  return result

def tm (t):
  return calendar.timegm (time.strptime (t,'%Y-%m-%d %H:%M'))

def diff_str (dates,now):
  dlist = []
  for ds in dates:
    st = ds [:2]
    rest = ds [3:].strip ()
    then = tm (rest)
    delta = abs (now - then)
    sign = 1 if now - then >= 0 else -1
    days,hours,mins = days_hours_mins (delta)
    dlist = (dlist + [(st,sign,days,hours,mins)]) [-2:]
    if sign == -1: 
      break
  result = []
  for st,sign,days,hours,mins in dlist:
    pm = "+" if sign == 1 else "−"
    rs = f"{st} {pm} {days} d {hours} h {mins} min"
    result.append (rs)
  return result

with open (file1) as f:
  dates = f.readlines ()
 
now = time.time ()

result = diff_str (dates,now)
print ("\n".join (result))

# Just use
# :!chmod +x %

