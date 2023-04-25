import arrow


def date_difference(date1: str, date2: str) -> str:
    arrow_date1 = arrow.get(date1, "YYYY-MM-DD")
    arrow_date2 = arrow.get(date2, "YYYY-MM-DD")

    human_readable_diff = arrow_date2.humanize(
        arrow_date1, granularity=["year", "month", "day"]
    )

    return human_readable_diff


if __name__ == "__main__":
    date1 = "2021-01-01"
    date2 = "2023-04-25"
    result = date_difference(date1, date2)
    print(f"The difference between {date1} and {date2} is {result}.")
