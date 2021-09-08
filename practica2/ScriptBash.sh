#!/bin/bash


	echo "---------------------------------------------"
	echo "Menu de opciones"
	echo "1. Crear directorios"
	echo "2. Eliminar directorios creados anteriormente"
	echo "---------------------------------------------"
	read -p "Introduce una opcion: " opc
	
	if [ $opc -eq 1 ]
	then
		read -p "Escribe los directorio o directorio que quiere crear separado por espacion: " directorios
		for dir in $directorios
		do
			if [ -d $dir ]
			then
				echo "la carpeta $dir ya existe"
			else
				mkdir $dir
				if [ $? -eq 0 ]
				then
					echo "$dir se ha creado con exito"
				else
					echo "Ups! Algo ha salido mal en la creacion @dir"
				fi
			fi
		done
	
	elif [ $opc -eq 2 ]
	then
		
		read -p "Escribe los directorios o directorio que quieres crear separados por espacion: " directorios
		for dir in $directorios
		do
			if [ -d $dir ]
			then
				rmdir $dir
				if [ $? -eq 0 ]
				then
					echo "$dir se ha eliminado con exito"
				else
					echo "Ups! Algo ha salido mal no se pudo borra $dir"
				fi
			else
				echo "No exist carpeta $dir"
				
			fi
		done
	fi
