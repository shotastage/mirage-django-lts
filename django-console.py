#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='argparse sample.')

    #bool オプション
    parser.add_argument('-e','--error', action='store_true', default=False, help='show error (default: show no error)')
    #数値 オプション
    parser.add_argument('-d','--data', type=int, help='data number')
    #文字列オプション
    parser.add_argument('-s','--str', type=str, help='data name')

    args = parser.parse_args()

    print(args)
