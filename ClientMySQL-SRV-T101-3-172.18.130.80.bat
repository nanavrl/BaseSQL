@echo off
@set srv=172.18.130.80
@rem if not "%1"=="" 
goto :label2
@echo .
@set /p correct=Entrer l'adresse IP du serveur mySQL sinon [Entrer] pour fonctionner en local : 
cls
@if /I "%correct%"=="" goto :label
@color 0A
@echo adresse IP serveur mySQL distant : %correct%
@echo last update mySQL : 25/08/2020 
@%CD%\App\ZMWS\mySQL\bin\mysql -uroot -h %correct% -peric --default-character-set=utf8 
@goto :eof
@:label2
@color 0A
@echo adresse IP serveur mySQL distant : %srv%
@echo last update mySQL : 25/08/2020 
@%CD%\App\ZMWS\mySQL\bin\mysql -uroot -h %srv% -peric --default-character-set=utf8 
@goto :eof
@:label
@color 0E
@tasklist /FI "IMAGENAME eq mysqld.exe" 2>NUL | find /I /N "mysqld.exe">NUL
@rem QPROCESS "mysqld.exe">NUL
@if "%ERRORLEVEL%"=="0" goto :suite
@echo . 
@echo Lancement du serveur local veuillez patienter quelques secondes, merci.
@start /MIN "serveur mySQL" %CD%\App\ZMWS\mySQL\lancerServeurMySQL.bat %CD%\App\ZMWS\mySQL\
@timeout /T 15
@:suite
cls
@tasklist /FI "IMAGENAME eq mysqld.exe" 2>NUL | find /I /N "mysqld.exe">NUL
@rem QPROCESS "mysqld.exe">NUL
@if "%ERRORLEVEL%"=="0" goto :suite1
@echo Erreur : impossible de se connecter au serveur local
@pause
@goto :eof
@:suite1
@echo client mySQL connecte au serveur local
@echo last update mySQL : 25/08/2020 
@%CD%\App\ZMWS\mySQL\bin\mysql -uroot -peric --default-character-set=utf8
@%CD%\App\ZMWS\mySQL\bin\mysqladmin shutdown -uroot -peric
@:eof
@rem E.Blot 
exit