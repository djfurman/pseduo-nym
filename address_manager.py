from geopy.geocoders import LiveAddress
import os

smarty_streets = LiveAddress(
    auth_id=os.getenv("SMARTY_STREETS_AUTH_ID"),
    auth_token=os.getenv("SMARTY_STREETS_AUTH_TOKEN")
)

location = smarty_streets.reverse("37.51423, -77.58351")
# location = smarty_streets.geocode(
#     query="1471 Robindale Rd, Richmond, VA 23235, USA"
# )

print(location.address)
print(location.latitude)
print(location.longitude)
