import os, discord

def getMON(guild_id, member):
    filename = './user_data/' + str(guild_id) + '.txt'
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            lines = file.read().splitlines()
            for line in lines:
                values = line.split(",")
                if len(values) >= 2:
                    values = [v.strip() for v in values]
                    member_id = int(values[0])
                    if member_id == member.id:
                        return int(values[1])
    return 0

def modMON(guild, member, mon):
    if mon > 0:
        moneys = mon
    else:
        moneys = 0
        
    filename = './user_data/' + str(guild.id) + '.txt'
    if os.path.isfile(filename):
        newContent = '';
        member_found = False
        with open(filename, 'r') as file:
            lines = file.read().splitlines()
            for line in lines:
                values = line.split(",")
                if len(values) >= 2:
                    values = [v.strip() for v in values]
                    member_id = int(values[0])
                    if member_id == member.id:
                        member_found = True
                        moneys = int(values[1]) + mon
                        if moneys < 0:
                           moneys = 0
                        values[1] = str(moneys)
                newContent = newContent + values[0] + ', ' + values[1] + '\n'
            if not member_found:
                newContent = newContent + str(member.id) + ', ' + str(moneys) + '\n'
        with open(filename, 'w') as file:
            file.write(newContent)
    else:
        with open(filename, 'w') as file:
            file.write(str(member.id) + ', ' + str(moneys) + '\n')

