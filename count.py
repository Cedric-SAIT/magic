# Finding and opening the sample.ini file
# Read out the information off of sample.ini file 
sample_ini = open("sample.ini")
information = sample_ini.read()

# counting the vowels within sample.ini file
counter = 0
for vowels in information:
    # list of the vowels
    if vowels in ["a","e","i","o","u","y"]:
        counter += 1 
