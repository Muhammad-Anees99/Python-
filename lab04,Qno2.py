inseconds=eval(input("Enter time in seconds:"))
inhours=(inseconds/3600)
hours=int(inhours)
inmins=(inhours-int(inhours))*60
mins=int(inmins)
seconds=(inmins-mins)
seconds=(inmins-mins)*60
print(f'{hours} hours :{mins} minutes : {seconds:.0f} seconds')