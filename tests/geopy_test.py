from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="your_app_name", timeout=10)  # REQUIRED by Nominatim

location = geolocator.reverse(
    (49.92284543678744, 36.42757826271524), exactly_one=True, addressdetails=True
)

address = location.raw["address"]


print(address)
