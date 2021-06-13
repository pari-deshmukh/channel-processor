"""
Channel Processing System:
A Python utility to augment measured performance data and calculate metrics.
"""
import argparse


class ChannelProcessor:
    """
    The ChannelProcessor class defines methods to read, write and process
    channel data to calculate metrics.
    """

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


if __name__ == "__main__":
    processor = ChannelProcessor()
    files = processor.parse_args()
    channels_list = processor.read_channels(files.channels_file)
    for ch_name, ch_data in channels_list.items():
        processor.write_channels(
            ch_name, channels_list[ch_name], files.channels_file)
