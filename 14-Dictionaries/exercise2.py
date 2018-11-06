artist = {
    "first": "Neil",
    "last": "Young",
}

# concat first and last name with a space

full_name = artist["first"] + " " + artist["last"]
print (full_name)

full_name2 = f"{artist['first']} {artist['last']}"
print (full_name2) 