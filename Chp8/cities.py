
import city
from city import describe_city
from city import describe_city as dc
import city as c
from city import *

"""Testing different import methods"""

city.describe_city("Tallahassee")

city.describe_city("Houston")

city.describe_city("Delhi", "India")

describe_city("Austin", "USA")

dc("Texas City", "USA")

c.describe_city("Washington D.C.", "USA")