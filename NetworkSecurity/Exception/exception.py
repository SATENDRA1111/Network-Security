import sys
from NetworkSecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):  ## construction
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info() ## this gives info in which line error occured
        self.line_no=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return "error occured in python script [{0}] line number [{1}] error message [{2}]".format(
            self.file_name,self.line_no,str(self.error_message))
        
        
# if __name__=="__main__":
#     try:
#         logger.logging.info("Enter in try block")
#         a=1/0
#         print('it not print')
#     except Exception as e:
        
#         raise NetworkSecurityException(e,sys)
        