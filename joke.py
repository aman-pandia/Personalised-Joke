import requests

def getjoke():
	api_url = 'http://api.icndb.com/jokes/random/'
	
	while True:
		name = input('Enter name : ')
		fname, lname = name.split()

		parametersObject = {
		    'firstName' : fname,
		    'lastName' : lname
		}

		resp = requests.get(url=api_url,params=parametersObject)

		jokeObj = resp.json()

		print(jokeObj['value']['joke'])
		print()
		print()

if __name__ == '__main__':
	try:
		print('Welcome to personalised jokes press Ctrl+C to exit')
		print()
		getjoke()
	except KeyboardInterrupt:
		print('Byee..Keep coming for the jokes XD')
