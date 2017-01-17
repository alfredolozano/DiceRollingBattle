## Auth: alfredolozano
# Call the 'battleDiceRoll' function to start a battle
# inputs are the number of troops in the territory that is attacking
# and the number of troops in the territory that is defending


def battleDiceRoll(attacking_troops, defending_troops): 
	print('==============================') 
	print('|| Att || Def|| TA || TD ||')
	print('==============================')
	return BDR(attacking_troops, defending_troops)


def BDR(attacking_troops, defending_troops):
	if attacking_troops == 1 or defending_troops == 0:
		print('==============================')
		if attacking_troops > defending_troops:
			print(''.join(['Att wins with ', str(attacking_troops), ' troops.']))
		else:
			print(''.join(['Def wins with ', str(defending_troops), ' troops.']))
	else:
		if attacking_troops > 3:
			if defending_troops > 1 :
				attack = sorted([
							random.randint(1,6)
							for i in range (1,4)], reverse = True)
				deffense = sorted([
							random.randint(1,6)
							for i in range (1,3)], reverse = True)
				if attack[0] > deffense[0]: defending_troops = defending_troops - 1
				else: attacking_troops = attacking_troops - 1
				if attack[1] > deffense[1]: defending_troops = defending_troops - 1
				else: attacking_troops = attacking_troops - 1
			else:
				attack = sorted([
							random.randint(1,6)
							for i in range (1,4)], reverse = True)
				deffense = sorted([
							random.randint(1,6)
							for i in range (1,2)], reverse = True)
				if attack[0] > deffense[0]: defending_troops = defending_troops - 1
				else: attacking_troops = attacking_troops - 1
		elif attacking_troops == 3:
			if defending_troops > 1 :
				attack = sorted([
							random.randint(1,6)
							for i in range (1,3)], reverse = True)
				deffense = sorted([
							random.randint(1,6)
							for i in range (1,3)], reverse = True)
				if attack[0] > deffense[0]: defending_troops = defending_troops - 1
				else: attacking_troops = attacking_troops - 1
				if attack[1] > deffense[1]: defending_troops = defending_troops - 1
				else: attacking_troops = attacking_troops - 1
			else:
				attack = sorted([
							random.randint(1,6)
							for i in range (1,3)], reverse = True)
				deffense = sorted([
							random.randint(1,6)
							for i in range (1,2)], reverse = True)
				if attack[0] > deffense[0]: defending_troops = defending_troops - 1
				else: attacking_troops = attacking_troops - 1
		else:
			if defending_troops > 1 :
				attack = sorted([
							random.randint(1,6)
							for i in range (1,2)], reverse = True)
				deffense = sorted([
							random.randint(1,6)
							for i in range (1,3)], reverse = True)
				if attack[0] > deffense[0]: defending_troops = defending_troops - 1
				else: attacking_troops = attacking_troops - 1
			else:
				attack = sorted([
							random.randint(1,6)
							for i in range (1,2)], reverse = True)
				deffense = sorted([
							random.randint(1,6)
							for i in range (1,2)], reverse = True)
				if attack[0] > deffense[0]: defending_troops = defending_troops - 1
				else: attacking_troops = attacking_troops - 1				
		string = "".join( ['|| ', ''.join(map(str, attack)), ' || ',
		''.join(map(str, deffense)), ' || ', str(attacking_troops), ' || ', 
		str(defending_troops), ' ||'] )
		print(string)
		return BDR(attacking_troops,defending_troops)
