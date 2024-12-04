import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #from exc_info we are only interested in exc_tb
    file_name = exc_tb.tb_frame.f_code.co_filename #extract file_name from exc_tb
    #show error message in understandable format with place holders.
    error_message="Error occured in Python Script name[{0}] line number [{1}] error message[{2}]".format(
    file_name, exc_tb.tb_lineno, str(error)

    return error_message
    )

#Whenever custom exception is raised, first of all it inherits parent exception.
#---We will initialize the custom exception variable i.e. error_message. and error_detail is tracked by sys.
class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys): #constructor
        super.__init__(error_message) #inherit the init function
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    #Inherit str functionality to print error message.
    def __str__(self):
        return self.error_message
    
    