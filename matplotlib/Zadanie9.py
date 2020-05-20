import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("zamowienia.csv",header=0,delimiter=";")
group=df.groupby(['Sprzedawca']).agg({"idZamowienia":['count']})
sprzedawca=group.index.values
zamowienia=[group.values[y][0] for y in range(len(group.values))]

Explode=[0 for i in range(len(group.index.values))]
Explode[5]=0.1

def prepare_label(pct, br):
    absolute = int(np.ceil(pct / 100. * np.sum(br)))
    return "{:.1f}% \n({}/{})".format(pct, absolute, sum(zamowienia))

wedges, texts, autotexts = plt.pie(zamowienia,explode=Explode, shadow=True,labels=sprzedawca,
                                   autopct=lambda pct: prepare_label(pct, zamowienia), textprops=dict(color="black"))

plt.setp(autotexts, size=8, weight="bold",rotation=-45)
plt.title(":)")
plt.legend(title='Sprzedawcy')
plt.show()