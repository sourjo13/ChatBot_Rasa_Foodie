
## interactive_story_1
* goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* goodbye

## interactive_story_3
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* goodbye
    - action_restart

## interactive_story_5
* greet
    - utter_greet
* not
    - utter_goodbye
    - action_restart

## interactive_story_6
* goodbye
    - action_restart

## interactive_story_7
* goodbye
    - action_restart

## interactive_story_8
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* location{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bengaluru"}
    - utter_request_email
* not
    - utter_goodbye
    - action_restart

## interactive_story_9
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"got_all": "yes"}
* affirm
    - utter_request_email
* email{"email": "phanijamadagni@gmail.com"}
    - slot{"email": "phanijamadagni@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_10
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"got_all": "yes"}
    - utter_email_prompt
* affirm
    - utter_request_email
* not
    - utter_goodbye
    - action_restart

## interactive_story_11
* restaurant_search{"cuisine": "chinese", "location": "bengaluru"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"got_all": "yes"}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "bharadwaj05@gmail.com"}
    - slot{"email": "bharadwaj05@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_13
* restaurant_search{"price": "low", "cuisine": "north indian", "location": "new delhi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "new delhi"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* not{"not": "no"}
    - utter_goodbye
    - action_restart

## interactive_story_14
* restaurant_search{"price": "low", "location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "phaneendra84@gmail.com"}
    - slot{"email": "phaneendra84@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_15
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_16
* restaurant_search{"cuisine": "italian", "location": "dharmavaram"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavaram"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_17
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
* goodbye
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "test123@gmail.com"}
    - slot{"email": "test123@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_18
* restaurant_search{"price": "low", "cuisine": "italian", "location": "Delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Delhi"}
    - slot{"price": "low"}
    - action_search_restaurants
* goodbye
    - utter_email_prompt
* email{"email": "jain@yahoo.com"}
    - slot{"email": "jain@yahoo.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_19
* restaurant_search{"price": "high", "location": "Delhi"}
    - slot{"location": "Delhi"}
    - slot{"price": "high"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bengaluru"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
* restaurant_search
    - utter_request_email
* email{"email": "someone@outlook.com"}
    - slot{"email": "someone@outlook.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_21
* restaurant_search{"price": "high", "location": "dharmavaram"}
    - slot{"location": "dharmavaram"}
    - slot{"price": "high"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_22
* restaurant_search{"price": "low", "cuisine": "italian", "location": "bengaluru"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bengaluru"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_23
* greet
    - utter_greet
* restaurant_search
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "happyman@gmail.com"}
    - slot{"email": "happyman@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_24
* greet
    - utter_greet
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
* not

## interactive_story_25
* restaurant_search{"price": "high", "cuisine": "indian", "location": "jaipur"}
    - slot{"cuisine": "indian"}
    - slot{"location": "jaipur"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_26
* greet
    - utter_greet
* goodbye
    - action_restart

## interactive_story_27
* greet
    - utter_greet

## interactive_story_28
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* location{"location": "jalandhar"}
    - slot{"location": "jalandhar"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "anjali@upgrad.com"}
    - slot{"email": "anjali@upgrad.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_29
* restaurant_search{"price": "low", "cuisine": "italian", "location": "warangal"}
    - slot{"cuisine": "italian"}
    - slot{"location": "warangal"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "abbas12@yahoo.com"}
    - slot{"email": "abba12s@yahoo.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_30
* restaurant_search{"price": "low", "cuisine": "american"}
    - slot{"cuisine": "american"}
    - slot{"price": "low"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_31
* restaurant_search{"cuisine": "italian", "location": "mysore"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mysore"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - reset_slots
    - utter_email_prompt
* email{"email": "admin@upgrad.com"}
    - slot{"email": "admin@upgrad.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_32
* restaurant_search{"price": "high", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - action_search_restaurants
    - slot{"location": "jodhpur"}
    - slot{"price": "high"}
    - slot{"cuisine": "italian"}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "email567@gmail.com"}
    - slot{"email": "email567@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_33
* restaurant_search{"cuisine": "italian", "location": "bengaluru"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bengaluru"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "manju_846@gmail.com"}
    - slot{"email": "manju_846@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_34
* restaurant_search{"cuisine": "italian", "location": "chikmagalur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavram"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location_valid": "not"}

## interactive_story_35
* restaurant_search{"cuisine": "italian", "location": "chikmagalur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavram"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location_valid": "not"}

## interactive_story_36
* restaurant_search{"cuisine": "italian", "location": "chikmagalur"}
    - slot{"cuisine": "italian"}
    - slot{"location": "chikmagalur"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_37
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "amritsar"}
    - slot{"location": "amritsar"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_38
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_39
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "phani@gmail.com"}
    - slot{"email": "phani@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_40
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "phaneendra84@gmail.com"}
    - slot{"email": "phaneendra84@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_41
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - action_restart

## interactive_story_42
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_43
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "culcutta"}
    - slot{"location": "culcutta"}
    - utter_ask_cuisine
* cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_44
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}

## interactive_story_45
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* location{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - utter_email_prompt
* not{"not": "never"}
    - utter_goodbye
    - action_restart

## interactive_story_46
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "ramya@yahoo.com"}
    - slot{"email": "ramya@yahoo.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_47
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_48
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "indore"}
    - slot{"location": "indore"}
    - utter_ask_cuisine
* cuisine{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_49
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "italian", "location": "mysore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "jodhpur"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_50
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "mexican", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "phaneendra84@gmail.com"}
    - slot{"email": "phaneendra84@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart
