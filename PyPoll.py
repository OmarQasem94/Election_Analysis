
import csv
import os

#Assign a variable to load a file from path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to load a file from path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:

    #read and analysze the data
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)


    # for row in file_reader:
    #     print(row)

    #print the file object
    print(election_data)


with open(file_to_save, "w") as txt_file:
    txt_file.write("counties in the Election\n")
    txt_file.write(("-" * 30) + "\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
txt_file.close()


