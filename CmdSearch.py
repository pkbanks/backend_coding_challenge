import sys
import duckduckgo
import json



total = len(sys.argv)

cmdargs = str(sys.argv)


print("the toal args: %d" % total)
print("Args list: %s " % cmdargs)


#Duck-Duck-Go





r = duckduckgo.query(sys.argv[1])

r.type

print("Results list: %s " % r.results)

print("Abstract list: %s " % r.abstract)

#PlaceHolder
resultsStr = ""

for x in r.results:
    resultsStr = resultsStr + '{"title": "'+ str(r.results[0].text) +'", "url": "'+r.results[0].url+'", "desc": "'+r.heading+'"}'




jData = '{"search_term": "'+ sys.argv[1] +'","result_count": "'+ str(len(r.results)) +'","results": ['+ resultsStr +']}'

jObj = json.loads(jData)

print(jObj)


