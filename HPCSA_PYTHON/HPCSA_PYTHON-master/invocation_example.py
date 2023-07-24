#import trial
from trial import my_print,my_logic

m_source = input("Pleased enter the source ")
m_destination = input("Pleased enter the destination ")
m_fare = float(input("Pleased enter the fare "))
m_discount_rate = float(input("Pleased enter the discount_rate in percentage "))

my_print(my_logic(m_source,m_destination,m_fare,m_discount_rate))
