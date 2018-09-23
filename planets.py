def weight_on_planets():
	weight = float(input('What do you weigh on earth? '))
	print('\n'+ 'On Mars you would weigh','%.2f' % round(weight*0.38,2),'pounds.'+'\n'+'On Jupiter you would weigh','%.2f' % round( weight*2.34,2),'pounds.')
   
if __name__ == '__main__':
   weight_on_planets()
