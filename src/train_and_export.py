import json
import pandas as pd
from xgboost import XGBRegressor
import m2cgen as m2c

# Load training data
with open('public_cases.json') as f:
    data = json.load(f)

records = []
y = []
for d in data:
    trip = d['input']['trip_duration_days']
    miles = d['input']['miles_traveled']
    receipts = d['input']['total_receipts_amount']
    miles_per_day = miles / trip
    spend_per_day = receipts / trip
    records.append({
        'trip_duration_days': trip,
        'miles_traveled': miles,
        'total_receipts_amount': receipts,
        'miles_per_day': miles_per_day,
        'spend_per_day': spend_per_day,
        'miles_bucket': int(miles // 50),
        'receipts_bucket': int(receipts // 50),
        'miles_per_day_bucket': int(miles_per_day // 25),
        'spend_per_day_bucket': int(spend_per_day // 25),
    })
    y.append(d['expected_output'])

X = pd.DataFrame(records)

# Train gradient boosted trees to model reimbursement
model = XGBRegressor(
    max_depth=5,
    n_estimators=300,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    base_score=0
)
model.fit(X, y)

# Export model to plain Python using m2cgen
code = m2c.export_to_python(model)
header = (
    '# Features order: trip_duration_days, miles_traveled, total_receipts_amount, '
    'miles_per_day, spend_per_day, miles_bucket, receipts_bucket, '
    'miles_per_day_bucket, spend_per_day_bucket\n'
)
with open('reimbursement_model_2.py', 'w') as f:
    f.write(header + code)
print('Model exported to reimbursement_model_2.py')
