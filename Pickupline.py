import csv

lines = ["Are you a magician? Because whenever I look at you, everyone else disappears",
         "Do you have a map? Because I keep getting lost in your eyes",
         "Do you believe in love at first sight, or should I walk by again?"]

# success rate of each pickup line
success_rate = {"Are you a magician? Because whenever I look at you, everyone else disappears": 0.7,
                "Do you have a map? Because I keep getting lost in your eyes": 0.4,
                "Do you believe in love at first sight, or should I walk by again?": 0.6}

# sort pickup lines based on success rate
pickup_lines = sorted(lines, key=lambda x: success_rate[x], reverse=True)

# write pickup lines and success rate to CSV file
with open("pickup_lines.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Pickup Line", "Success Rate"])
    for line in pickup_lines:
        writer.writerow([line, success_rate[line]])


