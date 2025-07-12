## BMI (BODY MASS INDEX)

## FORMULA bmi = weight_kg / (height_m ** 2)

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def get_bmi_catigory(bmi):
    
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("===BMI Calculator==")
    try:
        wight = float(input("Enter Wight: "))
        Hight = float(input("Enter Hight: "))

        bmi = calculate_bmi(wight, Hight)
        catigory = get_bmi_catigory(bmi)
        print(f"youre bmi is: {bmi:.2}")
        print(f"Catigory: {catigory}")
    except ValueError:
        print("Please print valid number")

if __name__ == "__main__":
    main()