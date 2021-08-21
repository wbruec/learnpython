import json

with open("cardano_out_data/out1.json", "r") as read_file:
    data = json.load(read_file)

#id = (data[0]["id"])
#fee = data[0]["fee"]["quantity"]

x = 0
lower_fees = []
for i in data:
    fee = data[x]["fee"]["quantity"]
    x += 1
    print(fee) if fee > 173289 else lower_fees.append(fee)

print(lower_fees)