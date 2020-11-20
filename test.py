from sensitive_data import aid, account, room, roomid, area, areaname, building, buildingid

# Test Get Electricity Bill
from get_elec import get_elec

print(get_elec(aid, account, room, roomid, area, areaname, buildingid, building))
