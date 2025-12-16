from fetch_emails import fetch_reports
from process_reports import clean_and_merge_reports
from send_email import send_report

def run_workflow():
    print("=== Fetching outlet reports ===")
    folder = fetch_reports()

    print("=== Cleaning and merging reports ===")
    report_file = clean_and_merge_reports(folder)

    print("=== Sending final report to GM ===")
    send_report(report_file)

    print("=== WORKFLOW COMPLETED SUCCESSFULLY ===")


if __name__ == "__main__":
    run_workflow()
