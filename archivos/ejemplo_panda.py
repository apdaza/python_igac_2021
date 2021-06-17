import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('fuentes/chat_performance_clean.csv')

print(data.head())

chats_per_user = data.groupby('user_id')['chat_id'].count().reset_index()
chats_per_user.columns = ['user_id', 'number_chats']
chats_per_user = chats_per_user.sort_values(
    'number_chats', ascending = False
    )
print(chats_per_user.head())

plt.rcParams['figure.figsize'] = [10, 10]


chats_per_user[0:10].plot(
    x = 'user_id',
    y = 'number_chats',
    kind = 'bar',
    legend = False,
    color = 'blue',
    width = 0.8
    )

plt.ylabel("Number of chats")
plt.xlabel("User")
plt.title("chats per user")
plt.gca().yaxis.grid(linestyle=":")
plt.savefig("chats_per_user.png")
