#!/usr/local/bin/python3
''' A simple Helper class'''

import datetime

__author__ = "Taylor Cochran"
__version__ = "1.0"
__maintainer__ = "Taylor Cochran"
__email__ = "taylorjcochran@hotmail.com"
__status__ = "Prototype"


class Helper(object):

  def to_bytes(self, str_or_byte):
    '''Encodes the passed str or bytes into utf-8'''
    if isinstance(str_or_byte, str):
      str_or_byte = str_or_byte.encode('utf-8')
    return str_or_byte

  def to_str(self, str_or_byte):
    '''Decodes the passed str or bytes from utf-8'''
    if isinstance(str_or_byte, bytes):
      str_or_byte = str_or_byte.decode('utf-8')
    return str_or_byte

  def get_date(self):
    ''' Grabs the current date/time stamp'''
    date = str(datetime.datetime.now())
    return date