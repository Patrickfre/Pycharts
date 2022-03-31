import matplotlib.pyplot as plt

daļas=[25,45,15,15] 
teksts=["labi","optimāli","traģiski","ģēnijs"]
krasas=["green","red","blue","purple"]
izcelums=[0.02,0.02,0.02,0.02]
autopct="%1.1f%%"

plt.pie(daļas,colors=krasas,explode=izcelums,labels=teksts,autopct="%1.1f%%")
plt.title("Mācības")
plt.style.use("Solarize_Light2")
plt.show()