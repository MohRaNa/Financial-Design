from patterns.csv_utils import Ride
from print_reporter import console_reporter, TabsFormatting

def create_content(rides):
    builder = [_create_headers("Taxi Report"), _create_table_headers()]
    for ride in rides:
        builder.append(_add_ride(ride))
    builder.append(_close_table_headers())

    content = "\n".join(builder)  # Unir con saltos de línea

    console_reporter.set_formatting_strategy(TabsFormatting())
    console_reporter.display_report(content)

    return content

def create_file(content: str):
    with open("financial-report.html", "w") as file:
        file.write(content)


def _create_headers(title: str):
    return f"<h1>{title}</h1>"


def _create_table_headers():
    return """
    <table>
        <tr>
            <th> TaxiID </th>
            <th> Pickup time </th>
            <th> Dropoff time </th>
            <th> Passenger count </th>
            <th> Trip Distance </th>
            <th> Total amount </th>
        </tr>
    """


def _close_table_headers():
    return "</table>"


def _add_ride(ride):
    return "".join([
        "<tr>",
        f"<td>{ride.taxi_id}</td>",
        f"<td>{ride.pick_up_time.isoformat()}</td>",
        f"<td>{ride.drop_of_time.isoformat()}</td>",
        f"<td>{ride.passenger_count}</td>",
        f"<td>{ride.trip_distance}</td>",
        f"<td>{_format_amount(ride.tolls_amount)}</td>",
        "</tr>"
    ])


def _format_amount(amount):
    if amount < 0:
        return f"<span style='color:red'>{amount}</span>"
    return str(amount)
