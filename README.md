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

### 3. Conversion App

### 4. API

### 5. Unit Testing

### 6. GUI

### 7. Containerization

### 8. CI/CD
