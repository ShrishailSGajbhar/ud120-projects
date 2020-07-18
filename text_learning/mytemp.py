string = "Hi sara, lets go to shackleton"
replaceList = ["sara", "shackleton", "chris", "germani"]


for w in string.split():
    if w in replaceList:
        string = string.replace(w,'')
print string
