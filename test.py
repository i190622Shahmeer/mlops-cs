# import pytest
from main import MLOps

mlopsObj = MLOps(5)

def test_getTotalStudents():
    assert mlopsObj.getTotalStudents() == 5

def test_AddStudents():
    mlopsObj.AddStudents()
    assert mlopsObj.getTotalStudents() == 6    

def test_removeStudents():
    mlopsObj.removeStudents()
    assert mlopsObj.getTotalStudents() == 5

def test_getClassName():
    assert mlopsObj.getClassName() == 'Machine Learning Operations (CS-B)'



    
