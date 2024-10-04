from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta, GastoDTOPeticion, GastoDTORespuesta, CategoriaDTOPeticion, CategoriaDTORespuesta, MetodoPagoDTOPeticion, MetodoPagoDTORespuesta, IngresoDTOPeticion, IngresoDTORespuesta
from app.api.models.modelosApp import Usuario, Gasto, Categoria, MetodoPago, Ingreso
from app.database.configuration import sessionLocal, engine

#Para que un api funcione debe tener un archivo enrutador
rutas=APIRouter() #ENDPOINTS

#Crear una funcion para establecer cuando yo quiera y necesite
#conexion hacia la base de datos
def getDataBase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

#PROGRAMACION DE CADA UNO DE LOS SERVICIOS
#QUE OFRECERA NUESTRA API

#SERVICIO PARA REGISTRAR O GUARDAR UN USUARIO EN BD
@rutas.post("/usuarios", response_model=UsuarioDTORespuesta)
def guardarUsuario(datosPeticion:UsuarioDTOPeticion, db:Session=Depends(getDataBase)):
    try:
        usuario=Usuario(
            nombres=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")

@rutas.get("/usuarios", response_model=List[UsuarioDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Usuario).all()
        return listadoDeUsuarios

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
    
    ####

@rutas.post("/Gastos")
def guardarUsuario(datosPeticion:GastoDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        gasto=Gasto(
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            nombre=datosPeticion.nombre
        )
        db.add(gasto)
        db.commit()
        db.refresh(gasto)
        return gasto
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
    
@rutas.get("/Gastos", response_model=List[GastoDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Gasto).all()
        return listadoDeUsuarios

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
    
    ####

@rutas.post("/Ingreso")
def guardarUsuario(datosPeticion:IngresoDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        ingreso=Ingreso(
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            nombre=datosPeticion.nombre
        )
        db.add(ingreso)
        db.commit()
        db.refresh(ingreso)
        return ingreso
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
    
@rutas.get("/Ingreso", response_model=List[IngresoDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Ingreso).all()
        return listadoDeUsuarios

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
    
    ####

@rutas.post("/Categoria")
def guardarUsuario(datosPeticion:CategoriaDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        categoria=Categoria(
            nombreCategoria=datosPeticion.nombreCategoria,
            descripcion=datosPeticion.descripcion
        )
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")

@rutas.get("/Categoria", response_model=List[CategoriaDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Categoria).all()
        return listadoDeUsuarios

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")

    ####

@rutas.post("/MetodoPago")
def guardarUsuario(datosPeticion:MetodoPagoDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        metodoPago=MetodoPago(
            nombreMetodo=datosPeticion.nombreMetodo,
            descripcion=datosPeticion.descripcion
        )
        db.add(metodoPago)
        db.commit()
        db.refresh(metodoPago)
        return metodoPago
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
    
@rutas.get("/MetodoPago", response_model=List[MetodoPagoDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(MetodoPago).all()
        return listadoDeUsuarios

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
