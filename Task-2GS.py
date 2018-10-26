import BeautifulSoup from bs4
import requests
import time

USER_AGENT = { "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0" }

def SearchRes ( key ,  number ) :
	assert isinstance ( key, str ), "Search term must be a string."
	assert isinstance ( number, int ), "Number should be an integer."
	new_key = key.replace ( " " , "+" )
	url = "https://www.google.com/search?q={}&num={&hl={}".format( new_key , number )
	resp = requests.get( url , headers = USER_AGENT )
	resp.raise()
	resp_text = resp.text
	return resp_text
	
def ParseRes ( ResCode ) : 
	soup = BeautifulSoup ( ResCode, "html5lib" )
	search_res=[]
	rank = 1
	res_par = soup.find_all( "div" , { class : "g" }
	for res in res_par:
		link = res.find("a")
		title = res.find("h3")
		body = res.find("span")
		if ( link and title ) :
			link = link["href"]
			title = title.text()
		if ( body ) :
			body = body.get_text()
		if ( link != "#" ) :
			search_res.append( { "rank" : rank , "title" : title , "body" : body , "link" = link } )
		rank += 1
		return search_res
	
def Plag_Check ( key , number ) :
	try :
		ResCode = SearchRes ( key , number )
		res = ParseRes( ResCoce)
        return results
    except AssertionError:
        raise Exception( "Incorrect arguments parsed to function" )
    except requests.HTTPError:
        raise Exception( "You appear to have been blocked by Google" )
    except requests.RequestException:
        raise Exception( "Appears to be an issue with your connection" )

if __name__=="__main__" : 
	key = input()
	#f = open ("file.txt" , "w" )
	#f.(key.split())
	#f.close()
	data = []
	for k in key : 
		try:
			res1 = Plag_Check ( "file.txt" )
			for res2 in res1  :
				data.append(res1)
		except Exception as e :
			print ( e )
	print ( data )						

