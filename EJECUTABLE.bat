@echo off
color a
@mode con cols=40 lines=23


set skin=Notch
set version=Aun sin especificar
set nombre=Gamersinnombre

:menu
	
	cls
	echo ----------------------------------------
	echo.
	echo          Selecciona un ajuste
	echo.
	echo         [1]Seleccionar version
	echo         [2]Seleccionar nombre
	echo          [3]Seleccionar skin
	echo             [4]Craqueado?
	echo		     [5]Ejecutar
	echo   Version escogida: %version%
	echo   Nombre a usar: %nombre%
	echo   Usuario de skin: %skin%
	echo   Version: craqueada (de momento)
	echo.   
	echo ----------------------------------------
	set/p ajuste= Que desea:
	if %ajuste% == 1 goto version
	if %ajuste% == 2 goto name
	if %ajuste% == 3 goto skin
	if %ajuste% == 4 goto login
	if %ajuste% == 5 goto start
	pause
goto menu


	
	
	
:version
	cls
	echo ----------------------------------------
	echo.
	echo       Que version le gustaria jugar
	echo.
	set/p version= EJ 1.18.2, 1.8.9:
	echo.
	echo.
	echo ----------------------------------------
	goto menu

:name:
	cls
	echo ----------------------------------------
	echo.
	echo       Que nombre le gustaria usar
	echo.
	set/p nombre=Nombre a usar:
	echo.
	echo.
	echo ----------------------------------------
	goto menu
	
:skin:
	cls
	echo ----------------------------------------
	echo.
	echo       Nombre de usuario portador de
	echo.			   skin deseada
	set/p skin=EJ vegetta777:
	echo.
	echo.
	echo ----------------------------------------
	goto menu
	
:login:
	cls
	echo ----------------------------------------
	echo.
	echo       Iniciar sesion con mojang
	echo.	    (Trabajando en ello...)
	echo.
	echo        Version actual: craqueada
	echo.
	echo ----------------------------------------
	pause
	goto menu

:start:
	cd recursos
	python3 a.py --username %nombre% --version %version% --skin_of %skin%
	cls
	pause
	goto menu








