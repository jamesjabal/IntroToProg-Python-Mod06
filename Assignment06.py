# --------------------------------------------------------------------------- #
# Title: Assignment06
# Desc: This assignment demonstrates using classes, functions, and separation
#       of concerns.
# Change Log: (Who, When, What)
#   James Jabal,8/14/2025,Created Script. Add FileProcessor & IO classes.
#                         Add revised descriptive class docstrings from Demo04.
#   James Jabal,8/15/2025,Move code inside functions. Add static methods.
#                         Simplified Error Handling with function calls.
#                         Use local variables inside functions.
#                         Add a returned value for input_student_data
#                         Renamed local variables: new_student & student_row
#   James Jabal,8/18/2025,Add returned data types for all functions.
#   James Jabal,8/19/2025,Reformatted code & comments for readability
#   James Jabal,8/20/2025,Use a constant for repeated error message
#                        ,Add parameters with arguments to function calls
#                        ,Add test for a successful write operation
# --------------------------------------------------------------------------- #
import json
import io as _io


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
NON_SPEC_ERROR_MESSAGE: str = "There was a non-specific error!"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.
success: bool = False  # Holds success boolean of file write operation


class FileProcessor:
    """
    A collection of functions that perform File Processing

    ChangeLog: (Who, When, What)
    James Jabal,8/14/2025,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list) -> list:
        """ This function reads data from file

        ChangeLog: (Who, When, What)
        James Jabal,8/15/2025,Created function
        James Jabal,8/19/2025,Add return type
        James Jabal,8/20/2025,Use global constant for repeated error message

       :param file_name: string of the file name
       :param student_data: list of student data
       :return: list of student data
        """

        file = _io.TextIOWrapper  # Defined inside method to allow file closing

        # Read the file data into a dictionary
        # Extract the data from the file
        try:
            file = open(file_name, "r")
            student_data = json.load(file)  # load JSON into a list
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running "
                                     "this script!", e)
        except Exception as e:
            IO.output_error_messages(NON_SPEC_ERROR_MESSAGE, e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list) -> bool:
        """ This function write data to file

        ChangeLog: (Who, When, What)
        James Jabal,8/15/2025,Created function
        James Jabal,8/19/2025,Add return type.
        James Jabal,8/20/2025,Use global constant for repeated error message
                             ,Add boolean status of successful write operation

       :param file_name: string of the file name
       :param student_data: list of student data
       :return: boolean status of successful write operation
        """

        file = _io.TextIOWrapper  # Defined inside method to allow file closing

        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=4)
            file.close()
            return True
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid "
                                     "JSON format", e)
        except Exception as e:
            IO.output_error_messages(NON_SPEC_ERROR_MESSAGE, e)
        finally:
            if file.closed == False:
                file.close()
        return False


class IO:
    """
    A collection of functions that present or gather user input and output

    ChangeLog: (Who, When, What)
    James Jabal,8/14/2025,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None) -> None:
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        James Jabal,8/15/2025,Created function
        James Jabal,8/19/2025,Add return type

        :param message: Custom Error Message
        :param error: Exception
        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str) -> None:
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        James Jabal,8/15/2025,Created function
        James Jabal,8/19/2025,Add return type

        :param menu: Menu string
        :return: None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice() -> str:
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        James Jabal,8/15/2025,Created function
        James Jabal,8/19/2025,Add return type

        :return: string with the users choice
        """
        choice = "0"

        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
            # Not passing the exception object to avoid the technical message
        return choice

    @staticmethod
    def input_student_data(student_data: list) -> list:
        """ This function gets the student data from the user

        ChangeLog: (Who, When, What)
        James Jabal,8/15/2025,Created function
        James Jabal,8/19/2025,Add return type

        :param student_data: list of student data
        :return: list of student data
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            new_student = {"FirstName": student_first_name,
                           "LastName": student_last_name,
                           "CourseName": course_name}
            student_data.append(new_student)  # Appends to passed variable
        except ValueError as e:
            IO.output_error_messages(e.__str__())
            # Not passing the exception object to avoid the technical message
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with "
                                     "your entered data.", e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list) -> None:
        """ This function displays the student courses

        ChangeLog: (Who, When, What)
        James Jabal,8/15/2025,Created function
        James Jabal,8/19/2025,Add return type

        :param student_data: list of student data
        :return: None
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student_row in student_data:
            print(student_row["FirstName"], student_row["LastName"],
                  student_row["CourseName"], sep=",")
        print("-" * 50)


# End of Classes & Functions

# Main Code

# Start by reading JSON file of Enrollments
students = FileProcessor.read_data_from_file(file_name=FILE_NAME,
                                             student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        success = FileProcessor.write_data_to_file(file_name=FILE_NAME,
                                                   student_data=students)
        if success:
            print("Written to File:")
            IO.output_student_courses(student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
