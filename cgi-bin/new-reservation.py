#!/usr/bin/env python
from modules.core.core import *
from modules.database import database as db
from datetime import datetime
import re

SQL_TABLES_AVAILABLE = "SELECT id FROM tables WHERE id NOT IN (SELECT tableNr FROM reservations WHERE (CAST(strftime('%s', ?) AS INTEGER) BETWEEN CAST(strftime('%s', dateAndTime) AS INTEGER) AND CAST(strftime('%s', dateAndTime) AS INTEGER) + 7200) OR (CAST(strftime('%s', dateAndTime) AS INTGER) BETWEEN CAST(strftime('%s', ?) AS INTEGER) AND CAST(strftime('%s', ?) AS INTEGER) + 7200)) LIMIT 1"


SQL_NEW_RESERVATION = "INSERT INTO reservations (name, phone, dateAndTime, tableNr) VALUES (?, ?, ?, ?)"

def validateDateAndTime(dateAndTime):
    try:
        datetime.strptime(dateAndTime, "%Y-%m-%d %H:%M")
        return True
    except ValueError:
        return False

def validatePhoneNumber(phoneNr):
    return re.match("(^\+[0-9]{2}|^\+[0-9]{2}\(0\)|^\(\+[0-9]{2}\)\(0\)|^00[0-9]{2}|^0)([0-9]{9}$|[0-9\-\s]{10}$)", phoneNr)

def newReservations(customer):
    if customer['name'] and customer['phone'] and customer['date'] and customer['time']:
        dateAndTime = "%s %s" % (customer['date'], customer['time'])

        if not validateDateAndTime(dateAndTime):
            return 3

        if not validatePhoneNumber(customer['phone']):
            return 4

        tableNr = db.single(SQL_TABLES_AVAILABLE, (dateAndTime, dateAndTime, dateAndTime))
        if not tableNr:
            return 2

        if db.query(SQL_NEW_RESERVATION, (customer['name'], customer['phone'], dateAndTime, tableNr)):
            return 0

    return 1;

customer = getJsonData()
response = {"errorCode": newReservations(customer)}
sendData(response)
