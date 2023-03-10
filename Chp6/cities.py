cities = {"Houston":{"Country":"USA", "Population":"2.288 million", "Fact":"Named After Sam Houston."},
         "Timbuktu":{"Country":"Mali", "Population":"32460", "Fact":"Is a historical center of Islamic Scholarship."},
         "Jakarta":{"Country":"Indonesia", "Population":"10.56 million","Fact":"Is the largest city in Southeast Asia." }}

for k,city_info in cities.items():
    print(f"\nCity: {k}")
    for classifier,fact in city_info.items():
        print(f"\t{classifier}")
        print(fact)
