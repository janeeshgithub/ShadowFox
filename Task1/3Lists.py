# Initial Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate the number of members
print("Initial Justice League members count:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("After recruiting Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman the leader:", justice_league)

# 4. Move either Green Lantern or Superman between Aquaman and Flash
justice_league.remove("Green Lantern")  # Removing first to insert at a different position
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")
print("After separating Aquaman and Flash:", justice_league)

# 5. Replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("After forming a new team:", justice_league)

# 6. Sort alphabetically and determine new leader
justice_league.sort()
print("After sorting alphabetically:", justice_league)
print("New leader of Justice League:", justice_league[0])
