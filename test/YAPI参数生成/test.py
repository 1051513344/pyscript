

import json
with open("EnrollApply.java", encoding="utf-8") as f:

    content = f.read()


template = """
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    
  },
  "required": [
    
  ]
}

"""
templatejSON = json.loads(template)

rowList = content.split("\n")
title = None
for row in rowList:
    if not row.startswith("    private static final "):
        if row.startswith("     * "):
            title = row.replace("     * ", "")
        if row.startswith("    private "):
            property = row.replace("    private ", "").split(" ")[1].replace(";", "")
            templatejSON["properties"][property] = {"type": "string", "title": title}
            templatejSON["required"].append(property)

print(json.dumps(templatejSON, ensure_ascii=False))