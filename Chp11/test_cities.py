from city_functions import city_country

def test_city_country_cap():
    """Does the program return data in the format City, Country???"""
    cc = city_country('Santiago', 'Chile')
    assert cc == 'Santiago, Chile'

def test_city_country_uncap():
    """Does the program return data in the format City, Country, if both the city
    and the country are not capitalized???"""
    cc = city_country('santiago', 'chile')
    assert cc == 'Santiago, Chile'

def test_city_country_cap_uncap():
    """Does the program return data in the format City, Country, if only City is Capitalized???"""
    cc = city_country('Santiago', 'chile')
    assert cc == 'Santiago, Chile'

def test_city_country_uncap_cap():
    """Does the program return data in the format City, Country, if only Country is Capitalized???"""
    cc = city_country('santiago', 'Chile')
    assert cc == 'Santiago, Chile'

def test_city_country_population():
    """Does the program return data in the format City, Country -Population xxx if population is given 
    as a parameter???"""
    cc = city_country('Santiago', 'Chile', population=5000000)
    assert cc == 'Santiago, Chile -Population 5000000'