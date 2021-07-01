#This code parses email address from a endnote export text file. the code is written in Python 3. Code modified from https://www.tutorialspoint.com/python_text_processing/python_extract_emails_from_text.htm


import re

infile = '/Users/rsn13/Pictures/Desktop/all_proteoform_references.txt'
outfile = '/Users/rsn13/Pictures/Desktop/scripts/output/email_addresses_proteoform.txt'

lines = []
emails = []
with open(infile, encoding='utf8') as fh:
    for line in fh:
        lines.append(line)
    
    for text in lines:
        emails_ids = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
        for i in emails_ids:
            if i not in emails:
                emails.append(i)
            
         
    for email in emails:
        sourceFile = open(outfile, 'a')
        print(email, file=sourceFile)
        sourceFile.close()
         

print('Done')
