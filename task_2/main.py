from typing import Callable 
from decimal import Decimal
import re

text = """Загальний дохід працівника складається з декількох частин: 
1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.0 доларів."""

def generator_numbers(text: str):
    # Looking for numbers in provided text and yields each number.
    pattern = r"\s\d+.\d+\s"
    for match in re.finditer(pattern, text):  
        yield match.group()     

def sum_profit(text: str, func: Callable[[str], int]):
    # Summarize all numbers from generator
    total_income = 0
    for income in generator_numbers(text):
        total_income += Decimal(income)     
    return total_income

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
