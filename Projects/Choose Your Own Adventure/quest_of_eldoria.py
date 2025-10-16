# Colors
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[34m"
MAGENTA = "\033[95m"
PURPLE = "\033[38;5;55m"
BLACK = "\033[30m"
BROWN = "\033[33m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Location Colors
LOC_ELDORIA = BLUE + BOLD + "Eldoria" + RESET
LOC_FOREST = GREEN + BOLD + "Forest of Eldoria" + RESET
LOC_VILLAGE = PURPLE + BOLD + "Village of Windrest" + RESET
LOC_MOUNTAINS = MAGENTA + BOLD + "Eldor Mountains" + RESET
LOC_TOWER = RED + BOLD + "Shadow Tower" + RESET
ITEM_KEY = BROWN + BOLD + "Sacred Key" + RESET
ITEM_HEART = RED + BOLD + "Heart of Eldoria" + RESET
NPC_ELDER = PURPLE + BOLD + "Elder of Windrest" + RESET


# Title Screen
print(f"""{BROWN}
         __...--~~~~~-._   _.-~~~~~--...__
       //               `V'               \\
      //                 |                 \\
     //__...--~~~~~~-._  |  _.-~~~~~~--...__\\
    //__.....----~~~~._\\ | /_.~~~~----.....__\\
               {BLACK}THE HERO OF ELDORIA
{RESET}""")


print(BOLD + BLUE + "\n=== THE QUEST OF ELDORIA ===" + RESET)
print(f"You awaken on a stone altar deep within the {LOC_FOREST}.")
print("Your head throbs, and faint symbols glow on your arm. You remember only your name... and a sense of purpose.\n")

print(BLACK + BOLD + "What will you do?" + RESET)
print("1. Look around")
print("2. Walk down the forest path")
print("3. Call out for help")

choice1 = input("Enter your choice: ")

if choice1 == "1":
    print("\nYou look around and find a dusty satchel beside the altar.")
    print("Inside is a small dagger and a torn map marking a village to the east.")
    print("You decide to head toward the village.")
    location = "village"

elif choice1 == "2":
    print("\nYou walk down the forest path. The trees whisper, almost as if alive.")
    print("After some time, you reach a fork in the road.")
    print("1. Take the left path toward faint lights.")
    print("2. Take the right path toward the sound of running water.")
    choice2 = input("Enter your choice: ")

    if choice2 == "1":
        print(f"\nYou head toward the lights and find a small village — the {LOC_VILLAGE}. The air smells of woodsmoke and bread.")
        location = "village"
    else:
        print("\nYou follow the sound of water and discover an ancient river shrine.")
        print("A spirit appears and offers you a choice.")
        print("1. Accept the blessing of water.")
        print("2. Refuse and move on.")
        choice3 = input("Enter your choice: ")
        if choice3 == "1":
            print(GREEN + "\nThe spirit touches your forehead. You feel stronger." + RESET)
            print(f"You leave, eventually finding your way to the {LOC_VILLAGE}.")
            location = "village"
        else:
            print(f"\nYou leave the shrine. After hours of walking, you collapse and wake up in the {LOC_VILLAGE}.")
            location = "village"

else:
    print("\nYour voice echoes through the trees. A figure appears — a hooded traveler.")
    print("They offer to guide you to a nearby village.")
    print(f"You follow them silently until you reach the gates of the {LOC_VILLAGE}.")
    location = "village"

# --- Village Scene ---
print(BOLD + f"\n=== The {LOC_VILLAGE} ===" + RESET)
print(f"You arrive at {LOC_VILLAGE}, a quiet town under the shadow of the {LOC_MOUNTAINS}.")
print("A guard stops you at the gate.")
print("Guard: 'Traveler, the kingdom is in danger. Are you friend or foe?'")
print("1. 'I'm just passing through.'")
print("2. 'I'm here to help.'")
print("3. Stay silent.")

choice4 = input("Enter your choice: ")

if choice4 == "1":
    print("\nThe guard eyes you suspiciously but lets you in.")
    trust = 1
elif choice4 == "2":
    print(GREEN + "\nThe guard nods solemnly. 'Then you must see the Elder. He will know your purpose.'" + RESET)
    trust = 3
else:
    print("\nThe guard frowns. 'Strange one... be careful.' You enter under watchful eyes.")
    trust = 0

print("\nInside the village, you find three main places to visit.")
print("1. The Tavern")
print("2. The Market")
print(f"3. The Hall of the {NPC_ELDER}")

choice5 = input("Enter your choice: ")

if choice5 == "1":
    print("\nYou enter the tavern. The smell of stew fills the air.")
    print(f"A bard sings of an ancient relic — the {ITEM_HEART} — hidden in the {LOC_MOUNTAINS}.")
    print("A man at the corner offers to sell you a map for 10 gold (you only have 5).")
    print("1. Try to bargain.")
    print("2. Leave.")
    choice6 = input("Enter your choice: ")
    if choice6 == "1":
        print(GREEN + "\nYou offer him your dagger instead. He grins and accepts. You now have the map to the mountains." + RESET)
        has_map = True
    else:
        print("\nYou leave the tavern empty-handed.")
        has_map = False
    has_potion = False

elif choice5 == "2":
    print("\nAt the market, you browse wares and hear gossip about a dark tower awakening beyond the hills.")
    print("A merchant gives you a strange riddle to earn a healing potion:")
    print(MAGENTA + "'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'" + RESET)
    answer = input("Your answer: ").lower()
    if "echo" in answer:
        print(GREEN + "\nThe merchant smiles. 'Correct!' He hands you a healing potion." + RESET)
        has_potion = True
    else:
        print(RED + "\nThe merchant shakes his head. 'Wrong... but brave of you to try.'" + RESET)
        has_potion = False
    has_map = False

else:
    print(f"\nYou enter the Elder’s Hall. The {NPC_ELDER} gazes into your glowing arm.")
    print(f"'Ah... you bear the Mark of Light. You were chosen to seal the {LOC_TOWER}.'")
    print(f"He gives you a {ITEM_KEY} and tells you to head into the {LOC_MOUNTAINS}.")
    has_map = True
    has_potion = True
    trust += 2

# --- Mountain Path ---
print(BOLD + f"\n=== Journey to the {LOC_MOUNTAINS} ===" + RESET)
print("You follow a winding trail up the snowy peaks.")
print("Night falls, and a storm brews. You spot a cave nearby.")
print("1. Enter the cave for shelter.")
print("2. Keep walking through the storm.")

choice7 = input("Enter your choice: ")

if choice7 == "1":
    print("\nInside the cave, you find ancient carvings glowing faintly.")
    print("You rest for the night, feeling the warmth of unseen fire.")
    print("When you wake, a hidden passage leads deeper underground.")
    cave = True
else:
    print("\nYou trudge through the storm and collapse from exhaustion.")
    print(f"When you awaken, you're at the base of the {LOC_TOWER}.")
    cave = False

# --- Final Area ---
print(BOLD + f"\n=== The {LOC_TOWER} ===" + RESET)
print("The air grows cold. Shadows swirl around the ancient tower of Eldoria.")
print("1. Enter bravely.")
print("2. Try to sneak in.")
print("3. Turn back.")

choice8 = input("Enter your choice: ")

if choice8 == "1":
    print("\nYou push the doors open and step inside. A voice echoes through the chamber:")
    print(MAGENTA + "'Only those of true light may pass. Answer this, and the path shall open:'" + RESET)
    print("'What walks on four legs in the morning, two at noon, and three in the evening?'")
    riddle2 = input("Your answer: ").lower()
    if "man" in riddle2 or "human" in riddle2:
        print(GREEN + "\nThe tower trembles. The shadows fade. Light floods the halls." + RESET)
        print(f"You ascend to the top and seal the darkness forever. The realm of {LOC_ELDORIA} is saved!")
        print(BOLD + BLUE + "Congratulations, hero — you have restored the light!" + RESET)
    else:
        print(RED + "\nThe voice roars: 'You are not worthy!' The shadows consume you. Game Over." + RESET)

elif choice8 == "2":
    print("\nYou sneak in quietly but step on a pressure plate. Arrows fly from the walls!")
    if has_potion:
        print(GREEN + "You drink your potion and survive the ambush, escaping through a side passage." + RESET)
        print("You emerge in daylight, vowing to return stronger. You survived, but the darkness remains...")
    else:
        print(RED + "You fall to the ground as the trap is triggered. Game Over." + RESET)
else:
    print("\nYou turn back, knowing some battles are not yet yours to fight.")
    print(f"Perhaps one day, your courage will bring light to {LOC_ELDORIA}...")

print("\nThanks for playing " + BOLD + BLUE + "The Quest of Eldoria!" + RESET)


