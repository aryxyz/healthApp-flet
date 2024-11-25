


def calculateBMI(weight,height):
    return round(int(weight) / ((int(height)/100)**2),1)


def calculateBMR(weight,height,gender,age):
    weight = int(weight)
    height = int(height)
    age = int(age)
    if gender == "male":
        return round(888.362+(13.397 * weight)+(4.799 * height)-(5.677*age))
    else:
        return round(447.593+(9.247*weight)+(3.098*height)-(4.330*age))