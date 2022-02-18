#Today I went to the zoo. I saw a(n)
#___________(adjective)
#_____________(Noun) jumping up and down in its tree.
#He _____________(verb, past tense) __________(adverb)
#through the large tunnel that led to its _______(adjective)
#__________(noun). I got some peanuts and passed
#them through the cage to a gigantic gray _______(noun)
#towering above my head. Feeding that animal made
#me hungry. I went to get a __________(adjective) scoop
#of ice cream. It filled my stomach. Afterwards I had to
#__________(verb) __________ (adverb) to catch our bus.
#When I got home I __________(verb, past tense) my
#mom for a __________(adjective) day at the zoo.
adj1 = input("Enter an adjective! ")
noun1 = input("Enter a noun! ")
verb1 = input("Enter a past tense verb! ")
adverb1 = input("Enter an Adverb! ")
adj2 = input("Enter an adjective! ")
noun2 = input("enter a noun! ")
#adj3 = input("Enter an adjective!")
#adj4 = input("Enter an adjective!")







madlib = ("Today I went to the zoo! I saw a {} {} jumping up and down its tree.".format(adj1, noun1)) +\
("He {} {} through the large tunnel that led to it's {} {}").format(verb1, adverb1, adj2, noun2) \


print(madlib)
