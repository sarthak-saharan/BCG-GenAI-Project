import warnings
import pandas as pd


warnings.filterwarnings('ignore')


df = pd.read_csv('/Users/sarthak.saharan/Documents/BCG Project/Final.csv')

df = df.dropna()

df['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income'].pct_change() * 100

df['Profit Margin'] = df['Net Income'] / df['Total Revenue']

df['Debt-to-Equity Ratio'] = df['Total Liabilities'] / (df['Total Assets'] - df['Total Liabilities'])

financial_data = df.to_dict('list')

def respond_to_query(query):

    if extract_company(query) is None:
        return f"Please mention Company name"

    if extract_year(query) is None:
        return f"Please mention year"
        
    if "total revenue" in query:
        company = extract_company(query)
        year = extract_year(query)
        revenue = query_total_revenue(company, year)
        return f"The total revenue for {company} in {year} was {revenue}."
    
    elif "net income" in query:
        company = extract_company(query)
        year = extract_year(query)
        net_income = query_net_income(company, year)
        return f"The net income for {company} in {year} was {net_income}."
    
    elif "trend of net income" in query:
        company = extract_company(query)
        year = extract_year(query)
        trend_data = query_net_income_trend(company,year)
        return f"The trend of net income for {company} over the years is as follows: {trend_data}"
    
    elif "profitability metrics" in query:
        company = extract_company(query)
        year = extract_year(query)
        profitability_metrics = query_profitability_metrics(company,year)
        return f"The profitability metrics for {company} are as follows: {profitability_metrics}"
    
    else:
        return "Sorry, I couldn't understand your query."

def extract_company(query):
    company_names = ['Microsoft', 'Apple', 'Tesla']
    for company in company_names:
        if company.lower() in query.lower():
            return company

def extract_year(query):
    years = ['F21', 'F22', 'F23']
    for year in years:
        if year in query:
            return year

# Example querying functions
def query_total_revenue(company, year):
    return df[(df['Company'] == company )&(df['Year'] == year)]['Total Revenue'].values[0] 

def query_net_income(company, year):
    return df[(df['Company'] == company )&(df['Year'] == year)]['Net Income'].values[0]

def query_net_income_trend(company,year):
    return df[(df['Company'] == company )&(df['Year'] == year)]['Net Income Growth (%)'].values[0]

def query_profitability_metrics(company,year):
    return df[(df['Company'] == company )&(df['Year'] == year)]['Profit Margin'].values[0]

user_query = input("Please enter your query: ")
response = respond_to_query(user_query)
print(response)
