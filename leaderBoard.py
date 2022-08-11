import os

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
                    values[1] = int(values[1])
                    all_values.append(values)

            all_values.sort(key=lambda row: row[1], reverse=True)
            return all_values
