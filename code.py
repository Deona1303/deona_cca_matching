print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

volleyball1 = input("I enjoy exercising.")
TAF1 = input("I enjoy exercising.")

outdoor1 = input("I'll go crazy if I do not go out of the house for the whole day.")
outdoor1 = input("I am up for any tough challenges.")

music1 = input("I can see colours in my mind when I hear music.")
music1 = input("I have a feel for listening to classical music.")


volleyball2 = input("I like competitve ball games")
TAF2 = input("I like running long distance and short distance")
=======
volleyball2 = input("I like ball games")
TAF2 = input("I like running long and short distances")


outdoor2 = input("I'm good with tying knots and ropes.")

music2 = input("I play a musical instrument well.")
music2 = input("I can play a musical instrument well.")


volleyball_final = int(volleyball1) + int(volleyball2)
TAF_final = int(TAF1) + int(TAF2)
outdoor_final = int(outdoor1) + int(outdoor2)
music_final = int(music1)+ int(music2)

print()

if volleyball_final > outdoor_final and volleyball_final > music_final:
  print("You might be suitable for volleyball!")
if TAF_final > outdoor_final and TAF_final > music_final:
  print("You might be suitable for Track and field!")
elif outdoor_final > music_final:
  print("You might be stuiable for ODAC!")
  print("You might be stuiable for Outdoor Adventure Club!")
else:
  print("You might be suitable for Band!")
