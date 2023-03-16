# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# opening the file mbox-short.txt
opene = open('mbox-short.txt')
lst = []
# empty list lst to store sorted hours
# empty diction to assist us in counting number of occurences of each hour
counts = dict()


# For every line that starts with 'FROM '.
# Split that line and keep the fifth item (time section).
# Split those time variables at the colons and get the first item only( hours ).
# Using the empty dictionary register the hours as keys and count occurences of each hour, for
# the values assign the count of the hours
for line in opene:
    if line.startswith('From '):
        words = line.split()[5]
        hour = words.split(':')[0]
        counts[hour] = counts.get(hour, 0) + 1

# sort the counts dictionary and append the new items to lst (empty list)
lst = sorted([(k, v) for k, v in counts.items()])

# loop thorugh all these members of the list and print them in key, value fashion

for k, v in lst:
    print(k, v)
