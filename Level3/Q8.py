input = "Robert000Smith000123"
output = list(i for i in input.split('0')if len(i)>0)
print({
        "first_name": output[0],
        "last_name": output[1],
        "id": output[2]
})  
