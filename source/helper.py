import json
from types import SimpleNamespace

encoding = "utf-8"

def writeToFile(fileName: str, content: str):
  with open(fileName, 'w', encoding=encoding) as out:
    out.write(content)

def appendToFile(fileName: str, content: str):
  with open(fileName, 'a', encoding=encoding) as out:
    out.write(content)

def readFile(fileName: str) -> str:
    with open(fileName, 'r', encoding=encoding) as out:
      return out.read()

def serializeJson(object, indent = False) -> str:
  return json.dumps(object, indent=2 if indent else 0, default=lambda obj: obj.__dict__)

def deserializeJson(str) -> any:
  return json.loads(str, object_hook=lambda d: SimpleNamespace(**d))