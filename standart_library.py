from datetime import datetime, timedelta, timezone
now = datetime.now(timezone.utc)
print(now)
later = now + timedelta(hours=6)
print(later)
iso = now.isoformat()
print(later)

from collections import Counter, defaultdict
words = ["Tahmid", "Habib", "Nayeem", "Habib", "Tahmid", "Mohin", "Habib"]

c = Counter(words)
print(c)

groups = defaultdict(list)

for plate, trip in [("Dhaka 120", 50), ("Dhaka 120", 150),("Chatto 984", 20), ("Cumilla 678", 12)]:
    groups[plate].append(trip)

print(groups)

import itertools
pair = list(itertools.combinations([1,2,3,4], 2))
triad = list(itertools.combinations([1,2,3,4], 3))
print(pair)
print(triad)