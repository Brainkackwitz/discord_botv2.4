import json  # for json parsing


# Open the json file with the role settings and pars it with JSON.
with open("settings.json") as f:
    settings = json.load(f)


# Save json properties into variables for better handling.
lvl1 = settings["perms"]["lvl1"]
lvl2 = settings["perms"]["lvl2"]
lvl3 = settings["perms"]["lvl3"]


def get(memb):
    lvl = [0]
    # Tests if the role in roles is existent in one of the role name arrays
    # and adds the level of the role array to the "lvl" integer array.
    # HINT: For better safety, you can set role ID's in JSON and here
    # instead of the role names.
    for r in memb.roles:
        if r.name in lvl3:
            lvl.append(3)
        elif r.name in lvl2:
            lvl.append(2)
        elif r.name in lvl1:
            lvl.append(1)
    print(lvl, max(lvl))
    # Returns the maximum level in "lvl" array
    # EXP: '[0, 1, 1, 2, 1]' -> returns '2'
    return max(lvl)

# Checks in the max role level is bigger than the required level
def check(memb, lvl):
    return get(memb) >= lvl