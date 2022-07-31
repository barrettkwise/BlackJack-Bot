import os
import discord

def leaderboard(guild):
  all_values = []
  filename = './user_data/' + str(guild.id) + '.txt'
  if os.path.isfile(filename):
      with open(filename, 'r') as file:
          lines = file.read().splitlines()
          for line in lines:
              values = line.split(",")
              if len(values) >= 2:
                  values = [v.strip() for v in values]
                  all_values.append(values)
  return genLeaderboard(all_values)


def genLeaderboard(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    sub_li.reverse()
    return sub_li
    
    
                  


