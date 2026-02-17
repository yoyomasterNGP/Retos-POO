# Reto 2 POO

Para este reto se realizó el diagrama UML sobre la organización de una subestación eléctrica. 
En este caso se utilizó una clase padre de componentes eléctricos, de las cuales tienen herencia 
el transformador y los interruptores que son los componentes más importantes. Así mismo,
la subestación es la composición de varios componentes eléctricos. Finalmente, se utilizó una
agregación para el mantenimiento de los equipos. 

## Diagrama UML de una subestación eléctrica

<pre>
 classDiagram
    class Subestacion {
        + Nombre
        + Ubicación
        + Lista componentes
        + Reporte de Estado()
    }

    class Componente Electrico {
        + Identificación
        + Marca
        + Activo
        + Conectar()
        + Desconectar()
    }

    class Transformador {
        + Potencia KVA
        + Voltaje Primario
        + Voltaje Secundario
        + Regular Voltaje()
    }

    class Interruptor {
        + Corriente Máxima
        + Corriente de Corto
        + Disparo
        + Abrir()
    }

    class Orden Mantenimiento {
        + Fecha Programada
        + Tipo (Preventivo/Correctivo)
        + Descripcion
        + Ejecutar Mantenimiento(Componente Electrico)
    }

    class Tecnico {
        + Nombre
        + Especialidad
        + Asignar Tarea(Orden Mantenimiento)
    }

    ComponenteElectrico <|-- Transformador : 
    ComponenteElectrico <|-- Interruptor : 
    Subestacion "1" *-- "*"  ComponenteElectrico : 
    Tecnico "1" --> "*" OrdenMantenimiento : 
    OrdenMantenimiento "1" o-- "1" ComponenteElectrico : 
</pre>
