from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib 
from email.mime.text import MIMEText
import pprint, json
import zomatopy
import requests

cities = ['ahmedabad','bengaluru','bangalore', 'chennai','madras', 'delhi','new delhi', 'hyderabad','kolkata', 'culcatta' ,'mumbai','bombay',
          'pune', 'agra', 'ajmer','aligarh', 'amravati','amaravati', 'amritsar','asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'dindugal', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur', 'hubli–dharwad', 'hubli','dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 'kannur', 'kanpur', 'karnal', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool', 'ludhiana', 'lucknow', 'madurai', 'malappuram', 'mathura', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'patna', 'pondicherry', 'purulia prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'surat', 'thanjavur', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 'vasai-virar', 'vijayawada','vijaywada', 'visakhapatnam', 'vellore', 'warangal']


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'


	def fetch(self,loc='banglore',cuisine='north indian',price='high'):
		
		#adjust the price range
		price_min = 0
		price_max = 99999
		if price == 'low':
			price_max = 300
		elif price == 'mid':
			price_min = 300
			price_max = 700
		elif price == 'high':
			price_min = 700
		else:
			price_min = 300
			price_max = 9999
		
		# provide API key and initialise a 'zomato app' object 
		config={ "user_key":"af89b691b36cce036b1ef21d06256163"}  # user key for account phaneendra84@gmail.com
		zomato = zomatopy.initialize_app(config)
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'italian':55,'north indian':50,'south indian':85,'north':50,'south':85,'mexican':73}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		iterator = 1
		if d['results_found'] > 0:
			for restaurant in d['restaurants']:
				if iterator <= 5:
					response = response + "<" + str(iterator) + "> " + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
					iterator = iterator + 1
			return "Below are top restaurants \n\n\n"+ response
		else:
			SlotSet('results_found',False)
			return "No results found for the selected crieteia, please try other options."

		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		if loc == None:
			return dispatcher.utter_message('Foodie chat wants to know the location')
		if loc.lower() not in cities:
			dispatcher.utter_message("We do not operate in that area yet")
			return [AllSlotsReset()]
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		res=''
		if cuisine == None or price == None:  
				dispatcher.utter_message("Please provide cuisine and price details")
		else:
			res = self.fetch(loc,cuisine,price)
			dispatcher.utter_message(res+"\n\n\n")
			 




class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'


	def fetch(self,loc='delhi',cuisine='north indian',price='high'):
		
		#adjust the price range
		price_min = 0
		price_max = 99999
		if price == 'low':
			price_max = 300
		elif price == 'mid':
			price_min = 300
			price_max = 700
		elif price == 'high':
			price_min = 700
		else:
			price_min = 300
			price_max = 9999
		
		# provide API key and initialise a 'zomato app' object
		config={ "user_key":"af89b691b36cce036b1ef21d06256163"}  # user key for account phaneendra84@gmail.com
		zomato = zomatopy.initialize_app(config)
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'italian':55,'north indian':50,'south indian':85,'north':50,'south':85,'mexican':73}        
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 10)
		d = json.loads(results)
		response=""
		iter = 1
		if d['results_found'] == 0:
			return "Sorry !! No restaurants found for the selected crieteia, please try other options."
		else:
			for restaurant in d['restaurants']:
				if iter <= 10:
					response = response + "<" + str(iter) + "> " +  restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address'] + " average budget for two people is " + str(restaurant['restaurant']['average_cost_for_two']) + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
					iter = iter + 1
			return response


	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		response = self.fetch(loc,cuisine,price)
		email = tracker.get_slot('email')
		if email == None:
			dispatcher.utter_message("Please provide the email address")
			return [AllSlotsReset()]
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls() 
		try:
			s.login("phanijamadagni@gmail.com", "hrtkjqpwbbflhwkq") 
		except:
			dispatcher.utter_message('Invalid credentials')
			return [AllSlotsReset()]
		
		message = "Top 10 restaurants you are looking for \n \n"
		message = message + response
                
		try:
			s.sendmail("phanijamadagni@gmail.com", str(email), message)
			s.quit()
			dispatcher.utter_message("Top 10 restaurants has been sent to your email address")
			return [AllSlotsReset()]
		except:
			dispatcher.utter_message("Opps!! Something went wrong while sending email. Please try again later.")
			return [AllSlotsReset()]