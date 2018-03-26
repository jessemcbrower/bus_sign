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
	nxt_times = []
	for pl in predictList:
		bus_num = pl.data[1]
		if pl.predictions:
			for p in pl.predictions:
				t = p - (currentTime - pl.lastQueryTime)
				nxt_times.append(str(int(t/60)))

		# IF NO BUSES ARE COMING

		if len(nxt_times) == 0:
			message = '      No buses today.      '

		# IF ONE BUS IS COMING

		elif len(nxt_times) == 1:
			message = '      The next ' + bus_num + ' bus arrives in: ' + str(nxt_times[0]) + ' minutes.      '

		# IF MULTIPLE BUSES ARE COMING

		elif len(nxt_times) > 1:
			message = '      The next ' + bus_num + ' buses arrive in: ' + (', '.join(str(e) for e in nxt_times[0:-1])) + ' and ' + str(nxt_times[-1]) + ' minutes.      '

	prevTime = currentTime

	# SETS MESSAGE TO SCROLL

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