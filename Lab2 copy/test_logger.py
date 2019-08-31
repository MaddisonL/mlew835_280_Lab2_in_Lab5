import unittest     # Import the Python unit testing framework
from logger import Logger


class Target:
    def __init__(self):
        self.text = "Put important information here!"
        
        
    def set_info(self,text):
        self.text = text
    
    

class LoggerTest(unittest.TestCase):
    
    def test_info(self):
        my_target  = Target() #Arrange
        my_logger = Logger(target = my_target.set_info)
        
        my_logger.info("Barry!") #Act 
        
        self.assertEqual(my_target.text, "[INFO] Barry!") #Assert
        
        
        
    def test_error(self):
        my_target= Target() #Arrange
        my_logger = Logger(target = my_target.set_info)
        
        my_logger.error("Jerry!") #Act
        
        self.assertEqual(my_target.text,"[WARNING] Jerry!") #Assert
        
        
    
if __name__ == '__main__':
    unittest.main()
    
    