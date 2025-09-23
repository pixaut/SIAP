import json

def readFile(filepath:str)->list:
    
    with open(file = filepath,mode = 'r+',encoding = 'utf-8') as f:
        lines = f.readlines()
    
    companies = list()

    for line in lines:
        parts = line.split()
        companies.append({
            'name' : parts[0],
            'type' : parts[1],
            'up'   : int(parts[2]),
            'down' : int(parts[3])
        }) 

    return companies

def calculateProfit(company:dict) -> float:
    return company['up']-company['down']

def linkCompaniesWithProfit(companies:list)->dict:
    return {company['name'] : calculateProfit(company) for company in companies}

def calculateAverage(companies:list)->float:
    avrg = 0
    [avrg := avrg + calculateProfit(company) for company in companies]
    return avrg/len(companies)

def makeJson(jsonpath:str,companies:list):

    avrg_profit = calculateAverage(companies)
    avrg_profit_dict = {'average_profit': avrg_profit}

    companies_profit_info = [linkCompaniesWithProfit(companies),avrg_profit_dict]

    with open(jsonpath,"w+",encoding='utf-8') as f: 
        json.dump(companies_profit_info, f, ensure_ascii=False, indent=2)



if __name__ == '__main__':
    
    txt_path = 'lab3/text_documents/F5.txt'
    json_path = 'lab3/json_documents/J1.txt'
    
    makeJson (json_path,readFile(txt_path))