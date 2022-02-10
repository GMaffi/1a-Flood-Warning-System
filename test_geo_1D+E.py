from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

stations = build_station_list()

def test_rivers_with_station():
	"Tests that repeated river names have been excluded from the set"
	list_river_names = []
	for station in stations:
		list_river_names.add(station.river)
	assert len(set_river) < len(stations) 

def test_stations_by_river():
	"Tests certain keys to ensure they have the appropriate associated stations"
    d = stations_by_river(stations)
    assert d.get('River Aire') = ['Airmyn', 'Apperley Bridge', 'Armley', 'Beal Weir Bridge', 'Bingley', 'Birkin Holme Washlands', 'Carlton Bridge', 'Castleford', 'Chapel Haddlesey', 'Cononley', 'Cottingley Bridge', 'Ferrybridge Lock', 'Fleet Weir', 'Gargrave', 'Kildwick', 'Kirkstall Abbey', 'Knottingley Lock', 'Leeds Crown Point', 'Leeds Crown Point Flood Alleviation Scheme', 'Leeds Knostrop Weir Flood Alleviation Scheme', 'Oulton Lemonroyd', 'Saltaire', 'Snaygill', 'Stockbridge']
    
def test_rivers_by_station_number():
    "Tests that the list outputted from the function is sorted correctly"
    station_number = []
    for tuple in rivers_by_station_number(stations, 9):
        station_number.append(tuple[1])
    for i in range(1, len(station_number)):
        current_station_number = stations[i]
        previous_station_number = stations[i-1]
        assert current_station_number[1] >= previous_station_number[1]