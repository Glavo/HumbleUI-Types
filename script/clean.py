#! /usr/bin/env python3
import build_utils, common, os, sys

def main():
  os.chdir(common.basedir)
  build_utils.rmdir("target")
  build_utils.rmdir("docs/apidocs")
  return 0

if __name__ == '__main__':
  sys.exit(main())