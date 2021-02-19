import csv
import os
from datetime import datetime, date

class Weather:

    data_path = os.path.join(os.getcwd(), 'data')

    data_sources = [
        'temperature',
        'precipitation',
        'sight',
        'wind'
    ]

    def __init__(self):
        self.data = {}
        self._loadCSVs()

    def _loadCSVs(self):
        """
        Load data from csv files, save in dictionary
        """
        for source in self.data_sources:
            with open(os.path.join(self.data_path, source + '.csv')) as file:
                # Ignore first row
                file.readline()

                # Read the entire file
                reader = csv.reader(file, delimiter=';')

                # Loop every row
                for row in reader:
                    # Create a datetime from the two first columns
                    dt = datetime.strptime(row[0] + row[1], '%Y-%m-%d%H:%M:%S')
                    date = dt.date()
                    time = dt.time()

                    # Create date key if not exists
                    if(date not in self.data):
                        self.data[date] = {}
                    # Create time key if not exists
                    if(time not in self.data[date]):
                        self.data[date][time] = {}
                    
                    # Save data in correct key (source)
                    self.data[date][time][source] = row[2:]
    
    def getData(self, date = None, time = None, source = None):
        """
        Get data from the sources

        Args:
            date: Which date to get data from
            time Which time to get data from
            source: Which source to get data from
        
        Returns:
            The requested data
        """
        if(date is not None):
            if(date not in self.data):
                return None
            if(time is not None):
                if(time not in self.data[date]):
                    return None
                if(source is not None):
                    if(source not in self.data[date][time]):
                        return None
                    return self.data[date][time][source]
                return self.data[date][time]
            return self.data[date]
        return self.data