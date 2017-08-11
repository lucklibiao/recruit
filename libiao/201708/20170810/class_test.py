#!/usr/bin/python

class student:
  stu_id=0
  def _init_(self,name,salary):
    self.name=name
    self.salary=salary
    stu_id+=1
  def displayCount(self):
    print "Total student %d",student.stu_id
  def displayStudent(self):
    print "Name: ",self.name,"Salay: ",self.salary
