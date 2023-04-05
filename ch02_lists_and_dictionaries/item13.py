def generate_csv():
    yield ("Date", "Make", "Model", "Year", "Price")
    for i in range(100):
        yield ("2019-03-25", "Honda", "Fit", "2010", "$3400")
        yield ("2019-03-26", "Ford", "F150", "2008", "$2400")


it = generate_csv()
header, *rows = it
print(f"CSV Header: {header}")  # CSV Header: ('Date', 'Make', 'Model', 'Year', 'Price')
print(f"Row count: {len(rows)}")  # Row count: 200
