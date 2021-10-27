from ftplib import FTP
import os

host = 'ftp.mirror.nl'
user = 'anonymous'
pws = ''

try:
    ftp = FTP(host, user, pws)

    print("Conexion con exito!...")
    print("\nDireccion actual en el path: "+ftp.pwd()+"\n")
    ftp.dir(); # Mostrar los directorios
    
    # OBTENER LOS ARCHIVOS TXT DE "pub"
    ftp.cwd("pub")
    print("\nDireccion actual en el path: "+ftp.pwd()+"\n")
    ftp.dir();

    # os.mkdir("Des_arch")
    # os.chdir("Des_arch/")
    # name_arch = 'robots.txt'
    # open_arch = open(name_arch, 'wb')
    # ftp.retrbinary("RETR "+name_arch, open_arch.write)

    # OBTENER LOS ARCHIVOS TXT DE pub/CPAN
    # ftp.cwd("CPAN")
    # print("\nDireccion actual en el path: "+ftp.pwd()+"\n")
    # ftp.dir();

    # os.chdir("Des_arch/")
    # name_arch = 'robots.txt'
    # open_arch = open(name_arch, 'wb')
    # ftp.retrbinary("RETR "+name_arch, open_arch.write)



except Exception as e:
    
    print("Conexion cerrada :"+str(e))
