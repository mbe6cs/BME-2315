import csv
import numpy as np
import matplotlib.pyplot as plt
from patient import Patient


patients = []
# here adding the libraries necessary for reading the data and give the final graphs

with open("Metadata and Protein Data for Module 1 (2).csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        new_patient = Patient(
            row["Donor ID"],
            row["Sex"],
            int(row["Age at Death"]),
            row["Cognitive Status"],
            row["APOE Genotype"],
            int(row["Thal"].replace("Thal ", "")),
            float(row["tTAU pg/ug"]),
            float(row["ABeta40 pg/ug"]),
            float(row["ABeta42 pg/ug"]),
            float(row["pTAU pg/ug"])
        )
        # adding individual patients to my list here
        patients.append(new_patient)


# organizes all of the patients by their age
patients.sort(key=lambda p: p.age)
# Here I decided to organize patients based on their age from youngest to oldest
print("Patients must be organized based on their age from youngest to oldest:")
for patient in patients:
    print(patient)


# find and choose patients here
Patient.find_and_select_patients(patients)


# All of this used to make my bar graph
female_values = [p.abeta42 for p in patients if p.sex == "Female"]
male_values = [p.abeta42 for p in patients if p.sex == "Male"]

means = [np.mean(female_values), np.mean(male_values)]
sds = [np.std(female_values), np.std(male_values)]

plt.bar(["Female", "Male"], means, yerr=sds, capsize=7)

plt.xlabel("Sex")
plt.ylabel("ABeta42")
plt.title("ABeta42 for male and female patients")

plt.show()


# This part of the code shows the scatter plot
ages = [p.age for p in patients]
values = [p.abeta42 for p in patients]

plt.scatter(ages, values)

plt.xlabel("Age at Death")
plt.ylabel("ABeta42")
plt.title("Age vs ABeta42")

plt.show()