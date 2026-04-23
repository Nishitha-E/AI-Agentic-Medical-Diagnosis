# from langchain_core.prompts import PromptTemplate
# from langchain_ollama import ChatOllama

# class Agent:
#     def __init__(self, medical_report=None, role=None, extra_info=None):
#         self.medical_report = medical_report
#         self.role = role
#         self.extra_info = extra_info
#         # Initialize the prompt based on role and other info
#         self.prompt_template = self.create_prompt_template()
#         # Initialize the model
#         self.model = ChatOllama(model="phi", temperature=0)

#     def create_prompt_template(self):
#         if self.role == "MultidisciplinaryTeam":
#             # templates = f"""
#             #     Act like a multidisciplinary team of healthcare professionals.
#             #     You will receive a medical report of a patient visited by a Cardiologist, Psychologist, and Pulmonologist.
#             #     Task: Review the patient's medical report from the Cardiologist, Psychologist, and Pulmonologist, analyze them and come up with a list of 3 possible health issues of the patient.
#             #     Just return a list of bullet points of 3 possible health issues of the patient and for each issue provide the reason.
                
#             #     Cardiologist Report: {self.extra_info.get('cardiologist_report', '')}
#             #     Psychologist Report: {self.extra_info.get('psychologist_report', '')}
#             #     Pulmonologist Report: {self.extra_info.get('pulmonologist_report', '')}
#             # """
            
#             templates = f"""
#             You are a team of medical experts.

#             Your task is to STRICTLY provide:

#             - Top 3 possible medical conditions
#             - Each in 1-2 lines
#             - Based ONLY on given reports

#             DO NOT:
#             - Add explanations
#             - Add extra stories
#             - Add unrelated content
#             - Ask questions

#             ONLY OUTPUT FORMAT:

#             1. Condition - Reason
#             2. Condition - Reason
#             3. Condition - Reason

#             Cardiologist Report: {self.extra_info.get('cardiologist_report', '')}
#             Psychologist Report: {self.extra_info.get('psychologist_report', '')}
#             """
#         else:
#             templates = {
#                 "Cardiologist": """
#                     Act like a cardiologist. You will receive a medical report of a patient.
#                     Task: Review the patient's cardiac workup, including ECG, blood tests, Holter monitor results, and echocardiogram.
#                     Focus: Determine if there are any subtle signs of cardiac issues that could explain the patient’s symptoms. Rule out any underlying heart conditions, such as arrhythmias or structural abnormalities, that might be missed on routine testing.
#                     Recommendation: Provide guidance on any further cardiac testing or monitoring needed to ensure there are no hidden heart-related concerns. Suggest potential management strategies if a cardiac issue is identified.
#                     Return your answer in clear bullet points.
#                     Always provide at least 3 possible conditions with reasons.
#                     Do not return empty output.
#                     Medical Report: {medical_report}
#                 """,
#                 "Psychologist": """
#                     Act like a psychologist. You will receive a patient's report.
#                     Task: Review the patient's report and provide a psychological assessment.
#                     Focus: Identify any potential mental health issues, such as anxiety, depression, or trauma, that may be affecting the patient's well-being.
#                     Recommendation: Offer guidance on how to address these mental health concerns, including therapy, counseling, or other interventions.
#                     Please only return the possible mental health issues and the recommended next steps.
#                     Patient's Report: {medical_report}
#                 """,
#                 "Pulmonologist": """
#                     Act like a pulmonologist. You will receive a patient's report.
#                     Task: Review the patient's report and provide a pulmonary assessment.
#                     Focus: Identify any potential respiratory issues, such as asthma, COPD, or lung infections, that may be affecting the patient's breathing.
#                     Recommendation: Offer guidance on how to address these respiratory concerns, including pulmonary function tests, imaging studies, or other interventions.
#                     Please only return the possible respiratory issues and the recommended next steps.
#                     Patient's Report: {medical_report}
#                 """
#             }
#             templates = templates[self.role]
#         return PromptTemplate.from_template(templates)
    
#     def run(self):
#         # print(f"{self.role} is running...")
#         prompt = self.prompt_template.format(medical_report=self.medical_report)
#         try:
#             response = self.model.invoke(prompt)
#             # Debug print (IMPORTANT)
#             print(f"\nDEBUG ({self.role}):", response, "\n")

#             # Handle different response formats
#             if hasattr(response, "content") and response.content:
#                 return response.content
#             elif isinstance(response, str):
#                 return response
#             else:
#                 return str(response)

#         except Exception as e:
#             print("Error occurred:", e)
#             return "Error in generating response"


# # Define specialized agent classes
# class Cardiologist(Agent):
#     def __init__(self, medical_report):
#         super().__init__(medical_report, "Cardiologist")

# class Psychologist(Agent):
#     def __init__(self, medical_report):
#         super().__init__(medical_report, "Psychologist")

# class Pulmonologist(Agent):
#     def __init__(self, medical_report):
#         super().__init__(medical_report, "Pulmonologist")

# class MultidisciplinaryTeam(Agent):
#     def __init__(self, cardiologist_report, psychologist_report, pulmonologist_report):
#         extra_info = {
#             "cardiologist_report": cardiologist_report,
#             "psychologist_report": psychologist_report,
#             "pulmonologist_report": pulmonologist_report
#         }
#         super().__init__(role="MultidisciplinaryTeam", extra_info=extra_info)


from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

class Agent:
    def __init__(self, medical_report=None, role=None, extra_info=None):
        self.medical_report = medical_report
        self.role = role
        self.extra_info = extra_info
        self.prompt_template = self.create_prompt_template()
        self.model = ChatOllama(model="phi", temperature=0)

    def create_prompt_template(self):
        if self.role == "MultidisciplinaryTeam":
            templates = f"""
You are a medical expert team.

STRICTLY give only:

1. Condition - Reason
2. Condition - Reason
3. Condition - Reason

Rules:
- Only 3 points
- No extra text
- No explanation paragraphs
- No unrelated content

Cardiologist Report: {self.extra_info.get('cardiologist_report', '')}
Psychologist Report: {self.extra_info.get('psychologist_report', '')}
"""
        else:
            templates = {
                "Cardiologist": """
Act like a cardiologist.

Give:
- 3 possible cardiac-related causes
- Short reasons

STRICT:
- Bullet points only
- No long paragraphs

Medical Report: {medical_report}
""",
                "Psychologist": """
Act like a psychologist.

Give:
- 3 possible mental health conditions
- Short reasons

STRICT:
- Bullet points only
- No extra explanation

Patient Report: {medical_report}
"""
            }
            templates = templates[self.role]

        return PromptTemplate.from_template(templates)

    def run(self):
        prompt = self.prompt_template.format(medical_report=self.medical_report)

        try:
            response = self.model.invoke(prompt)

            # DEBUG (can remove later)
            print(f"\nDEBUG ({self.role}):", response, "\n")

            if hasattr(response, "content") and response.content:
                return response.content.strip()
            elif isinstance(response, str):
                return response.strip()
            else:
                return str(response).strip()

        except Exception as e:
            print("Error occurred:", e)
            return ""

# Agents
class Cardiologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Cardiologist")

class Psychologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Psychologist")

class MultidisciplinaryTeam(Agent):
    def __init__(self, cardiologist_report, psychologist_report, pulmonologist_report):
        extra_info = {
            "cardiologist_report": cardiologist_report,
            "psychologist_report": psychologist_report,
            "pulmonologist_report": pulmonologist_report
        }
        super().__init__(role="MultidisciplinaryTeam", extra_info=extra_info)