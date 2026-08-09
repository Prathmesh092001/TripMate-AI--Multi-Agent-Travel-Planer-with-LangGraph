from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

res = search_flights("Plan a 7 days Switzerland trip from India")
print(res)

#res = tavily_search("Best places to visit in Paris")
#print(res)