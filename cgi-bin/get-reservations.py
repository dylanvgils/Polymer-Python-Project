#!/usr/bin/env python
from modules.core.core import *
from modules.database import database as db

SQL_GET_ALL_RESERVATIONS = "SELECT *, CAST(strftime('%s', dateAndTime) AS INTEGER) AS sortDate FROM reservations ORDER BY sortDate"

def getReservations():
    body = []

    for result in db.query(SQL_GET_ALL_RESERVATIONS):
        body.append({"id": result['id'], "name": result['name'], "phone": result['phone'], "dateAndTime": result['dateAndTime'], "tableNr": result['tableNr']})

    return body

sendData(getReservations())
