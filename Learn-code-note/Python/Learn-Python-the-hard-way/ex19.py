def checese_and_crackers(cheeese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheeese_count
    print "You have %d boxes of cracksers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
checese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_carackers = 50

checese_and_crackers(amount_of_cheese, amount_of_carackers)


print "We can even do math inside too:"
checese_and_crackers(1 + 1, 2 + 2)

print "And we can combine the two, variables and math:"
checese_and_crackers(amount_of_cheese + 11, amount_of_carackers + 100)
