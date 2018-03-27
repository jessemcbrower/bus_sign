# Scroll pHAT HD - Bus Sign

A project using NextBus data to tell me when my next bus is coming

## To add your own bus stop data:

Run routefinder.py to find your stops

```
1. Delete everything inside of stops = []

2. Run routefinder.py

3. Paste results into stops = []

4. Repeat as needed
```

## To start app on power up:

```
1. sudo nano /ect/rc.local

2. Line to add is: python {path to script}

3. Add line to script above exit 0
```

### App will start when Pi is plugged in