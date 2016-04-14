from user_input import UserInput
import sys

class StartProgram(object):

    def main(argv=None):
        UserInput().take_input()

    if __name__ == "__main__":
        main(sys.argv)
