
import datetime

print ('Hello there!')
print ('what is your name ? ')
myname=input()
print ('Good to meet you ' + myname)
print ('your year birth')
mybirthyear =input()
current_date = datetime.date.today()
current_year = current_date.year
print ('You are ' + str(int(current_year)-int(mybirthyear)) + 'years old')


