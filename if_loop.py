


weight = int(input("enter weight : "))
unit = input("enter unit K for kgs and L for lbs: ")

if unit.upper()=='K':
    converted_weight = weight / 0.45
else:
    converted_weight = weight * 0.45

print("converted weight is ", converted_weight)


