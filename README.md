Here is the output of my file

I used data set 5

Tommys-MacBook-Pro:HW4 tommydifranco$ python3 2026_ia626_difrantc_taxi.py
Field names: ['medallion', 'hack_license', 'vendor_id', 'rate_code', 'store_and_fwd_flag', 'pickup_datetime', 'dropoff_datetime', 'passenger_count', 'trip_time_in_secs', 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']


Q1: Row Count & Datetime Range

| Metric              | Value                     |
|---------------------|--------------------------|
| Total Rows          | 15,285,049               |
| Datetime Start      | 2013-05-01 00:00:00      |
| Datetime End        | 2013-05-31 23:59:59      |

Q2 & Q3: Field Names & Sample Data

  | Field                | Value                          |
|----------------------|--------------------------------|
| medallion            | 3B1A31779BCE30367D00C6F7911573C0 |
| hack_license         | AED0496C937E41C4515D64E851F873AB |
| vendor_id            | VTS                            |
| rate_code            | 1                              |
| store_and_fwd_flag   |                                |
| pickup_datetime      | 2013-05-01 00:04:00            |
| dropoff_datetime     | 2013-05-01 00:12:00            |
| passenger_count      | 1                              |
| trip_time_in_secs    | 480                            |
| trip_distance        | 1.34                           |
| pickup_longitude     | -73.982285                     |
| pickup_latitude      | 40.772816                      |
| dropoff_longitude    | -73.986214                     |
| dropoff_latitude     | 40.758743                      |

Q5: Geographic Range
| Field              | Minimum      | Maximum      |
|--------------------|-------------|-------------|
| Pickup Latitude    | -3117.4717  | 2354.8628   |
| Pickup Longitude   | -2342.2798  | 123.7318    |
| Dropoff Latitude   | -3447.9065  | 3210.3794   |
| Dropoff Longitude  | -2211.7773  | 2386.9951   |

Q6: Average Haversine Trip Distance
| Metric                         | Value        |
|---------------------------------|-------------|
| Average Distance (miles)       | 2.2791      |
| Valid Rows Used for Computation| 14,996,660  |

Q6: Trip Distance Histogram
  [Alt text](Q6_histogram.png)


Q7: Distinct Values
  | Field                | Distinct Values                                  |
|----------------------|--------------------------------------------------|
| vendor_id            | VTS, CMT                                         |
| rate_code            | 0, 1, 2, 3, 4, 5, 6, 7, 65, 210                  |
| store_and_fwd_flag   | (empty), N, Y                                    |

Q8: Numeric Min/Max
  | Field               | Minimum | Maximum  |
|---------------------|--------|----------|
| passenger_count     | 0.0    | 6.0      |
| trip_time_in_secs   | 0.0    | 10800.0  |
| trip_distance       | 0.0    | 100.0    |

Q9: Average Passengers by Hour (Full Dataset)
[Alt text](Q9histogram.png)

Q11: Average Passengers by Hour (Reduced Dataset Compared to Full )
[Alt text](Q11_average_passengers.png)


