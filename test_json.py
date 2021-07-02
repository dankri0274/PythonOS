import json

data = {
	"president": {
		"name": "Daniel Kristensen",
		"species": "Homo Sapiens"
	}
}

with open("C:/Users/dankri/Documents/Programmering/Python/Testing/Logininfo/file.json", "a") as file:
	json.dump(data, file)
	file.write(",\n")