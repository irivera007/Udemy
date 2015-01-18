
class Payroll():
    def __init__(self,name,rate,hours):
        self.name=name
        self.rate=rate
        self.hours=hours
        self.wage=rate*hours
        print "Name: " +name
        print "Salary: " + str(self.wage)
    
    def overtime(self,ohours):
        self.ohours=ohours
        otime=ohours*1.5
        total=otime*self.rate+self.wage
        print "Overtime hours: " +str(otime)
        print "Total + overtime: " +str(total)

Employee = Payroll("Arthur",14.20,4.2)

Employee.overtime(1)
