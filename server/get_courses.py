import glob
import json
import pandas as pd
import sys


school = sys.argv[1]

courses = pd.Series()

for file in glob.glob(f"csv/{school}/*"):
    df = pd.read_csv(file)

    with open("text.txt", 'w') as file:
        file.write(df["CRS SUBJ CD"].to_string() + courses.to_string())

    courses = pd.concat([courses, df["CRS SUBJ CD"].dropna()])
    courses.drop_duplicates(inplace=True)

print(json.dumps(sorted(courses)))