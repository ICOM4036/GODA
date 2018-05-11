"""
    DEFAULT TEXT MESSAGES TO BE DISPLAYED SHALL BE DEFINED HERE TO AVOID TEXT CLUTTERING
"""
ver = '\tG.O.D.A' \
      '\nGENERIC OBJECTIVE DATA ADMINISTRATOR' \
      '\n------------------------------------' \
      '\nVERSION\t\t\t#.##' \
      '\nRELEASE DATE\t\tMM-DD-YYYY' \
      '\nWEBSITE\t\t\tSOMETHING.COM'
help_txt = 'FOR MORE INFORMATION ON A COMMAND TYPE "HELP -[CMD]"\n' \
           '\nCRT\t\tCREATE LIBRARY OR COLLECTION' \
           '\nOPEN\t\tOPEN AN INSTANCED LIBRARY OR COLLECTION' \
           '\nQUIT\t\tCLOSE AN INSTANCED LIBRARY OR COLLECTION'

help_cmd = {
    'crt': '\nCRT\t\tCREATE COMMAND'
           '\nCRT LIB\t\tCREATE A NEW LIBRARY'
           '\nCRT COL\t\tCREATE A NEW COLLECTION',
    'open': '\nOPEN\t\tOPEN COMMAND'
            '\nOPEN [LIB_NAME]\t\tOPENS A LIBRARY INSTANCE'
            '\nOPEN [COL_NAME]\t\tOPENS AN INSTANCE OF A COLLECTION IN THE CURRENT LIBRARY'
}