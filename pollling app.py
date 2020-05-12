issue=input("What is the yes or no issue you will be voting on today:\nShould soda be banned for young children?")
no_of_voters=int(input("What is the number of voters you will allow on the issue:"))
password=input("Enter a password for polling results:")

yes_count=0
no_count=0
poll_results={}

for i in range(no_of_voters):
    name=input("Enter the namae:")
    if name in poll_results.keys():
        print("You already voted")
    else:
        print("Should soda be banned for young children?")
        choice=input("Enter the choice:(Yes/No)")
        if choice== "yes":
            choice="yes"
            yes_count+=1
        elif choice== "no" or "n":
            choice="no"
            no_count+=1
        else:
            print("not allowed")
    poll_results[name]=choice

print("The voters are:")
for key in poll_results.keys():
    print(key)

if yes_count > no_count:
    print("yes wins")
elif no_count > yes_count:
    print("no wins")
else:
    print("tie")