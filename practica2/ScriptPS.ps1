#Script de PowerShell


function Menu-Opciones {

    Clear-Host
    Write-Host "Comenzando Menu..."
    Write-Host "1. Mostrar Todos los servicios"
    Write-Host "2. Generar reporte de los servicios"
    Write-Host "3. Salir del Menu"

}

Menu-Opciones

While(($opc = Read-Host -Prompt "Selecciona una opcion") -ne "3") {

    if ($opc -eq "1")
    {
        Clear-Host
        Write-Host "------------------------------";
        Write-Host "Mostrando todos los servicios...";
        Write-Host "------------------------------";
        Get-Service;
        Write-Host "------------------------------";
        Write-Host "Salio con exito!";
    }
    elseif ($opc -eq "2")
    {
        Clear-Host
        Write-Host "------------------------------";
        Write-Host "Generando informa de todos los servicios...";
        Write-Host "------------------------------";
        Get-Service | Out-File -FilePath D:/InformeServicios.txt;
        Write-Host "------------------------------";
        Write-Host "Salio con exito!";
    }
    else 
    {
        Write-Host "Salida del programa";
        break
    }

    

}