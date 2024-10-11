class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        tMins = self.tMins() + other.tMins()
        return Time(tMins // 60, tMins % 60)
    def tMins(self):
        return self.hours * 60 + self.minutes
    def displayTime(self):
        print(str(self.hours)+" hours and "+str(self.minutes)+" minutes")
    def displayMinute(self):
        print(str(self.hours * 60 + self.minutes)+" minutes")


time1 = Time(2, 50)
time2 = Time(1, 20)

result = time1.addTime(time2)

# Display results
print("Time 1:")
time1.displayTime()
print("Time 2:")
time2.displayTime()
print("Result:")
result.displayTime()
print("Total minutes in result:")
result.displayMinute()