from patterns import csv_utils
from patterns import web_report
from print_reporter import ConsoleReporter, TabsFormatting
CSV_FILE = "../taxi-data.csv"


def main():
    rides = csv_utils.parse_file(CSV_FILE)
    html_report = web_report.create_content(rides)
    web_report.create_file(html_report)


if __name__ == '__main__':
    rides = csv_utils.parse_file(CSV_FILE)
    html_report = web_report.create_content(rides)

    # Use the ConsoleReporter to display the HTML content in the console
    ConsoleReporter.set_formatting_strategy(TabsFormatting())
    ConsoleReporter.display_report(html_report)