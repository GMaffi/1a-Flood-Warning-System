from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

stations = build_station_list()

def test_rivers_with_station():
	"Tests that repeated river names have been excluded from the set"
	list_river_names = []
	for station in stations:
		list_river_names.append(station.river)
	assert len(list_river_names) <= len(stations) 

def test_stations_by_river():
    "Tests certain keys to ensure they have the appropriate associated stations"
    d = stations_by_river(stations)
    assert d.get('River Aire') == ['Cononley', 'Gargrave', 'Fleet Weir', 'Snaygill', 'Ferrybridge Lock', 'Saltaire', 'Bingley', 'Airmyn', 'Castleford', 'Carlton Bridge', 'Armley', 'Cottingley Bridge', 'Kildwick', 'Chapel Haddlesey', 'Beal Weir Bridge', 'Stockbridge', 'Leeds Crown Point', 'Knottingley Lock', 'Kirkstall Abbey', 'Birkin Holme Washlands', 'Apperley Bridge', 'Oulton Lemonroyd', 'Leeds Knostrop Weir Flood Alleviation Scheme', 'Leeds Crown Point Flood Alleviation Scheme']

def test_rivers_by_station_number():
    "Tests that the list outputted from the function is sorted correctly"
    station_number = []
    for tuple in rivers_by_station_number(stations, 9):
        station_number.append(tuple[1])
    for i in range(1, len(station_number)):
        assert station_number[i] <= station_number[i-1]

