arn = "arn:resources::account:12345/jhony"
print(arn.split("/"))  #["arn:resources::account:12345, jhony"]
print(arn.split("/")[1]) #jhony