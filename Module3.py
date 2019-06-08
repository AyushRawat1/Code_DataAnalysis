import pandas as pd  
from apyori import apriori 

store_data = pd.read_csv('Market_Basket_Optimisation.csv', header=None) 

store_data.head() 

records = []  

for i in range(0, 7501):  
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])

rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)  

results = list(rules)

results_list_1 = []
results_list_2 = []
results_list_3 = []

for i in range(0, len(results)):   

    results_list_1.append('RULE:\t' + str(results[i][0]) + '\nSUPPORT:\t' + str(results[i][1]))
    
    results_list_2.append('RULE:\t' + str(results[i][0]) + '\nCONFIDENCE:\t' + str(results[i][1]))
    
    results_list_3.append('RULE:\t' + str(results[i][0]) + '\nLIFT:\t' + str(results[i][1]))



for item in rules:
    
 
    pair = item[0]
    
    items = [x for x in pair]
    
    print("Rule: " + items[0] + " -> " + items[1])

    print("Support: " + str(item[1]))



    print("Confidence: " + str(item[2][0][2]))
    
    print("Lift: " + str(item[2][0][3]))
    
    print("=====================================")
    