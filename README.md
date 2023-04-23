# 5th-age-monster-builder

## Project Structure

```
.
├── README.md
├── data
│   ├── huge_stats.csv
│   ├── initiative.csv
│   ├── large_stats.csv
│   ├── mook_stats.csv
│   ├── normal_stats.csv
│   └── template.csv
├── docker
├── requirements.txt
├── src
│   ├── app.py
│   └── utils
│       ├── classes.py
│       └── data.py
└── tests
```

## Steps

### 1. OOP

Create a creature class in `utils/classes.py` and import it into `src/app.py` to test it. Add optional parameters to the class to allow for more customization down the road.

```python
from utils.classes import Creature

if __name__ == '__main__':
    test = Creature(name="Hello World")
    print(test.name)
```

```bash
$ python src/app.py
Hello World
```

### 2. Database

Create stat and options data in the `data` folder and options lists in `utils/data.py`. Import the data into `src/app.py` to test it. Convert the csv files into dictionaries for use in the `Creature` class and populating options lists later down the road.

```python
import csv
from utils.classes import Creature

if __name__ == '__main__':
    test = Creature(name="Orc")
    
    with open('data/normal_stats.csv', newline='', encoding='utf-8-sig') as statsfile:
        reader = csv.DictReader(statsfile)
        for row in reader:
            print(f'A Level {row["Monster Level"]} {test.name} has {row["AC"]} AC')
```

```bash
$ python src/app.py 
A Level 0 Orc has 16 AC
A Level 1 Orc has 17 AC
A Level 2 Orc has 18 AC
A Level 3 Orc has 19 AC
A Level 4 Orc has 20 AC
A Level 5 Orc has 21 AC
A Level 6 Orc has 22 AC
A Level 7 Orc has 23 AC
A Level 8 Orc has 24 AC
A Level 9 Orc has 25 AC
A Level 10 Orc has 26 AC
A Level 11 Orc has 27 AC
A Level 12 Orc has 28 AC
A Level 13 Orc has 29 AC
A Level 14 Orc has 30 AC
```

### 3. Conversion App

### 4. API

### 5. Unit Testing

### 6. GUI

### 7. Containerization

### 8. CI/CD
