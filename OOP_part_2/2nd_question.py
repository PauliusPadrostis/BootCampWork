"""
Create a program that would:
* have a class "Worker".
* Worker class would have parameters: name, hourly_rate, employed_since.
* Would have a method that would calculate how many days has the worker worked since the date entered until today
(considering that the worker works 7 days / week).
* Would have a method that would calculate how much has the worker earned since employment (using the method above)
(considering that the worker works 8 hours / day).
* Would have a class "NormalWorker" which would change the Worker class so that it would calculate the salary differently.
(considering that the normal worker works only 5 days / week).
"""

import datetime


class Worker:
    def __init__(self, name, hourly, started):
        self.name = name
        self.hourly = hourly
        self.started = started

    def days_worked(self):
        dtstarted = datetime.datetime.strptime(self.started, "%Y-%m-%d")
        days_worked = datetime.datetime.today() - dtstarted
        return days_worked.days

    def calc_salary(self):
        return self.hourly * 8 * self.days_worked()


class NormalWorker(Worker):
    def days_worked(self):
        dtstarted = datetime.datetime.strptime(self.started, "%Y-%m-%d")
        days_worked = datetime.datetime.today() - dtstarted
        return days_worked.days - (days_worked.days * 28 // 100)


worker1 = Worker("Matt", 12, "2023-2-12")
worker2 = Worker("Josh", 15, "2010-1-1")
worker3 = NormalWorker("Laura", 15, "2010-1-1")

print(worker1.days_worked())
print(worker2.days_worked())
print(worker3.days_worked())
print("\n")
print(worker1.calc_salary())
print(worker2.calc_salary())
print(worker3.calc_salary())