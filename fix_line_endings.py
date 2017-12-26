# fix the line ending from \r to \n
# because excel incorrectly uses \r

import sys
filename = sys.argv[1]
f = open(filename, 'r')
content = f.read()
f.close()

new_content = content.replace('\r', '\n')
new_content = new_content.replace('"', '')
f = open(filename, 'w')
f.write(new_content)
f.close()
