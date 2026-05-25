# Student Analyser

import pandas as pd
import sys
import json
from datetime import datetime, date

# validate country, joined date and bet status
def validate_data(data):
    for x in data.index:
        if pd.isna(data.loc[x,"country"]):
            data.loc[x,"country"] = "missing"

        if pd.isna(data.loc[x,"joined_date"]):
            data.loc[x,"joined_date"] = "missing"
        else:    
            if datetime.strptime((data.loc[x,"joined_date"]), "%d/%m/%Y").date() > date.today():
                data.loc[x,"joined_date"] = "incorrect"

        if pd.isna(data.loc[x,"bet_status"]):
            data.loc[x,"bet_status"] = "missing"
        else:
            if (data.loc[x,"bet_status"]).lower() not in ["active", "completed"]:
                data.loc[x,"bet_status"] = "incorrect"
    return data

input_file = "students.csv"
output_file = "report.json"

# read student data
try: 
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"File not found: {input_file}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

# validate data
df = validate_data(df)

total_students = len(df)
students_by_country = df["country"].value_counts().to_dict()
students_by_joineddate = df["joined_date"].value_counts().to_dict()
students_by_betstatus = df["bet_status"].value_counts().to_dict()

report = {
    "Total Students": total_students,
    "Students by Country": students_by_country,
    "Students by Joined Date": students_by_joineddate,
    "Students by Bet Status": students_by_betstatus
}

# print report
for key,value in report.items():
    if type(value) == dict: 
        print(f"\n{key}:")
        for key1,value1 in value.items():
            print(key1,value1)
    else:
        print(f"{key}:\n{value}")

# write report to json file
with open(output_file, "w") as f:
    json.dump(report, f, indent=4)

print(f"\nReport saved to {output_file}\n")






