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

# producing file with vowel counts
information = open("counts.txt", "w")
# writing the vowel count onto the .txt file
vowels = information.write(f"The total amount of vowels is {counter}")
# opens file to display information 
information = open("counts.txt", "r")
vowels = information.read()
information.close()


