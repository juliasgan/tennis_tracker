from user_input import UserInput
import sys


class StartProgram(object):

    def main(argv=None): #command line arguments
        user_input = UserInput()
        user_input.take_input()
        user_input.interface.mainloop()


    if __name__ == "__main__":
        main(sys.argv) #array or list of all the variables

