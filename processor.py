"""
Channel Processing System:
A Python utility to augment measured performance data and calculate metrics.
"""
import argparse, statistics


class ChannelProcessor:
    """
    The ChannelProcessor class defines methods to read, write and process
    channel data to calculate metrics.
    """

    def __init__(self) -> None:
        self.files = self.parse_args()
        self.metrics = {}
        self.channels_dict = self.read_channels(self.files.channels_file)
        self.parameters_dict = self.read_parameters(self.files.parameters_file)
        self.process_data()
        print("Value of the metric b (mean of Channel B) is %s" % self.metrics['b'])
        
        for ch_name, ch_data in self.channels_dict.items():
            if ch_name != 'X':
                self.write_channels(ch_name, ch_data, self.files.channels_file)

    # Use the argparse module to parse command line input parameters for
    # reading channel and parameter data files. Define channel and parameter
    # data files as required arguments.
    def parse_args(self):
        """
        Defines input arguments, performs syntax checks and parses channel and
        parameter filename arguments. Returns a tuple with the file names.
        """
        file_help_msg = "Relative path to a text file containing"
        program_description = "Channel Processing System"

        # Initialize the argparse parser and set the program description.
        parser = argparse.ArgumentParser(description=program_description)

        # Create a required arguments group for the parser's mandatory
        # arguments.
        required_arguments_group = parser.add_argument_group(
            'required arguments')

        # Add mandatory arguments for relative paths to channel and parameter
        # data files.
        required_arguments_group.add_argument(
            "-c", "--channels-file",
            help=file_help_msg + " channels data.",
            required=True)
        required_arguments_group.add_argument(
            "-p", "--parameters-file",
            help=file_help_msg + " parameters data.",
            required=True)

        # Read arguments from command line.
        return parser.parse_args()

    # Loading up the channels data from the file into the memory for the
    # purposes of this assignment. Loading such data into memory for processing
    # isn't ideal with real world systems.
    def read_channels(self, channels_file):
        """
        Reads channel data from the input file, processes them into a
        dictionary and returns the dictionary of channels.
        """
        # Initialize a blank tuple for storing channel data.
        channels = {}
        # Read through the channels data file and filter out blank lines.
        channel_stream = filter(None, open(
            channels_file, 'r').read().splitlines())
        for line in channel_stream:
            channel_data = line.split(",")
            channel_name = channel_data.pop(0)
            channels[channel_name] = channel_data
        return channels

    def process_data(self):
        X = self.channels_dict['X']
        m = self.parameters_dict['m']
        c = self.parameters_dict['c']
        
        Y = [float(m) * float(X_el) + float(c) for X_el in X]
        A = [1 / float(X_element) for X_element in X]
        B = [float(A_element) + float(Y_element) for A_element, Y_element in zip(A, Y)]
        b = statistics.mean (B)
        C = [float(X_item) + b for X_item  in X]

        self.channels_dict['Y'] = Y
        self.channels_dict['A'] = A
        self.channels_dict['B'] = B
        self.metrics['b'] = b
        self.channels_dict['C'] = C

    def write_channels(self, channel_name, channel_data, channels_file):
        """
        Creates a new channel data entry in the given channels data file.
        """
        with open(channels_file, 'r+') as channel_stream:
            lines = channel_stream.read()
            # Check if the input file is empty or if it doesn't end with a
            # newline entry.
            if len(lines):
                last_line = lines[-1]
                if '\n' not in last_line:
                    channel_name = '\n' + channel_name
            channel_data.insert(0, channel_name)
            channel_stream.write(', '.join('%s' % x for x in channel_data))
            channel_stream.close()

    def read_parameters(self, parameters_file):
        """
        Reads parameters from the input file, processes them into a
        dictionary and returns the dictionary of parameters.
        """
        # Initialize a blank tuple for storing parameters.
        parameters = {}
        # Read through the parameters data file and filter out blank lines.
        parameter_stream = filter(None, open(
            parameters_file, 'r').read().splitlines())
        for line in parameter_stream:
            parameter_data = line.split(",")
            parameter_name = parameter_data.pop(0)
            parameters[parameter_name] = parameter_data.pop(0)
        return parameters


if __name__ == "__main__":
    processor = ChannelProcessor()
