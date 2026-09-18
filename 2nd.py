


while True:
    Noun = input("Enter a noun:")
    Adjective = input("Enter an adjective:") 
    Verb_ing = input("Enter a verb ending in -ing:")
    sentence = f"Today I went to the zoo with my {Adjective} friend,and we saw a {Noun} {Verb_ing} in its cage."
    print (sentence)
    
    again = input("Do you want to play again? (yes/no): ")
    if again.lower() != "yes" and again.lower() != "y":
        break