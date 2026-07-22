distance_mi=50
is_raining=True
has_bike=False
has_car=False
has_ride_share_app=True
if not distance_mi:
 print('False')
elif distance_mi <= 1:
    print(not is_raining)
elif distance_mi <= 6:
    print(has_bike and not is_raining)
else:
    print(has_ride_share_app or has_car)
