"""
This file creates a basic dataset that will be used to introduce various
concepts of the Python programming language, the Numpy library, the Pandas
library.

Additionally, this dataset will be visualized using the Matplotlib library.
Finally, this script is an example of good software craftmanship.

Example usage:
$python create_dataset.py -nr 5 -nc 2
"""
import argparse
import random

DEFAULT_NROWS = 10
DEFAULT_NCOLS = 10
DEFAULT_FILENAME = 'basics_dataset.txt'
DEFAULT_DELIMITER = ','
DEFAULT_HEADER = "Sample Dataset"
DEFAULT_COMMENT_CHAR = "#"


def create_dataset(nrows, ncols, filename, delimiter, header, comment_char):
    """
    This function creates an example dataset. The name and contents of the file
    are based on the arguments to the function.

    Note that the data itself is randomly generated.
    """
    with open(filename, mode='w') as file_obj:
        if header is not None:
            file_obj.write(f"{comment_char} {header} \n")
        for row in range(nrows):
            file_obj.write(f"{row}")
            for col in range(ncols):
                file_obj.write(f"{delimiter}{random.randint(0, 100)}")
            file_obj.write("\n")


def parse_cmd_line_args():
    """
    This function parses the command line arguments passed when running the
    script.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-nr', '--nrows', type=int, default=DEFAULT_NROWS,
        help="number of rows in dataset"
    )
    parser.add_argument(
        '-nc', '--ncolumns', type=int, default=DEFAULT_NCOLS,
        help="number of columns in dataset"
    )
    parser.add_argument(
        '--filename', type=str, default=DEFAULT_FILENAME,
        help="dataset filename"
    )
    parser.add_argument(
        '--delimiter', type=str, default=DEFAULT_DELIMITER,
        help="dataset delimiter"
    )
    parser.add_argument(
        '--header', type=str, default=DEFAULT_HEADER,
        help="dataset header info"
    )
    parser.add_argument(
        '--comment-char', type=str, default=DEFAULT_COMMENT_CHAR,
        help="comment character used in dataset"
    )
    args = parser.parse_args()
    return (args.nrows, args.ncolumns, args.filename, args.delimiter,
            args.header, args.comment_char)


if __name__ == "__main__":
    args = parse_cmd_line_args()
    create_dataset(*args)

