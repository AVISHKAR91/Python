from flask import Flask, render_template, request

# We will have to do pip install requests before trying out this example
import requests

import json

app = Flask(__name__)

@app.route('/convert', methods = ['POST', 'GET'])
def convert() -> 'html':

    ta = 0
    
    try:     
        sc = request.form['source_currency']
        tc = request.form['target_currency']                
        
        sa = int (request.form['source_amount'])
        
        # See https://exchangerate.host/#/ for more details
        
        url = 'https://api.exchangerate.host/latest'        
        
        fullUrl = url + '?base=' + sc + '&symbols=' + tc + '&amount=' + str (sa)        
        
        response = requests.get(fullUrl)
        
        # Will convert the json into a Python dictionary
        response_json = response.json() 
        
        # From the response json dictionary, extract the target amount from the 'rates' key
        print (response_json ['rates'][tc])
        ta = response_json ['rates'][tc]
        	           
    except:
        data = 'Error'
          
    title = 'Here is the result of the conversion:'  
    
    return render_template('result.html', 
                            the_title=title,
                            source_currency=sc,
                            target_currency=tc,
                            source_amount=sa,
                            target_amount=ta,)
    
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':

    currency_dict = {}
    
    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    response_json = response.json()
    
    currencies = response_json ['symbols']
    #print (currency_list)
    
    for key, values in currencies.items():
        #print (values['code'])
        #print (values['description'])
        
        code = values['code']
        description = values['description']
        
        currency_dict[key] = description
        currency_dict[key] = description        
        
    return render_template('entry_dropdown_dict_dynamic_cur.html', the_title='Welcome to our forex calculator!', source_currency_dict = currency_dict, target_currency_dict = currency_dict)    

app.run(debug=True)

