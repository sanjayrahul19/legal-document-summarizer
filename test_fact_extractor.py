
from app.fact_extractor import extract_important_facts

sample_text = """
ABC Technologies Pvt. Ltd. agrees to employ Rahul as a Software Engineer
starting from 1 January 2027.

Rahul must follow all company policies.

The employee will receive an annual salary of INR 800,000.

The employee is required to protect confidential company information.

Either party may terminate this agreement by providing 30 days written notice.
"""

facts = extract_important_facts(sample_text)

print("Extracted Facts:")

for category, values in facts.items():

    print(f"\n{category.upper()}:")

    for value in values:
        print("-", value)
