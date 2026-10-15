# import matplotlib.pyplot as plt

# baholar = [60,75,80,70,90]

# plt.plot(baholar)
# plt.title("imtihon natijalari")
# plt.xlabel("imtihonlar")
# plt.ylabel("ballar")
# plt.grid(True)
# plt.show()




# import matplotlib.pyplot as plt

# kunlar = ["d","s","ch","p","j"]
# savdo = [10,15,8,20,18]

# plt.bar(kunlar,savdo,color="blue",)
# plt.title("Hafta sotuvlari")
# plt.xlabel("kunlar")
# plt.ylabel("savdosi")
# plt.grid(True)

# plt.show()




# import matplotlib.pyplot as plt

# baholar = [20,22,24,21,25,27,23]

# plt.plot(baholar,marker="o",color="red")
# plt.title("ob havo natijalari")
# plt.xlabel("kunlar")
# plt.ylabel("harorat (C)")
# plt.grid(True)
# plt.show()


# import matplotlib.pyplot as plt 

# boy = [150,155,160,170,175]
# vazn = [45,48,52,55,60]

# plt.scatter(vazn,boy)

# plt.title("odam malumotlari")
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt 
# ranglar = ["qizil","kok","yashil","sariq"]
# sonlar = [1,2,3,4]

# plt.pie(sonlar,labels=ranglar,autopct="%1.1f%%")
# plt.show()

# import matplotlib.pyplot as plt 
# bosqichlar = [1,2,3,4,5,6]
# ballar = [10,20,18,30,35,50]

# plt.plot(bosqichlar,ballar,marker="o",color="red",linestyle="-.")
# plt.grid(True)
# plt.show()
import matplotlib.pyplot as plt 

import random
sonlar =[random.randint(1,100)for i in range((50))]
plt.hist(sonlar)