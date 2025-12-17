d1 = {
    'simplekey' :'Hello'
}

d2 = {
    'k1':{
        'k2':'hello'
        }
    }

d3 = {
    'k1':[{'nest_key':['this is deep',['hello']]}]  
    }

print(d1.values())
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])




