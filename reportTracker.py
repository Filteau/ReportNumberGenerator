from CRUD import ReportCRUD
import datetime 

class ReportTracker:
    def __init__(self):
        self.crud = ReportCRUD('example_db.xlsx')
        self.reportCount = 0

    def get_LocationID(self):
        self.read_info('locationID')
        print("LocationID retrieved: ", self.locationID)
        return self.locationID

    def set_LocationID(self, location_id):
        self.locationID = location_id

    def get_UserID(self):
        self.read_info('userID')
        print("UserID retrieved: ", self.userID)
        return self.userID

    def set_UserID(self, user_id):
        self.userID = user_id

    def get_Date(self):
        now = datetime.datetime.now()
        self.date = now.strftime("%m%y")
        print("Date retrieved: ", self.date)
        return self.date

    def set_Date(self, date_value):
        self.date = date_value

    # Retrieves the latest report number from the database via the CRUD class
    def get_ReportCount(self):
        latest_report = self.crud.read_latest_report()

        # If there's a latest report, extract the date and report number
        if latest_report:
            # Ensure this matches the format of self.get_Date()
            latest_date = str(latest_report.get('Date')).zfill(4)
            print("Latest Date Parsed Value: ", latest_date)
            latest_ReportNum = latest_report.get('ReportNum')
            print("Latest Report Number Parsed Value: ", latest_ReportNum)
            
            current_date = self.get_Date()

            # Compare current date to the latest report date
            if latest_date == current_date:
                # Increment the report number for the current month
                self.reportCount = int(latest_ReportNum) + 1
            else:
                # Reset report number for a new month
                self.reportCount = 1
        else:
            # No previous reports, start with report number 1
            self.reportCount = 1

        return self.reportCount

    def set_ReportCount(self, report_count):
        self.reportCount = report_count

    # Reads from the info.txt file to parse the LocationID and UserID
    def read_info(self, query):
        try:
            with open('info.txt', 'r') as file:
                for line in file:
                    if 'LocationID' in line:
                        self.locationID = line.split('=')[1].strip()
                        if not self.locationID:
                            raise ValueError('LocationID is empty')
                        try:
                            self.locationID = int(self.locationID)
                        except ValueError:
                            raise ValueError('LocationID is not a valid integer')
                    if 'UserID' in line:
                        self.userID = line.split('=')[1].strip()
                        if not self.userID:
                            raise ValueError('UserID is empty')
                        try:
                            self.userID = int(self.userID)
                        except ValueError:
                            raise ValueError('UserID is not a valid integer')
                        
            if self.locationID is None or self.userID is None:
                raise ValueError('LocationID or UserID not found in info.txt')
            
            elif query == 'locationID':
                return self.locationID
            
            elif query == 'userID':
                return self.userID
            
        except FileNotFoundError:
            raise FileNotFoundError('info.txt file not found')
    
    def saveReport(self, report):
        # Split the report string
        locationID, userID, MMYY, reportNum = report.split('-')
        record = {
            'LocationID': int(locationID),
            'UserID': int(userID),
            'Date': MMYY,
            'ReportNum': int(reportNum)
        }
        return self.crud.create_record(record)
    
    # Formats the report number and returns it as a string
    def reportNumberGenerator(self):
        #print("You're in the reportNumberGenerator method")
        locationID = str(self.get_LocationID()).zfill(4)
        userID = str(self.get_UserID()).zfill(4)
        MMYY = self.get_Date()
        reportNum = str(self.get_ReportCount()).zfill(4)
        reportnum = f"{locationID}-{userID}-{MMYY}-{reportNum}"
        reportdb = f"{MMYY}-{reportNum}"
        self.saveReport(reportnum, reportdb)
        return reportnum, reportdb
