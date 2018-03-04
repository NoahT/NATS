#!/usr/local/bin/python3
''' A simple SQL database'''

import sqlite3


__author__ = "Taylor Cochran"
__version__ = "1.0"
__maintainer__ = "Taylor Cochran"
__email__ = "taylorjcochran@hotmail.com"
__status__ = "Prototype"


class Person(object):
  def __init__(self, first, last, ID, address, occupation):
    self.first = first
    self.last = last
    self.id = ID
    self.address = address
    self.occupation = occupation


class DataBase(object):
  def __init__(self, database):
    self.database = sqlite3.connect(database)
    self.cursor = self.database.cursor()

  def add_person(self, person):
    '''Creates an entry in the person_table

    Args:
      person: Should either be a Person object,  
              or a tuple with (first, last, address, occupation)
    '''
    
    if isinstance(person, Person):
      self.cursor.execute('''
        INSERT INTO person_table (first, last, ID, address, occupation)
        VALUES (?, ?, ?, ?, ?)''',
        (
          person.first, person.last, person.id, 
          person.address, person.occupation
         ))

    else:
      first      = person[0]
      second     = person[1]
      ID         = person[2]
      address    = person[3]
      occupation = person[4]

      self.cursor.execute('''
          INSERT INTO person_table (first, last, ID, address, occupation)
          VALUES (?, ?, ?, ?, ?)''',
          (
            first, second, ID, 
            address, occupation 
           ))

    self.database.commit()

  def remove_person(self, person):
    ''' Removes an entry from person_table
    
    Args:
        person: a tuple or object of type person
    '''
    if isinstance(person, Person):
      self.cursor.execute('''
        DELETE FROM person_table WHERE ID=?''',
        (person.id,))
    else:
      ID = person[2]
      self.cursor.execute('''
          DELETE FROM person_table WHERE ID=?''',
          (ID,))
    self.database.commit()

  def get_person(self, ID):
    ''' Returns a tuple containing the data from person_table entry.
    
    Args:
        ID: the person's id number in the database
    '''
    self.cursor.execute('''
      SELECT * FROM person_table WHERE ID=?
      ''', (ID,))
    return self.cursor.fetchone()

  def close_database(self):
    '''Closes the database'''
    self.database.commit()
    self.database.close()


if __name__ == '__main__':
  db = DataBase("Test.db")
  test_person1 = Person("Noah", "Teshima", "00001",
                       "456 Road Street", "Food Remover")
  test_person2 = ("Noah", "Teshima", "00001",
                       "456 Road Street", "Food Remover")
  db.add_person(test_person1)
  value = db.get_person("00001")
  print(value)
  db.remove_person(test_person2)
  value = db.get_person("00001")
  print(value)
  db.close_database()
  


