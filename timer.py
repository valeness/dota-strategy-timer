import time
import os

class creepInfo():
	def main(self):
		start_time = time.time()
		global dota_time
		dota_time += 1
		
		os.system('cls')
		print "Tick: %s" % dota_time	

		creep_state = int(dota_time / 450)

		if creep_state > 30:
			creep_state = 30

		# Creep Stats
		melee_HP = 550 + (10 * creep_state)
		melee_DMG = 21 + (1 * creep_state)
		ranged_HP = 300 + (10 * creep_state)
		ranged_DMG = 23 + (2 * creep_state)
		siege_HP = 550
		siege_DMG = 40

		# Mega Creep Stats
		mega_melee_HP = 700 + (19 * creep_state)
		mega_melee_DMG = 40 + (2 * creep_state)
		mega_ranged_HP = 475 + (19 * creep_state)
		mega_ranged_DMG = 43 + (2 * creep_state)
		mega_siege_HP = 1015
		mega_siege_DMG = 56

		# Creep Wave Number
		num_wave = 1 + (dota_time / 30)

		# Creep Lineup
		num_melee = 3
		num_ranged = 1
		num_siege = 0

		# Extra Melee Creep
		if dota_time == 1050:
			num_melee += 1
		elif dota_time == 2040:
			num_melee += 1
		elif dota_time == 3030:
			num_melee += 1

		# Extra Ranged Creep
		if dota_time == 2730:
			num_ranged += 1

		# Extra Siege Creep
		if num_wave % 7 == 0:
			num_siege += 1

		num_creeps = num_melee + num_ranged + num_siege
		total_creeps = num_creeps * num_wave

		num_creeps_array = [num_melee, num_ranged, num_siege]

		def total(melee, ranged, siege, total_wave_reward):

			num_reward = [melee, ranged, siege]

			total_reward = zip(num_creeps_array, num_reward)
			for i in total_reward:
				total_wave_reward += i[0] * i[1]

			return total_wave_reward

		print "Gold: " + str(total(43, 48, 74, 0))
		print "Exp: " + str(total(62, 41, 88, 0))
		print "Mega Gold: " + str(total(22, 22, 74, 0))
		print "Mega Exp: " + str(total(25, 25, 88, 0))

		execution_time = "{0:.2f}".format(time.time() - start_time)
		print "Execution Time: %s" % (execution_time)

		time.sleep(1.0 - float(execution_time))

print('Input Negative Times for (Time until match starts)')
dota_time = int(raw_input('Input Time to start at: '))

while True:
	creep = creepInfo()
	creep.main()