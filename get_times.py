import time
from predict import predict

# USE THIS ON THE PHAT SIDE TO SEE LIGHTS

import scrollphathd as sphd
sphd.set_brightness(0.2)
sphd.rotate(180)

stops = [
  ( 'mbta', '62', '7919', 'Alewife' ),
  ( 'mbta', '627', '7919', 'Alewife' ),
  ( 'mbta', '77', '7922', 'Harvard' )
]

predictList = []
for s in stops:
	predictList.append(predict(s))

time.sleep(1)

def get_times():
	currentTime = time.time()
	nxt_times = []
	for pl in predictList:
		bus_num = pl.data[1]
		if pl.predictions:
			for p in pl.predictions:
				t = p - (currentTime - pl.lastQueryTime)
				nxt_times.append(str(int(t/60)))

		# USE THIS ON THE MAC SIDE FOR TESTING IN THE CONSOLE

		# print 'The next ' + bus_num + ' bus will arrive in: '
		
		if len(nxt_times) == 0:

			# USE THIS ON THE PHAT SIDE TO SEE LIGHTS

			string = '     No buses today.     '
			# sphd.write_string(string)

		elif len(nxt_times) == 1:
			
			# USE THIS ON THE PHAT SIDE TO SEE LIGHTS

			string = '     The next ' + bus_num + ' bus arrives in: ' + str(nxt_times[0]) + " minutes.     "
			# sphd.write_string(string)

			# USE THIS ON THE MAC SIDE FOR TESTING IN THE CONSOLE

			# print str(nxt_times[0]) + " minutes."

		elif len(nxt_times) > 1:

			# USE THIS ON THE PHAT SIDE TO SEE LIGHTS
			
			string = '     The next ' + bus_num + ' buses arrive in: ' + (', '.join(str(e) for e in nxt_times[0:-1])) + ' and ' + str(nxt_times[-1]) + ' minutes.     '
			# sphd.write_string(string)

			# USE THIS ON THE MAC SIDE FOR TESTING IN THE CONSOLE

			# print (', '.join(str(e) for e in nxt_times[0:-1])) + ' and ' + str(nxt_times[-1]) + ' minutes.'

			# USE THIS ON THE MAC SIDE FOR TESTING IN THE CONSOLE

			# print 'No buses today.'

	# sphd.show()
	# sphd.scroll()
	
	prevTime = currentTime
	sphd.write_string(string)
	sphd.show()
	sphd.scroll()

while True:
	get_times()