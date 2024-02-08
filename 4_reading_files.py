lyrics = open('sample_files/ShakeItOff.txt', 'r')
# open function opens a file
# r (also default mode) means read

# read 10 characters, including spaces
buffer = lyrics.read(10)
print(buffer)

buffer = lyrics.read(20)
print(buffer)

# readline method reads whole line
lyric_line = lyrics.readline()
print(lyric_line)

next_line = lyrics.readline()
print(next_line)

# use loops
# read next 5 lines
for line in range(5):
    next_line = lyrics.readline()
    # print(line, next_line, end='')
    # use -1 to remove line separator
    print(line, next_line[:-1])

print("#" * 25, "SLURPING 1 ", "#" * 25)
# slurping 1
# lines = open('brian.txt').read()
# .read() reads entire file
# so whole song is in song variable
song = open('sample_files/ShakeItOff.txt', 'r').read()
print(f"Whole song:\n{song}")

# slurping 2
# lines= open('brian.txt').read().splitlines()
# .splitlines() returns a list of strings
print("#" * 25, "SLURPING 2 ", "#" * 25)
song_as_list = open('sample_files/ShakeItOff.txt', 'r').read().splitlines()
print(f"Whole song:\n{song_as_list}")

# slurping 3
print("#" * 25, "SLURPING 3 ", "#" * 25)
# linelist = open('brian.txt').readlines()
# includes \n end of line markers
song_as_list = open('sample_files/ShakeItOff.txt', 'r').readlines()
print(f"Whole song:\n{song_as_list}")


# best approach
print("#" * 25, "BEST APPROACH ", "#" * 25)
# uses the file object iterator

for line in open('sample_files/ShakeItOff.txt', 'r'):
    print(line[:-1])
