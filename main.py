from reportTracker import ReportTracker

def main():
    # Create an instance of ReportTracker
    tracker = ReportTracker()
    
    # Call the reportNumberGenerator method to generate a report
    report = tracker.reportNumberGenerator()
    
    # Print the generated report
    print(report)

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()
