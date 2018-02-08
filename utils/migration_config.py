#!/usr/bin/env python

import os

if __name__ == "__main__":
    try:
        os.rename("DjFile", "Miragefile")
    except:
        pass

    try:
        os.rename("DjFile.additional", "Miragefile.addon")
    except:
        pass

    try:
        os.rename("DjFile.secret", "Miragefile.secret")
    except:
        pass
