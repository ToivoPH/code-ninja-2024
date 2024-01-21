import os
import json

"""

Pt 1
Purpose of this exericse is to get all the relevant filepaths using the OS library.
By using os function and relative path, we get both the data folder and the output folder (results)

This task will introduce the OS function and apply the idea of current working directory, and glob function(challenge)
Functions & concetps to use:
os.join()
os.getcwd()
relative path
glob.glob() challenge*

"""


class ExtractData:

    def __init__(self, path, output_filename=None):

        self.srcdir = path
        self.cwd = None
        self.data = None
        self.filename = output_filename
        self.final = None

    def get_current_working_dir(self):
        """
        return current working directory using pathlib
         - modify code to return the correct output.
        """
        return os.getcwd()
    
    def get_output_dir(self):
        """
        return filepath \results using pathlib
         - modify code to return the correct output.
        """
        return False

    def get_datafile(self, query):
        """
        Challenge:
         return filepath  glob function
         - Use query to select 
         - modify code to return the correct output.
        """
        return False

    def load_data_json(self):
        """
        Get the json filepath and return the data stored in the file
        """
        
        myfile = os.path.join(self.srcdir, 'top-countries-realtime.json')
        with open(myfile) as file:
            self.data = json.load(file)

        return self.data

    def load_data_pandas(self):
        """
        return specified file using pandas library
        """
        return False

    def process_data(self):
        """
        Work out some simple processes and calculations
        """
        return False

    def load_data_text(self):
        """
        load text data
        """
        return False


    def output_file(self, format):
        """
        output format in to the specified data
        """
        if format == '.txt':
            return False

        elif format == '.csv':
            return False

        elif format == '.xlsx':
            return False


if __name__ == "__main__":

    #  Use of relative path
    path = './data'
    ed = ExtractData(path)
    ab = ed.load_data_json()
    print(ab)