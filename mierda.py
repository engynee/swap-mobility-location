import logging
LOG_FILENAME = 'tuerestonto.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
b='holaAAA'
a=raw_input()
logging.debug(a)
print 'se ha printado la:' + str(a)
