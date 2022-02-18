values = 1, 2, 3, 4

x, y, z, t = values

# Karsi tarafta atayacagimiz eleman sayisi ,
# esitledigimiz listgedeki elemanlarin sayisina
# esit degilse hata verir

# a,b = values
# a,b,c,d = values

a, b, *c = values
print(c)