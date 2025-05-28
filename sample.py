import re

def find_ssn(text):
    # Define the pattern for a valid SSN
    ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
    
    # Find all SSNs in the input text
    ssns = re.findall(ssn_pattern, text)
    
    return ssns
    

def extract_emails(text):
    # Define the regular expression pattern for emails
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    
    # Find all matches in the input text
    emails = re.findall(email_pattern, text)
    all_emails = text2
    
    return emails




# Example usage
input_text = "John's SSN is 123-45-6789 and Jane's SSN is 987-65-4321."
ssns = find_ssn(input_text)

if ssns:
    print("SSNs found:", ssns)
else:
    print("No SSNs found.")


