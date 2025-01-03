import sys

def error_message_details(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "error is seen here in the script with script name [{0}] line number [{1}] error message [{2}]".format()
    file_name.exc_tb.tb_lineno, str(error)
    return error_message


class CustomException(Exception):
    def _init_(self,error_message,error_details:sys):
        super._init_(error_message)
        self.error_message = error_message_details(error_message,error_details = error_details)

    def _str_(self):
        return self.error_message
