# STEP : 4
# EVERYTHING AS USUAL before
mycursor.execute("SELECT * FROM studentscg WHERE age > 22")

for x in mycursor :
    print(x)
