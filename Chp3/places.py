locations = ["Brazil", "India", "United Arab Emirates", "Qatar", "Taiwan"]

print(f"Original order of list: {locations}")

print(f"Sorted list: {sorted(locations, reverse=True)}")

print(f"Original order of list still exists!!! {locations}")

locations.reverse()

print(f"Reversed and changed: {locations}")

locations.reverse()

print(f"Back in original order of list: {locations}")

locations.sort()

print(f"Alphabetical Order: {locations}")

locations.sort(reverse=True)

print(f"Reverse-Alphabetical Order: {locations}")

