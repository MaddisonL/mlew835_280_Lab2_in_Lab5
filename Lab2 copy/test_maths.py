import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function.  '''
        
        positive_integer1 = 12 #Arrange
        positive_integer2 = 5
        
        rational_number1 = 1.5
        rational_number2 = 0.5
        
        positive_sum = maths.add(positive_integer1, positive_integer2)#Act
        rational_sum = maths.add(rational_number1,rational_number2)
        
        self.assertEqual(positive_sum, 17) #Assert
        self.assertEqual(rational_sum, 2.0)
       
        
    def test_add_convert(self):
        
        'Tests the conversion functionality of the add function.'
        
        to_binary1 = 4 #Arrange
        to_binary2 = 12
        
        to_hex1 = 16
        to_hex2 = 6
        
        binary_sum = maths.add(to_binary1, to_binary2, 2) #Act
        hex_sum = maths.add(to_hex1,to_hex2, 16)
        
        self.assertEqual(binary_sum,"10000") #Assert
        self.assertEqual(hex_sum, "16")
        

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        
        sequence_number = 5 #Arrange
        input_result = maths.fibonacci(sequence_number) #Act
        self.assertEqual(input_result,5) #Assert
        
        
    
    def test_convert_base(self):
        ''' Tests the convert_base function.'''
        
        to_convert_binary = 9 #Arrange
        to_convert_hexidecimal = 22
         
        binary_convert = maths.convert_base(to_convert_binary, 2) #Act
        hex_convert = maths.convert_base(to_convert_hexidecimal,16)
        
        self.assertEqual(binary_convert, "1001") #Assert
        self.assertEqual(hex_convert, "16")
        
    

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
