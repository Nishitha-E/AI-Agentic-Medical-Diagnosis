# import random
# import os

# # Sample data pools
# names = ["Arjun Mehta", "Priya Sharma", "Rahul Verma", "Sneha Reddy", "Kiran Patel"]
# ages = [25, 30, 35, 40, 45]
# genders = ["Male", "Female"]

# symptoms_pool = [
#     "chest pain, palpitations, sweating",
#     "abdominal pain, bloating, irregular bowel movements",
#     "shortness of breath, wheezing",
#     "headache, dizziness, nausea",
#     "fatigue, weakness, loss of appetite"
# ]

# diagnosis_map = {
#     "chest": "Panic Disorder / Cardiac Issue",
#     "abdominal": "IBS / GERD",
#     "breath": "Asthma / COPD",
#     "headache": "Migraine",
#     "fatigue": "General Weakness / Anemia"
# }

# def generate_report():
#     name = random.choice(names)
#     age = random.choice(ages)
#     gender = random.choice(genders)
#     symptoms = random.choice(symptoms_pool)

#     report = f"""
# Medical Case Report
# Name: {name}
# Age: {age}
# Gender: {gender}

# Chief Complaint:
# The patient reports {symptoms} for the past few weeks.

# Medical History:
# No major previous illnesses reported.

# Lifestyle:
# Moderate activity, occasional stress.

# Examination:
# Vitals normal. No major abnormalities detected.
# """

#     return name.replace(" ", "_"), report


# def save_reports(n=5):
#     os.makedirs("Generated_Reports", exist_ok=True)

#     for i in range(n):
#         filename, report = generate_report()
#         filepath = f"Generated_Reports/{filename}_{i}.txt"

#         with open(filepath, "w", encoding="utf-8") as f:
#             f.write(report)

#     print(f"{n} reports generated successfully!")


# if __name__ == "__main__":
#     save_reports(5)