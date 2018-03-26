
# STSTUS
VALID_LOCK_FILE = False

# @define
ENTER_DEFINE_BLOCK = False
DEFINING_TO = "Abstract"



DEPENDENCIES = []

with open("Miragefile.deps") as mlock:
    parse_str = mlock.readlines()


    for line in parse_str:

        # Avoid parsing empty line
        line_striped = line.strip()

        if len(line_striped) < 1:
            continue

        # DOC TYPE CHECK
        if "@mirage" in line_striped:
            if not "vendoring" in line_striped:
                print("This is not mirage locking file!")
                exit(1)
            else:
                VALID_LOCK_FILE = True


        # Parse @define block
        if "@define" in line_striped and "begin" in line_striped:
            ENTER_DEFINE_BLOCK = True
            DEFINING_TO = line_striped.split(" ")[1]
            continue

        if "@end" in line_striped:
            ENTER_DEFINE_BLOCK = False
            continue

        if ENTER_DEFINE_BLOCK:
            DEPENDENCIES.append(line)


    for dep in DEPENDENCIES:
        print("Found dependencies: " + dep.split("::")[0] + "           Version: " + dep.split("::")[1])
