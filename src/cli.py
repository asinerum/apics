from apiliter import *

def main ():
  import os.path as op
  theapp, host, port, cert, key = app_init()
  if op.isfile(cert) and op.isfile(key):
    uvicorn.run (
      theapp,
      host=host,
      port=443,
      ssl_certfile=cert,
      ssl_keyfile=key,
    )
  else:
    uvicorn.run (theapp, host=host, port=port)

if __name__ == '__main__':
  main()
