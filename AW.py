def bmi_func(h, w):
    m = h/100
    bmi = w/(m**2)
    print("Your Body mass index is:- %0.2f" % bmi)
    pr = 0
    if bmi < 16:
        pr = "Health Status :- Severe Thinness"
    elif 16 <= bmi < 17:
        pr = "Health Status :- Moderate Thinness"
    elif 17 <= bmi < 18.5:
        pr = "Health Status :- Mild Thinness"
    elif 18.5 <= bmi < 25:
        pr = "Health Status :- Normal"
    elif 25 <= bmi < 30:
        pr = "Health Status :- OverWeight"
    elif 30 <= bmi < 35:
        pr = "Health Status :-Obese class 1"
    elif 35 <= bmi < 40:
        pr = "Health Status :- Obese class 2"
    elif bmi > 40:
        pr = "Health Status :- Obese class 3"
    print(pr)
    a = bmi
    return a


def ft_to_cm(ft):
    return ft*30.48


def body_fat(p, q, r):
    # if q>21 and r == 1:
    #     BFP = 1.20 * p + 0.23 * q - 16.2
    # # elif q < 21 and r == 1:
    # #     BFP = 1.51 * p - 0.70 * q - 2.2
    # elif q > 21 and r == 2:
    #     BFP = 1.20 * p + 0.23 * q - 5.4
    # # elif q < 21 and r == 2:
    # #     BFP = 1.51 * p - 0.70 * q + 1.4

    bfp = -44.988 + (0.503 * q) + (10.689 * r) + (3.172 * p) - (0.026 * p**2) + (0.181 * p * r) - (
                0.02 * p * q) - (0.005 * p**2 * r) + (0.00021 * p**2 * q)
    print("Your Body Fat Percentage is:-", round(bfp, 2))

    return bfp


def calorie(i, j, k, p, gen):
    cal = 0
    if gen == 0:
        cal = (10 * j + 6.25 * k - 5 * i + 5)
    elif gen == 1:
        cal = (10 * j + 6.25 * k - 5 * i - 161)

    if p == 1:
        cal = cal*1.2
    elif p == 2:
        cal = cal*1.4
    elif p == 3:
        cal = cal*1.6
    elif p == 4:
        cal = cal*1.75
    elif p == 5:
        cal = cal*2
    elif p == 6:
        cal = cal * 2.3
    print("To maintain your present weight your calorie intake should be:- ", round(cal, 2))
    return cal


def ideal_w(h):
    mini = 18.5 * (h**2)/10000
    maxi = 24.9 * (h**2)/10000
    print("Your minimum weight should be", round(mini))
    print("Your maximum weight should be", round(maxi))
    return maxi


def main():
    hi = float(input("Enter your height in feet:- "))
    wi = float(input("Enter your weight in kilogram:- "))
    age = int(input("Enter your age:- "))
    gen = int(input("Gender:- (0) Male (1) Female "))
    print("Physical Activity:- \n(1)Sedentary lifestyle (little or no exercise)\n (2)Slightly active lifestyle (light exercise or sports 1-2 days/week)\n (3)Moderately active lifestyle (moderate exercise or sports 2-3 days/week) \n(4)Very active lifestyle (hard exercise or sports 4-5 days/week)\n (5)Extra active lifestyle (very hard exercise, physical job or sports 6-7 days/week)\n(6)Professional athlete ")
    pa = int(input())
    x = bmi_func(ft_to_cm(hi), wi)
    y = body_fat(x, age, gen)
    z = calorie(age, wi, ft_to_cm(hi), pa, gen)
    w = ideal_w(ft_to_cm(hi))


if __name__ == "__main__":
    main()
