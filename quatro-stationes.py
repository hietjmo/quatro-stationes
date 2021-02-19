#!/usr/bin/python

# python quatro-stationes.py

from datetime import date, datetime
import sys
import os

dirname, filename = os.path.split(
  os.path.abspath(sys.argv[0]))

file1 = dirname + os.path.sep + "seasons-utc-list.txt"

with open (file1) as f:
  dates = f.readlines ()
 
now = datetime.now()

def dt (t):
  return datetime.strptime (t,'%Y-%m-%d %H:%M')

def days_hours_mins(td):
  return td.days, td.seconds//3600, (td.seconds//60)%60

dlist = []
for ds in dates:
  st = ds [:2]
  rest = ds [3:].strip ()
  delta = now - dt (rest)
  days,hours,mins = days_hours_mins (delta)
  dlist = (dlist + [(st,days,hours,mins)]) [-2:]
  if days < 0: 
    break

result = []
for st,days,hours,mins in dlist:
  pm = "+" if days >= 0 else "−"
  ds = abs (days)
  rs = f"{st} {pm} {ds} d {hours} h {mins} min"
  result.append (rs.replace("-","−"))

print ("\n".join (result))


# Just use
# :!chmod +x %

