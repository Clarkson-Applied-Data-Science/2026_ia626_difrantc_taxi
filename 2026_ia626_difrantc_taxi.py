import csv
import math
import collections
import datetime

FILENAME = 'trip_data_5.csv'

def haversine(lat1, lon1, lat2, lon2):
    R = 3958.8
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    lat_difference = lat2 - lat1
    lon_difference = lon2 - lon1
    a = math.sin(lat_difference/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(lon_difference/2)**2
    return R * 2 * math.asin(math.sqrt(a))

row_count = 0
min_datetime = None
max_datetime = None

min_pickup_lat = float('inf');  max_pickup_lat = float('-inf')
min_pickup_lon = float('inf');  max_pickup_lon = float('-inf')
min_dropoff_lat = float('inf'); max_dropoff_lat = float('-inf')
min_dropoff_lon = float('inf'); max_dropoff_lon = float('-inf')

total_distance = 0
valid_distance_count = 0

passengers_by_hour = collections.defaultdict(list)
distinct_values = collections.defaultdict(set)
DISTINCT_FIELDS = ['vendor_id', 'rate_code', 'store_and_fwd_flag', 'payment_type']

numeric_fields = ['passenger_count', 'trip_time_in_secs', 'trip_distance']
numeric_min = {f: float('inf') for f in numeric_fields}
numeric_max = {f: float('-inf') for f in numeric_fields}

sample_data = None
field_names = None
reduced_rows = []

with open(FILENAME, 'r') as f:
    reader = csv.DictReader(f)
    reader.fieldnames = [field.strip() for field in reader.fieldnames]
    field_names = reader.fieldnames
    print("Field names:", field_names)

    for row in reader:
        row_count += 1

        if row_count == 1:
            sample_data = dict(row)

        if row_count % 1000 == 0:
            reduced_rows.append(row)

        try:
            dt = datetime.datetime.strptime(row['pickup_datetime'].strip(), '%Y-%m-%d %H:%M:%S')
            if min_datetime is None or dt < min_datetime:
                min_datetime = dt
            if max_datetime is None or dt > max_datetime:
                max_datetime = dt
            try:
                passengers_by_hour[dt.hour].append(int(row['passenger_count']))
            except:
                pass
        except:
            pass

        try:
            plat = float(row['pickup_latitude'])
            plon = float(row['pickup_longitude'])
            dlat = float(row['dropoff_latitude'])
            dlon = float(row['dropoff_longitude'])

            if plat != 0 and plon != 0:
                min_pickup_lat = min(min_pickup_lat, plat)
                max_pickup_lat = max(max_pickup_lat, plat)
                min_pickup_lon = min(min_pickup_lon, plon)
                max_pickup_lon = max(max_pickup_lon, plon)

            if dlat != 0 and dlon != 0:
                min_dropoff_lat = min(min_dropoff_lat, dlat)
                max_dropoff_lat = max(max_dropoff_lat, dlat)
                min_dropoff_lon = min(min_dropoff_lon, dlon)
                max_dropoff_lon = max(max_dropoff_lon, dlon)

            if plat != 0 and plon != 0 and dlat != 0 and dlon != 0:
                dist = haversine(plat, plon, dlat, dlon)
                total_distance += dist
                valid_distance_count += 1
        except:
            pass

        for field in DISTINCT_FIELDS:
            if field in row:
                distinct_values[field].add(row[field].strip())

        for field in numeric_fields:
            try:
                val = float(row[field])
                numeric_min[field] = min(numeric_min[field], val)
                numeric_max[field] = max(numeric_max[field], val)
            except:
                pass

print(f"\nQ1: Row Count & Datetime Range")
print(f"Total rows: {row_count}")
print(f"Datetime range: {min_datetime} to {max_datetime}")

print(f"\nQ2 & Q3: Field Names & Sample Data")
for field in field_names:
    print(f"  {field}: {sample_data.get(field, 'N/A')}")

print(f"\nQ5: Geographic Range")
print(f"Pickup Latitude:   {min_pickup_lat:.4f} to {max_pickup_lat:.4f}")
print(f"Pickup Longitude:  {min_pickup_lon:.4f} to {max_pickup_lon:.4f}")
print(f"Dropoff Latitude:  {min_dropoff_lat:.4f} to {max_dropoff_lat:.4f}")
print(f"Dropoff Longitude: {min_dropoff_lon:.4f} to {max_dropoff_lon:.4f}")

print(f"\nQ6: Average Haversine Trip Distance")
if valid_distance_count > 0:
    print(f"Average distance: {total_distance / valid_distance_count:.4f} miles")
    print(f"Computed from {valid_distance_count} valid rows")

print(f"\nQ7: Distinct Values")
for field, values in distinct_values.items():
    print(f"  {field}: {values}")

print(f"\nQ8: Numeric Min/Max")
for field in numeric_fields:
    print(f"  {field}: min={numeric_min[field]}, max={numeric_max[field]}")

print(f"\nQ9: Average Passengers by Hour (Full Dataset)")
print(f"{'Hour':<6} {'Avg Passengers':<15} {'Count'}")
for hour in range(24):
    vals = passengers_by_hour[hour]
    if vals:
        avg = sum(vals) / len(vals)
        bar = '#' * int(avg * 10)
        print(f"  {hour:02d}:00  {avg:.4f}          {len(vals)}   {bar}")

print(f"\nQ10: Writing reduced CSV (1 in every 1000 rows)")
with open('trip_data_reduced.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(reduced_rows)
print(f"Reduced CSV written: {len(reduced_rows)} rows into trip_data_reduced.csv")

passengers_by_hour_reduced = collections.defaultdict(list)

with open('trip_data_reduced.csv', 'r') as f:
    reader = csv.DictReader(f)
    reader.fieldnames = [field.strip() for field in reader.fieldnames]
    for row in reader:
        try:
            dt = datetime.datetime.strptime(row['pickup_datetime'].strip(), '%Y-%m-%d %H:%M:%S')
            passengers_by_hour_reduced[dt.hour].append(int(row['passenger_count']))
        except:
            pass

print(f"\nQ11: Average Passengers by Hour (Reduced Dataset - 1 in 1000 rows)")
print(f"{'Hour':<6} {'Avg Passengers':<15} {'Count'}")
for hour in range(24):
    vals = passengers_by_hour_reduced[hour]
    if vals:
        avg = sum(vals) / len(vals)
        bar = '#' * int(avg * 10)
        print(f"  {hour:02d}:00  {avg:.4f}          {len(vals)}   {bar}")

print(f"\nQ6: Trip Distance Histogram")
bins = [0, 1, 2, 5, 10, 20, 50, float('inf')]
bin_labels = ['0-1', '1-2', '2-5', '5-10', '10-20', '20-50', '50+']
bin_counts = [0] * len(bin_labels)

with open(FILENAME, 'r') as f:
    reader = csv.DictReader(f)
    reader.fieldnames = [field.strip() for field in reader.fieldnames]
    for row in reader:
        try:
            plat = float(row['pickup_latitude'])
            plon = float(row['pickup_longitude'])
            dlat = float(row['dropoff_latitude'])
            dlon = float(row['dropoff_longitude'])
            if plat != 0 and plon != 0 and dlat != 0 and dlon != 0:
                dist = haversine(plat, plon, dlat, dlon)
                for i in range(len(bins) - 1):
                    if bins[i] <= dist < bins[i+1]:
                        bin_counts[i] += 1
                        break
        except:
            pass

print(f"{'Range (mi)':<12} {'Count':<10} Bar")
max_count = max(bin_counts) if bin_counts else 1
for label, count in zip(bin_labels, bin_counts):
    bar = '#' * int((count / max_count) * 40)
    print(f"  {label:<10} {count:<10} {bar}")