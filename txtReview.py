# 1) open the txt file, and print the results one line at a time
infile = open("txtFile.txt","r")

for line in infile:
    print(line.rstrip("\n"))

infile.close()


# 2) create a new txt file called "tv.txt" and write the contents of the list to the text file with a header of "Popular 2000's tv shows"
tvList = [
    'Big Bang Theory',
    'The Ellen Show',
    'Family Guy',
    'George Lopez',
    'How I Met Your Mother',
    'The Office',
    'Honey, I Shrunk the Kids: The TV Show',
    'South Park',
    'The Simpsons',
    'Two and a Half Men',
    'Friends',
    'Everybody Hates Chris',
    'Malcolm in the Middle',
    'The Middle',
    'American Dad'
]
outfile = open("tv.txt","w")
outfile.write("Popular 2000's tv shows" + "\n" + "\n")
for line in tvList:
    outfile.write(line + "\n")
outfile.close()

# 3) open the tv.txt file in append mode and add your favorite tv show to the end of the file
afile = open("tv.txt","a")
afile.write("Zack and Cody\n")
afile.close()


