import sys
import json
from src.reimbursement import calculate_reimbursement

#!/usr/bin/env python3
"""
Travel Reimbursement Calculator - Reverse Engineered Legacy System

Based on comprehensive analysis of:
- 1,000+ historical input/output cases
- Employee interviews revealing business logic insights
- Pattern analysis showing complex multi-component algorithm

Key discoveries:
- Base per-diem: ~$100/day
- Tiered mileage rates with efficiency bonuses
- Complex receipt processing with caps, boosts, and penalties
- Special 5-day trip logic
- Various edge cases and rounding quirks

Usage: python3 reimbursement_calculator.py <days> <miles> <receipts>
"""

# import sys
# import math

# def calculate_reimbursement(days, miles, receipts):
#     """
#     Calculate travel reimbursement using reverse-engineered legacy system logic

#     Args:
#         days (int): Trip duration in days
#         miles (float): Total miles traveled
#         receipts (float): Total receipt amount in dollars

#     Returns:
#         float: Calculated reimbursement amount rounded to 2 decimal places
#     """

#     # Convert inputs to appropriate types
#     days = int(days)
#     miles = float(miles)
#     receipts = float(receipts)

#     # COMPONENT 1: Base Per Diem (~$100/day)
#     # Lisa from Accounting: "100 a day seems to be the base"
#     total = days * 100

#     # COMPONENT 2: Mileage Component with Tiered Rates
#     # Analysis revealed different rates based on total distance, not simple linear
#     # Lisa: "First 100 miles or so, you get the full rate... After that, it drops"
#     if miles < 100:
#         # Higher rate for short distances
#         total += miles * 0.65
#     elif miles < 600:
#         # Standard rate for medium distances
#         total += miles * 0.42
#     else:
#         # Reduced rate for long distances (diminishing returns)
#         total += miles * 0.28

#     # COMPONENT 3: Receipt Processing (Most Complex Component)
#     # Based on Lisa's insights about caps and Kevin's spending thresholds
#     # "Medium-high amounts—like $600-800—seem to get really good treatment"
#     # "Really low amounts get penalized"

#     if receipts < 10:
#         # Very small receipts get a fixed boost
#         # Lisa: "if you submit $50 in receipts... you're better off submitting nothing"
#         # This handles the penalty by giving a small fixed amount instead
#         total += 45
#     elif receipts < 50:
#         # Small receipts get favorable treatment to avoid penalties
#         total += receipts * 1.3
#     elif receipts < 200:
#         # Moderate receipts get good treatment (Lisa's "sweet spot")
#         total += receipts * 0.85
#     elif receipts < 800:
#         # Higher receipts get reduced treatment (caps kicking in)
#         # Lisa: "Medium-high amounts... get really good treatment"
#         total += receipts * 0.65
#     elif receipts < 1500:
#         # High receipts get further reduced treatment
#         total += receipts * 0.55
#     else:
#         # Very high receipts get heavily capped
#         # "each dollar matters less and less"
#         total += 825 + (receipts - 1500) * 0.35

#     # COMPONENT 4: Special Cases and Bonuses

#     # Kevin's 5-day bonus observation
#     # "5-day trips almost always get a bonus"
#     if days == 5:
#         total += 75

#     # Efficiency bonus for optimal miles/day ratios
#     # Kevin: "sweet spot around 180-220 miles per day"
#     # Marcus: "efficiency bonus theory—that you get extra money for covering lots of ground"
#     miles_per_day = miles / days if days > 0 else 0
#     if 120 <= miles_per_day <= 250:
#         total += 25  # Efficiency bonus for optimal travel efficiency

#     # COMPONENT 5: Rounding Quirks and Edge Cases
#     # Kevin: "if your receipts end in 49 or 99 cents, you often get a little extra money"
#     receipt_cents = round((receipts % 1) * 100)
#     if receipt_cents in [49, 99]:
#         total += 3  # Small rounding quirk bonus

#     # Round to 2 decimal places as per legacy system output format
#     return round(total, 2)


def main():
    """
    Reads trip data from command-line arguments, calculates reimbursement,
    and prints the result.
    """
    try:
        # sys.argv[0] is the script name itself
        trip_duration = int(sys.argv[1])
        miles_traveled = float(sys.argv[2])
        total_receipts = float(sys.argv[3])

        trip_details = {
            "trip_duration_days": trip_duration,
            "miles_traveled": miles_traveled,
            "total_receipts_amount": total_receipts
        }

        reimbursement = calculate_reimbursement(trip_details)

        # The eval script expects a single number as output
        print(reimbursement)

    except (IndexError, ValueError) as e:
        print(f"Error: Invalid or missing command-line arguments. {e}", file=sys.stderr)
        print("Usage: python -m src.main <duration_days> <miles_traveled> <receipts_amount>", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
