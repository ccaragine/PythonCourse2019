import re

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()

otext = ''.join(obama)


## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

re.findall(r"The", otext)
re.findall(r"[^'the']", otext) ## ^ except
re.findall(r'^.*\.$', otext, re.MULTILINE)

re.findall(r"\.^'the'", otext)

for l in obama:
    check_the = re.findall(r'[Tt]he', l)
    if len(check_the)==0:
        print(l) 


# TODO: print lines that contain a word of any length starting with s and ending with e
re.findall(r'\bs\w+e\b', otext)

for l in obama:
    check_se = re.findall(r'\bs\w+e\b', l)
    if len(check_se)!=0:
        print(l) 




## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = r"Please enter a date in the format 09.10.96: "
identify = re.findall(r"\d{2}.\d{2}.\d{2}", date)
"""
Month: \d 
Day: \d 
Year: \d  
""" % identify, identify, identify 




