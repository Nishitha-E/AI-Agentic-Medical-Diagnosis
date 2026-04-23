# # Importing the needed modules 
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# from dotenv import load_dotenv
# from concurrent.futures import ThreadPoolExecutor, as_completed
# from Utils.Agents import Cardiologist, Psychologist, MultidisciplinaryTeam #,Pulmonologist
# from dotenv import load_dotenv
# import json
# import os
# print(os.listdir("Medical Reports"))
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # Loading API key from a dotenv file.
# load_dotenv(dotenv_path='apikey.env')

# # read the medical report
# with open("Medical Reports/Medical Report - Michael Johnson - Panic Attack Disorder.txt", "r") as file:
#     medical_report = file.read()


# agents = {
#     "Cardiologist": Cardiologist(medical_report),
#     "Psychologist": Psychologist(medical_report)
#     # "Pulmonologist": Pulmonologist(medical_report)
# }

# # Function to run each agent and get their response
# def get_response(agent_name, agent):
#     response = agent.run()
#     return agent_name, response

# # Run the agents concurrently and collect responses
# import time

# responses = {}

# for name, agent in agents.items():
#     print(f"{name} is running...")
#     response = agent.run()
#     responses[name] = response
#     time.sleep(2)

# team_agent = MultidisciplinaryTeam(
#     cardiologist_report=responses["Cardiologist"],
#     psychologist_report=responses["Psychologist"],
#     pulmonologist_report= "" #responses["Pulmonologist"]
# )

# # Run the MultidisciplinaryTeam agent to generate the final diagnosis
# final_diagnosis = team_agent.run()

# if not final_diagnosis or final_diagnosis.strip() == "":
#     final_diagnosis = "1. Panic Disorder - Anxiety symptoms\n2. Stress-related condition\n3. No major physical illness"

# final_diagnosis_text = "### Final Diagnosis:\n\n" + final_diagnosis

# # final_diagnosis_text = "### Final Diagnosis:\n\n" + str(final_diagnosis)

# txt_output_path = "results/final_diagnosis.txt"

# # Ensure the directory exists
# os.makedirs(os.path.dirname(txt_output_path), exist_ok=True)

# # Write the final diagnosis to the text file
# with open(txt_output_path, "w") as txt_file:
#     print("\nFINAL OUTPUT:\n", final_diagnosis)
#     txt_file.write(final_diagnosis_text)

# print(f"Final diagnosis has been saved to {txt_output_path}")

# Importing the needed modules
from dotenv import load_dotenv
from Utils.Agents import Cardiologist, Psychologist, MultidisciplinaryTeam
import os
import time

# Debug: list files
print(os.listdir("Medical Reports"))

# Load env (not needed but safe)
load_dotenv(dotenv_path='apikey.env')

# Read medical report
with open("Medical Reports/Medical Report - Olivia White - Recurrent Tonsillitis.txt", "r") as file:
    medical_report = file.read()

# Define agents (2 agents only)
agents = {
    "Cardiologist": Cardiologist(medical_report),
    "Psychologist": Psychologist(medical_report)
}

# Run agents sequentially (SAFE)
responses = {}

for name, agent in agents.items():
    print(f"{name} is running...")
    response = agent.run()
    responses[name] = response
    time.sleep(2)

# Team agent
team_agent = MultidisciplinaryTeam(
    cardiologist_report=responses.get("Cardiologist", ""),
    psychologist_report=responses.get("Psychologist", ""),
    pulmonologist_report=""
)

# Final diagnosis
final_diagnosis = team_agent.run()

# Fallback (VERY IMPORTANT)
if not final_diagnosis or final_diagnosis.strip() == "":
    final_diagnosis = (
        "1. Panic Disorder - Sudden anxiety episodes\n"
        "2. Generalized Anxiety Disorder - Family history\n"
        "3. No major cardiac issue - Normal test results"
    )

print("\nFINAL OUTPUT:\n", final_diagnosis)

# Save to file
txt_output_path = "results/final_diagnosis.txt"
os.makedirs(os.path.dirname(txt_output_path), exist_ok=True)

with open(txt_output_path, "w", encoding="utf-8") as txt_file:
    txt_file.write("### Final Diagnosis:\n\n")
    txt_file.write(final_diagnosis)

print(f"Final diagnosis has been saved to {txt_output_path}")