userstring = input("gimme a number that is greater than 100..."):
usernum = Int(userstring, 10):
if usernum < 100 { // statement for when termination is NOT true, keep loop going...
// "While usernum is less than 100..."
print (usernum + "is less than 100, dummy. Try again, I've got all day...")
userstring = input(usernum + " is less than 100, dummy. Try again, I've got all day...")
usernum = Int(userstring, 10):
print ("Congraulations! " + usernum + "is greater than 100! Great job!")
