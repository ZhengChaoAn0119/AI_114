import numpy as np

lin_a = np.array([[100, 115, 95], [50, 215], [120, 100]], dtype=object)
lin_b = np.array([[115, 115], [165, 145, 125], [125]], dtype=object)
lin_c = np.array([[130], [75, 95, 325], [130, 140, 150, 160], [195]], dtype=object)

lionLi = np.array([lin_a, lin_b, lin_c], dtype=object)

Max_salary = lionLi[0][0][0]
Min_salary = lionLi[0][0][0]
Max_lin = Max_family = Max_ps = 0
Min_lin = Min_family = Min_ps = 0

for lin in range(0, len(lionLi)):
    for family in range(0, len(lionLi[lin])):
        for ps in range(0, len(lionLi[lin][family])):
            if lionLi[lin][family][ps] > Max_salary:
                Max_salary = lionLi[lin][family][ps]
                Max_lin = lin
                Max_family = family
                Max_ps = ps

            if lionLi[lin][family][ps] < Min_salary:
                Min_salary = lionLi[lin][family][ps]
                Min_lin = lin
                Min_family = family
                Min_ps = ps


print(
    f"The Max salary: {Max_salary}, happen from {Max_lin} lin, family-{Max_family},person-{Max_ps}"
)
print(
    f"The Min salary: {Min_salary}, happen from {Min_lin} lin, family-{Min_family},person-{Min_ps}"
)
