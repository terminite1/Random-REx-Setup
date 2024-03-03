import random
import time

enable_limited_gears = False

pickaxelist = [
    # w1
    "Default",
    "Poly Pickaxe",
    "Steel Sickle",
    "Miner's Mallet",
    "Stone Ravager",
    "Big Slammer",
    "Darkstone Pick",
    "Crystallized Pickaxe",
    "Trinity Claymore",
    "57 Leaf Clover",
    # sw1
    "Legacy Trinity Claymore",
    "Nostalgic Axe",
    "NilAxe",
    # w2
    "Permafrost Pick",
    "Poison Pick",
    "Electraver",
    "Dimensional Scythe",
    "Celestial Smasher",
    "Moon Scepter",
    "Soul Scythe",
    "Prism of Chaos"
]

offgearlist = [
    # w1
    "Core Frag",
    "Blazuine Molotov",
    "Accretium Fireball",
    "Temporum Timebomb",
    "Neptunium Nuke",
    "Combustal Clusterbomb",
    "Erodimium Bomb",
    "Suncindium Flashbang",
    "Luminatite Lantern",
    "Polarium Tunneller",
    "The Inktorb",
    # w2
    "Matterbomb",
    "Shattering Heart",
    "Spiral Striker",
    "T1 Terraformer",
    "Coronal Carpetbomb",
    "Cube Collector",
    "Obliveracy Obliterator",
    "Subspace Tripmine",
]
maingearlist = [
    "Flashlight",
    "Jump Coil",
    "Speed Coil",
    "Thundarian Coil",
    "Acceleratium Coil",
    "Candilium Candle",
    "Elementonic",
    # w2
    "Vitriol Vigor",
]

limitedmain = [
    "Frost Coil",
    "Winged Coil"
]

limitedoff = [
    "Tip Jar",
    "Coal Smokebomb",
    "Metamorphosis Hourglass",
    "Phantasm Lantern",
    "Heartbreaker",
    "Freeze Frag"
]

if enable_limited_gears:
    print("Limited time items enabled")
    pickaxelist.append("Christmas Crusher")
    maingearlist += limitedmain
    offgearlist += limitedoff

print(f"Picking from {len(pickaxelist) - 1} pickaxes, {len(offgearlist) - 1} offhand gears, and {len(maingearlist)} main hand gears\n")

def main():
    randompick = random.choice(pickaxelist)
    randomoff = random.choice(offgearlist)
    randommain = random.choice(maingearlist)

    print("Your random pickaxe is:")
    print(randompick,"\n")
    time.sleep(1)
    print("Your random offhand is:")
    print(randomoff,"\n")
    time.sleep(1)
    print("Your random mainhand is:")
    print(randommain, "\n")
    input("Press Enter to pick again...")
    main()

main()
