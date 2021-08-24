def beCheerful(name='', repeat=2):		# set defaults when declaring the parameters
	print(f"good morning {name}\n" * repeat)


beCheerful() 
#output: Good morning   
#        Good morning

beCheerful("tim")

beCheerful(name="john")		

beCheerful(repeat=6)

beCheerful(name="michael", repeat=5)

beCheerful(repeat=3, name="kb")