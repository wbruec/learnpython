import json

with open("cardano_out_data/out.json", "r") as read_file:
    data = json.load(read_file)

#id = (data[0]["id"])
#fee = data[0]["fee"]["quantity"]

x = 0
error_fees = []
for i in data:
    fee = data[x]["fee"]["quantity"]
    id = data[x]["id"]
    x += 1
    if fee < 1:
        error_fees.append(fee)

