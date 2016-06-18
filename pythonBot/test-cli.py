#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time, sys, pprint, config
from mysql.connector import (connection) 
import msgParse

cnx = connection.MySQLConnection(user=config.MYSQL_USER, password=config.MYSQL_PASSWORD, host= config.MYSQL_HOST, database=config.MYSQL_DB)
inTxt=sys.argv[1]
outTxt= msgParse.answer(inTxt, cnx)
print(inTxt +'\n'+ outTxt)
cnx.close();
