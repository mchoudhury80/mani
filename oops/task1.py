import logging
#logging.basicConfig(filename="stringUtility.log", level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class StringUtilities:
    """This program is Oops concept using old tasks as Sudhansu sir said"""
    def extract_data(self ,s):
        """TASK-1's task
         1 . Try to extract data from index one to index 300 with a jump of 3
        :param s: input string
        :return: slices the string s with a step of 3 and starting point of 1, ending point of 300
        """
        try:
            logging.info("The given string for this operation is %s" , s)
            s1 = s[1:300:3]
            logging.info("The output of this operation is %s" , s1)
            return s1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n"+ str(e))

    def reverse_string(self, s):
        """TASK-1's task
        2 . Try to reverse a string without using reverse function
        :param s: input string
        :return: reverses the given string"""
        try:
            logging.info("The given string for this operation is %s", s)
            s2 = s[::-1]
            logging.info("The output of this operation is %s", s2)
            return s2
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))


    def split_uppercase_string(self,s):
        """TASK-1's task
        3 . Try to split a string after conversion of entire string in uppercase
        :param s: input string
        :return: it returns a list of string. which were converted to uppercase and then splitted using split()
        """
        try:
            logging.info("The given string for this operation is %s", s)
            s3 = s
            s4 = s3.upper().split(' ')
            logging.info("The output of the operation is %s", s4)
            return s4
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))


    def conversion_to_lower_string(self,s):
        """TASK-1's task
        4 . try to convert the whole string into lower case
        :param s: input string
        :return: return the given string with all characters in lowercase"""
        try:
            logging.info("The given string for this operation is %s", s)
            s5 = s
            s6 = s5.lower()
            logging.info("The out put of the operation is %s",s6)
            return s6
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))


    def convert_capital_to_string(self,s):
        """TASK-1's task
        5 . Try to capitalize the whole string
        :param s: input string
        :return: return the given string in capitalize form"""
        try:
            logging.info("The given string for this operation is %s", s)
            s7 = s
            s8 = s7.capitalize()
            logging.info("The output of the operation is %s", s8)
            return s8
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))


    def expandtab_of_string(self,s):
        """TASK-1's task
        6. Try to give an example of expand tab"""
        try:
            logging.info("The given string for this operation is %s", s)
            s9 = s
            s10 = s9.expandtabs()
            logging.info("The output of the operation is %s", s10)
            return  s10
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))


    def strip_the_string(self,s):
        """TASK-1's task
        7. Give an example of strip
        :param s: input string
        :return: returns the given string with tab spaces"""
        try:
            logging.info("The given string for this operation is %s", s)
            s11 = s
            s12 = s11.strip()
            logging.info("The output of the operation is %s", s12)
            return s12
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))


    def lstrip_the_string(self,s):
        """ TASK-1's task
        8. Give an example of lstrip
        :param s: input string
        :return: returns the given string with stripping the extra spaces present on its left and right side"""
        try:
            logging.info("The given string for this operation is %s", s)
            s13 = s
            s14 = s13.lstrip()
            logging.info("The output of the operation is %s", s14)
            return s14
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))


    def rstrip_the_string(self,s):
        """ TASK-1's task
        9. Give an example of rstrip
        :param s: input string
        :return: returns the given string with stripping the extra spaces present on its right side"""
        try:
            logging.info("The given string for this operation is %s", s)
            s15 = s
            s16 = s15.rstrip()
            logging.info("The output of the operation is %s", s16)
            return s16
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))


    def replacing_a_string(self,s,pr ,tr):
        """ TASK-1's task
        10.  Replace a string charecter by another charector by taking your own example
        :param s: input a string
        :param pr: the part we want to replace
        :param tr: with what we want to replace
        :return:"""
        try:
            logging.info("The given string for this operation is %s", s)
            s17 = s
            s18 = s17.replace(pr,tr)
            logging.info("The output of the operation is %s", s18)
            return s18
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))




obj1 = StringUtilities()

str1 = obj1.extract_data("This is my first python program and i am learning oops concept using string function")
logging.info(str1)

str2 = obj1.reverse_string("This is my first python program and i am learning oops concept using string function")
logging.info(str2)

str4 = obj1.split_uppercase_string("This is my first python program and i am learning oops concept using string function")
logging.info(str4)

str6 = obj1.conversion_to_lower_string("This is my first python program and i am learning oops concept using string function")
logging.info(str6)

str8 = obj1.convert_capital_to_string("This is my first python program and i am learning oops concept using string function")
logging.info(str8)

str10 = obj1.expandtab_of_string("This\tis\tmy\tfirst\tpython\tprogram\tand\ti\tam\tlearning\toops\tconcept\tusing\tstring\tfunction")
logging.info(str10)

str12 = obj1.strip_the_string("This is my first python program and i am learning oops concept using string function")
logging.info(str12)

str14 = obj1.lstrip_the_string("This is my first python program and i am learning oops concept using string function")
logging.info(str14)

str16 = obj1.rstrip_the_string("This is my first python program and i am learning oops concept using string function")
logging.info(str16)

str18 = obj1.replacing_a_string("This is my first python program and i am learning oops concept using string function", "first","second")
logging.info(str18)
