from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
	'''возвращает для заданной страны ее код Pygal, из 2-х букв'''
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
			#если страна не найдена вернуть None
			return None
