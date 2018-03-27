import time
from predict import predict
import scrollphathd as sphd

# SETS DEFAULT BRIGHTNESS

sphd.set_brightness(0.2)

# ROTATES DISPLAY 180 DEGREES

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

while True:

	# GETS CURRENT BUS TIMES

	currentTime = time.time()
	message = []
	for pl in predictList:
		nxt_times = []
		bus_num = pl.data[1]
		destination = pl.data[3]
		if bus_num == '627':
			bus_num = '62/76'
		else:
			bus_num = pl.data[1]
		if pl.predictions:
			for p in pl.predictions:
				t = p - (currentTime - pl.lastQueryTime)
				nxt_times.append(str(int(t/60)))

		# IF ONE BUS IS COMING

		if len(nxt_times) == 1:
			string = '      The next ' + bus_num + ' bus arrives in: ' + str(nxt_times[0]) + ' minutes.      '
			message.append(string)

		# IF MULTIPLE BUSES ARE COMING

		elif len(nxt_times) > 1:
			string = '      The next ' + bus_num + ' buses arrive in: ' + (', '.join(str(e) for e in nxt_times[0:-1])) + ' and ' + str(nxt_times[-1]) + ' minutes.      '
			message.append(string)
	
	# MESSAGE FOR IF NO BUSES ARE COMING

	if message == []:
		message = '      No buses today.      '

	# MESSAGE FOR IF BUSES ARE COMING

	else:
		message = ' '.join(str(e) for e in message)

	prevTime = currentTime

	# SETS MESSAGE TO BUFFER

	sphd.write_string(message)

	# SCROLLS MESSAGE

	msg_len = sphd.get_buffer_shape()[0]
	for i in range(msg_len):
		sphd.show()
		sphd.scroll()

	# CLEARS SCREEN AND PAUSES 2 SECONDS

	sphd.clear()
	sphd.show()
	time.sleep(2)