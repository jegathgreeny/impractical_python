"""Generate funny names by randomly combining names from two separate lists."""

import random
import sys

# This program has a pylint score of 10.0.0/10.
# This is a reference to how code should be constructed.

print("\nWelcome to the Psych 'Sidekick Name Picker.'")
print("A name just like Sean would pick for Gus:")


first = (
    "Baby Oil",
    "Bad News",
    "Big Burps",
    "Bill 'Beenie-Weenie'",
    "Bob 'Stinkbug'",
    "Bowel Noises",
    "Boxelder",
    "Bud 'Lite'",
    "Butterbean",
    "Buttermilk",
    "Buttocks",
    "Chad",
    "Chesterfield",
    "Chewy",
    "Chigger",
    "Cinnabuns",
    "Cleet",
    "Cornbread",
    "Crab Meat",
    "Crapps",
    "Dark Skies",
    "Dennis Clawhammer",
    "Dicman",
    "Elphonso",
    "Fancypants",
    "Figgs",
    "Foncy",
    "Gootsy",
    "Greasy Jim",
    "Huckleberry",
    "Huggy",
    "Ignatious",
    "Jimbo",
    "Joe 'Pottin Soil'",
    "Johnny",
    "Lemongrass",
    "Lil Debil",
    "Longbranch",
    '"Lunch Money"',
    "Mergatroid",
    '"Mr Peabody"',
    "Oil can",
    "Oinks",
    "Old scratch",
    "Ovaltine",
    "Pennywhistle",
    "Pictchfork Ben",
    "Potato Bug",
    "Pushmeet",
    "Rock candy",
    "Schlomo",
    "Scratchensniff",
    "Scut",
    "Sid 'The Squirts'",
    "Skidmark",
    "Slaps",
    "Snakes",
    "Snoobs",
    "Snorki",
    "Soupcan Sam",
    "Spitzitout",
    "Squids",
    "Stinky",
    "Storyboard",
    "Sweet Tea",
    "TeeTee",
    "Wheezy Joe",
    "Winston 'Jazz Hands'",
    "Worms",
)

last = (
    "Appleyard",
    "Bigmeat",
    "Bloominshine",
    "Boogerbottom",
    "Breedslovetrout",
    "Butterbaugh",
    "Clovenhoof",
    "Clutterbuck",
    "Cocktoasten",
    "Endicott",
    "Fewhairs",
    "Gooberdapple",
    "Goodensmith",
    "Goodpasture",
    "Guster",
    "Henderson",
    "Hooperbag",
    "Hoosenater",
    "Hootkins",
    "Jefferson",
    "Jenkins",
    "Jingley-Schmidt",
    "Johnson",
    "Kingfish",
    "Listenbee",
    "m'Bembo",
    "McFadden",
    "Moonshine",
    "Nettles",
    "Noseworthy",
    "Olivetti",
    "Outerbridge",
    "Overpack",
    "Overturf",
    "Oxhandler",
    "Pealike",
    "Pennywhistle",
    "Peterson",
    "Pieplow",
    "Pinkerton",
    "Porkins",
    "Putney",
    "Quakenbush",
    "Rainwater",
    "Rosenthal",
    "Rubbins",
    "Sackrider",
    "Snuggleshine",
    "Splern",
    "Stevens",
    "Stroganoff",
    "Sugar-Gold",
    "Swackhamer",
    "Tippins",
    "Turnipseed",
    "Vinaigrette",
    "Walkingstick",
    "Wallbanger",
    "Weewax",
    "Weiners",
    "Whipkey",
    "Wigglesworth",
    "Wimplesnatch",
    "Winterkorn",
    "Woolysocks",
)

while True:
    first_name = random.choice(first)
    last_name = random.choice(last)

    print("\n")
    print(f"{first_name} {last_name}.", file=sys.stderr)
    print("\n")

    # Enter q to break out of the loop.
    try_again = input("Try again? (Press Enter else q to quit) ")
    if try_again.lower() == "q":
        break