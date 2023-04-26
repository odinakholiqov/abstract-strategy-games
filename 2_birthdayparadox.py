import datetime, random


def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001,1,1)

        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)

    return birthdays


def getMatch(birthdays):
    #checking all birthdays on uniquness
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA

#months names
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

#getting valid input
while True:
    response = input("How many birthdays should I generate? (Max 100)")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break

#generating and displaying the birthdays
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end="")
    monthName = MONTHS[birthday.month - 1]
    print(f"{monthName} {birthday.day}", end="")


#checking for match(s)
match = getMatch(birthdays)

print()
print()

#displaying the results
if match is not None:
    monthName = MONTHS[match.month - 1]
    dateText = "{} {}".format(monthName, match.day)
    print(f"Multiple people have a birthday on {dateText}")
else:
    print("There is no matching birthdays")

#Running this experiment for 100 000 simulations
simMatch = 0
for i in range(100000):
    #reporting the progress
    if i % 1000 == 0:
        print(i, "simulations run... ")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) is not None:
        simMatch += 1

#displaying the results of the experiment
probability = round(simMatch / 100000 * 100, 2)
print("Out of 100,000 simulations of", numBDays, "people, there was a")
print("matching birthday in that group", simMatch, "times. This means")
print("that", numBDays, "people have a ", probability, "% chance of")
print("having a matching birthday in their group.")
