def calculate_margin(revenue: float, cost: float) -> float:
    if revenue <= 0:
        raise ValueError("Revenue must be greater than zero.")
    return round(((revenue - cost) / revenue) * 100, 2)

if __name__ == "__main__":
    print(f"Margin: {calculate_margin(100, 70)}%")
