Here is the output of my file
I used data set 5

Tommys-MacBook-Pro:HW4 tommydifranco$ python3 2026_ia626_difrantc_taxi.py
Field names: ['medallion', 'hack_license', 'vendor_id', 'rate_code', 'store_and_fwd_flag', 'pickup_datetime', 'dropoff_datetime', 'passenger_count', 'trip_time_in_secs', 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']

Q1: Row Count & Datetime Range
Total rows: 15285049
Datetime range: 2013-05-01 00:00:00 to 2013-05-31 23:59:59

Q2 & Q3: Field Names & Sample Data
  medallion: 3B1A31779BCE30367D00C6F7911573C0
  hack_license: AED0496C937E41C4515D64E851F873AB
  vendor_id: VTS
  rate_code: 1
  store_and_fwd_flag: 
  pickup_datetime: 2013-05-01 00:04:00
  dropoff_datetime: 2013-05-01 00:12:00
  passenger_count: 1
  trip_time_in_secs: 480
  trip_distance: 1.34
  pickup_longitude: -73.982285
  pickup_latitude: 40.772816
  dropoff_longitude: -73.986214
  dropoff_latitude: 40.758743

Q5: Geographic Range
Pickup Latitude:   -3117.4717 to 2354.8628
Pickup Longitude:  -2342.2798 to 123.7318
Dropoff Latitude:  -3447.9065 to 3210.3794
Dropoff Longitude: -2211.7773 to 2386.9951

Q6: Average Haversine Trip Distance
Average distance: 2.2791 miles
Computed from 14996660 valid rows

Q7: Distinct Values
  vendor_id: {'VTS', 'CMT'}
  rate_code: {'7', '6', '2', '5', '4', '0', '3', '210', '65', '1'}
  store_and_fwd_flag: {'', 'N', 'Y'}

Q8: Numeric Min/Max
  passenger_count: min=0.0, max=6.0
  trip_time_in_secs: min=0.0, max=10800.0
  trip_distance: min=0.0, max=100.0

Q9: Average Passengers by Hour (Full Dataset)
Hour   Avg Passengers  Count
  00:00  1.7557          615159   #################
  01:00  1.7475          447404   #################
  02:00  1.7488          325517   #################
  03:00  1.7441          231684   #################
  04:00  1.7151          169224   #################
  05:00  1.6080          152723   ################
  06:00  1.5788          324381   ###############
  07:00  1.6172          578670   ################
  08:00  1.6462          700296   ################
  09:00  1.6529          716646   ################
  10:00  1.6775          697113   ################
  11:00  1.6951          724912   ################
  12:00  1.7053          758422   #################
  13:00  1.7120          739119   #################
  14:00  1.7252          762057   #################
  15:00  1.7438          713664   #################
  16:00  1.7403          581581   #################
  17:00  1.7346          715131   #################
  18:00  1.7254          895596   #################
  19:00  1.7304          952499   #################
  20:00  1.7314          911934   #################
  21:00  1.7476          904301   #################
  22:00  1.7561          881508   #################
  23:00  1.7610          785508   #################

Q10: Writing reduced CSV (1 in every 1000 rows)
Reduced CSV written: 15285 rows into trip_data_reduced.csv

Q11: Average Passengers by Hour (Reduced Dataset - 1 in 1000 rows)
Hour   Avg Passengers  Count
  00:00  1.6917          652   ################
  01:00  1.8144          431   ##################
  02:00  1.7111          315   #################
  03:00  1.8182          220   ##################
  04:00  1.9444          198   ###################
  05:00  1.6250          128   ################
  06:00  1.6541          292   ################
  07:00  1.6250          592   ################
  08:00  1.6241          705   ################
  09:00  1.6419          740   ################
  10:00  1.7137          695   #################
  11:00  1.7357          719   #################
  12:00  1.6730          740   ################
  13:00  1.6542          697   ################
  14:00  1.6332          747   ################
  15:00  1.7169          717   #################
  16:00  1.7572          593   #################
  17:00  1.7020          745   #################
  18:00  1.7553          952   #################
  19:00  1.6770          935   ################
  20:00  1.7440          918   #################
  21:00  1.7246          904   #################
  22:00  1.7520          879   #################
  23:00  1.6861          771   ################

Q6: Trip Distance Histogram
Range (mi)   Count      Bar
  0-1        5220594    ########################################
  1-2        4819887    ####################################
  2-5        3655543    ############################
  5-10       941316     #######
  10-20      355321     ##
  20-50      2723       
  50+        1276     
