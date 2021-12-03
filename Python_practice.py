# # algorithm that calculates the percentage of votes a candidate receives in an election, you might write a simple algorithm like this:
# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")



# #using if statemnts on our counties list to determine if the second county in the list is Denver. If so, then we will print "Denver" to the screen.
# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])


# #testing If-Else statements
# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")



#nested if-else statements
# #What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')


#compound statement
# # What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')



#Membership Operators
# if "Arapahoe" in counties: 
#   print("True") 
# else: 
#   print("False")

# # counties = ["Arapahoe","Denver","Jefferson"] 
# # if "El Paso" not in counties: 
# #   print("True") 
# # else: 
# #   print("False")



# # #Logical Operator (and, or, not)
# # if "Arapahoe" in counties and "El Paso" not in counties:
# #    print("Only Arapahoe is in the list of counties.")
# # else:
# #     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")




# # #Iterating through lists
# # counties = ["Arapahoe","Denver","Jefferson"] 
# # for county in counties:
# #     print(county)



 

# # for i in len(counties_tuples):

# #       print(counties_tuples[i])

# # counties_tuple = ("Arapahoe","Denver","Jefferson")
# # for i in range(len(counties_tuple)):
# #        print(counties_tuples[i])






# #To get the keys
# # for county in counties_dict.keys():
# #     print(county)

# # #To get the values
# # for voters in counties_dict.values():
# #     print(voters)

# #To get key and value
# # for key, value in dictionary_name.items():
# #     print(key, value)

# # other method

# for county, voters in counties_dict.items():
#     print(county, voters)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():
#     print(county, " county has ", voters, " registered voters") 

