def C2F():
    c = float(input("Celsius: "))
    f = c * 9 / 5 + 32
    print(f"Celsius: {c:.1f}°C, the Fahrenheit is {f:.1f}°F")


def F2C():
    f = float(input("Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f"Fahrenheit: {f:.1f}°F, the Celsius is {c:.1f}°C")


def Chenge_Temp():
    func = input(
        "If Celsius to Fahrenheit, Please input y.\nIf Fahrenheit to Celsius, Please input n. "
    )
    if func == "y":
        C2F()
    if func == "n":
        F2C()


# Chenge_Temp()

# def BMI_function(kg, meter):
#     BMI = kg / (meter**2)
#     return BMI


# kg = float(input("Please input the kg : "))
# meter = float(input("Please input the meter : "))
# BMI = BMI_function(kg, meter)
# print(f"YOUR Height : {meter}, Weight : {kg}, and BMI : {BMI}")


def BMI_function():
    kg = float(input("Please input your kg : "))
    centimeter = float(input("Please input your centimeter : "))
    BMI = kg / ((centimeter / 100) ** 2)
    print(f"YOUR Height : {centimeter}cm, Weight : {kg}kg, and BMI : {BMI:.1f}")
    pass


BMI_function()
