d=[23,12,9]
try:
   print(d[1])
except NameError:
   print("Name is not defined")
except TypeError:
   print("PLease provide correct values")
except IndexError:
   print("Index position not found")
except Exception as e:
   print("Error ",e)
else:
   print("Successfully executed in try block")
finally:
   print("Completed")