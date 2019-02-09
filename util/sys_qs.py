import base64
import json
import sys
from xml.dom import minidom


if len(sys.argv) == 1 or sys.argv[1] == '-':
    s = sys.stdin.read()
else:
    with open(sys.argv[1]) as f:
        s = f.read()

# pretty print xml
#out = minidom.parseString(s).toprettyxml(indent='  ')

# pretty print json
#out = json.dumps(json.loads(s), indent=2)

# base64 encode
#out = base64.b64encode(s.encode()).decode()

# base64 decode
out = base64.b64decode(s.encode()).decode()

print(out)