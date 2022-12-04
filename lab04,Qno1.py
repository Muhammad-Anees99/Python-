inseconds=eval(input("Enter time in seconds:"))
inmins=inseconds/60
mins=int(inmins)
seconds=(inmins-mins)*60
print(f'{mins}minutes : {seconds:.0f}seconds')
