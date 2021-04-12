import requests
import json

class Client:
	def __init__(self, url, apikey):
		self.url = url
		self.apikey = apikey

	# Account information
	def getUserId(self):
		url = f'{self.url}/api/client/account'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return str(resp["attributes"]["id"])

	def getUsername(self):
		url = f'{self.url}/api/client/account'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return str(resp["attributes"]["username"])

	def getEmail(self):
		url = f'{self.url}/api/client/account'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return str(resp["attributes"]["email"])

	def getFirstname(self):
		url = f'{self.url}/api/client/account'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return str(resp["attributes"]["first_name"])

	def getLastname(self):
		url = f'{self.url}/api/client/account'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return str(resp["attributes"]["last_name"])

	def getLanguage(self):
		url = f'{self.url}/api/client/account'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return str(resp["attributes"]["language"])

	def isUserAdmin(self):
		url = f'{self.url}/api/client/account'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return bool(resp["attributes"]["admin"])

	# Account
	def updateEmail(self, email, password):
		url = f'{self.url}/api/client/account/email'
		headers = {
		    "Authorization": f"Bearer {self.apikey}",
		    "Accept": "application/json",
		    "Content-Type": "application/json",
		    "cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}
		payload = f'''{{
			"email": "{email}",
			"password": "{password}"
		}}'''

		response = requests.request('PUT', url, data=payload, headers=headers)
		if response.text != "":
			resp = json.loads(response.text)
			return resp["errors"][0]["code"]
		else:
			return None

	def updatePassword(self, currentPassword, newPassword, newPasswordConfirmation):
		url = f'{self.url}/api/client/account/password'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}
		payload = f'''{{
			"current_password": "{currentPassword}",
			"password": "{newPassword}",
			"password_confirmation": "{newPasswordConfirmation}"
		}}'''

		response = requests.request('PUT', url, data=payload, headers=headers)
		if response.text != "":
			resp = json.loads(response.text)
			return resp["errors"][0]["code"]
		else:
			return None

	def createApiKey(self, description):
		url = f'{self.url}/api/client/account/api-keys'
		headers = {
		    "Authorization": f"Bearer {self.apikey}",
		    "Accept": "application/json",
		    "Content-Type": "application/json",
		    "cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}
		payload = f'''{{
		  "description": "{description}"
		}}'''

		response = requests.request('POST', url, data=payload, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["identifier"]

	def deleteApiKey(self, identifier):
		url = f'{self.url}/api/client/account/api-keys/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('DELETE', url, headers=headers)
		if response.text != "":
			resp = json.loads(response.text)
			return resp["errors"][0]["code"]
		else:
			return None

	# ---
	# Server
	# ---

	# Server information
	def isUserServerOwner(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["server_owner"]

	def getServerIdentifier(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["identifier"]

	def getServerUuid(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["uuid"]

	def getServerName(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["name"]

	def getServerNode(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["node"]

	def getServerSftpIp(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["sftp_details"]["ip"]

	def getServerSftpPort(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["sftp_details"]["port"]

	def getServerDescription(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["description"]

	def getServerMemory(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["limits"]["memory"]

	def getServerSwap(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["limits"]["swap"]

	def getServerDisk(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["limits"]["disk"]

	def getServerIo(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["limits"]["io"]

	def getServerCpu(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["limits"]["cpu"]

	def getServerDatabaseLimit(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["feature_limits"]["databases"]

	def getServerAllocationLimit(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["feature_limits"]["allocations"]

	def getServerBackupLimit(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["feature_limits"]["backups"]

	def isServerSuspended(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["is_suspended"]

	def isServerInstalling(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["is_installing"]

	def getServerState(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}/resources'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["current_state"]

	def getServerMemoryUsage(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}/resources'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return int(resp["attributes"]["resources"]["memory_bytes"])

	def getServerCpuUsage(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}/resources'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return resp["attributes"]["resources"]["cpu_absolute"]

	def getServerDiskUsage(self, identifier):
		url = f'{self.url}/api/client/servers/{identifier}/resources'
		headers = {
			"Authorization": f"Bearer {self.apikey}",
			"Accept": "application/json",
			"Content-Type": "application/json",
			"cookie": "pterodactyl_session=eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%253D%253D"
		}

		response = requests.request('GET', url, headers=headers)
		resp = json.loads(response.text)
		return int(resp["attributes"]["resources"]["disk_bytes"])