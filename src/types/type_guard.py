# type_guard.py
from dataclasses import dataclass

from typeguard import typechecked


@dataclass
class SalesStats:
    total: float
    average: float
    maximum: float


@typechecked
def analyze_sales(amounts: list[float]) -> SalesStats:
    total = sum(amounts)
    return SalesStats(total, total / len(amounts), max(amounts))


print(analyze_sales([100.0, 200.0, 300.0]))
## SalesStats(total=600.0, average=200.0,
## maximum=300.0)

bad_data = [100, "200", 300.0]
try:
    analyze_sales(bad_data)
except TypeError:
    print(f"Bad inputs: {bad_data}")
## Bad inputs: [100, '200', 300.0]
