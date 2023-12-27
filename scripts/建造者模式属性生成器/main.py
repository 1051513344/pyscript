

if __name__ == "__main__":
    filterProperties = ["dict", "records"]
    with open("model.java", "r", encoding="utf-8") as f:
        source = f.read()
    className = ""
    for i in source.split("\n"):
        if i.startswith("public class"):
            className = i.split(" ")[2]
            break
    print(f"    public {className}()", "{}\n")
    print(f"    public {className}(Builder builder)", "{")
    for i in source.split("\n"):
        if "private" in i and not i.startswith("    private static final long"):
            property = i.split(" ")[len(i.split(" "))-1].replace(";", "")
            if property != "" and not property in filterProperties:
                print(f"        this.{property} = builder.{property};")
    print("    }\n")
    print("    public static class Builder {")
    for i in source.split("\n"):
        if "private" in i and not i.startswith("    private static final long"):
            type = i.split(" ")[len(i.split(" "))-2]
            property = i.split(" ")[len(i.split(" "))-1].replace(";", "")
            if property != "" and not property in filterProperties:
                print(f"        public {type} {property};")
    print("\n        public Builder() {}\n")
    print(f"        public {className} build()", "{")
    print(f"            return new {className}(this);")
    print("        }\n")
    for i in source.split("\n"):
        if "private" in i and not i.startswith("    private static final long"):
            type = i.split(" ")[len(i.split(" "))-2]
            property = i.split(" ")[len(i.split(" "))-1].replace(";", "")
            if property != "" and not property in filterProperties:
                upProperty = property[0].upper()+property[1:]
                print(f"        public Builder set{upProperty}({type} {property})", "{")
                print(f"            this.{property} = {property};")
                print("            return this;")
                print("        }")
    print("    }")
