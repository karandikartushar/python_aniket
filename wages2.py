def calcWeeklyWages(totalHours, hourlyWage):
    if totalHours <= 40:
        totalWages = hourlyWage*totalHours
    elif totalHours <= 60:
        overtime = totalHours-40
        totalWages = 1.5*hourlyWage*overtime+hourlyWage*40
    else:
        overtime = totalHours-60
        totalWages = 2*overtime*hourlyWage+1.5*hourlyWage*20+hourlyWage*40
        return totalWages

def main():
    hours = float(input('Enter hours worked in 1 week: '))
    wage = float(input('Enter dollars paid per hour: '))
    total = calcWeeklyWages(hours, wage)
    print('Wages for {hours} hours at ${wage} per hour are ${total}.'.format(**locals()))
main()

