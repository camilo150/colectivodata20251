import pandas as pd 

dataFrameUsuarios=pd.read_excel("./data/usuarios_sistema_completo.xlsx") 


#1. Solo estudiantes
#soloEstudiantes = dataFrameUsuarios[dataFrameUsuarios['tipo_usuario'] == 'estudiante']
#print(soloEstudiantes)
#2. Solo profesores
#soloProfesores = dataFrameUsuarios[dataFrameUsuarios['tipo_usuario'] == 'docente']
#print(soloProfesores)
#3. Todos excepto estudiantes
#noEstudiantes = dataFrameUsuarios[dataFrameUsuarios['tipo_usuario'] != 'estudiante']
#print(noEstudiantes)
#4. Filtrar por especialidad
#especialidad = dataFrameUsuarios[dataFrameUsuarios['especialidad'] == '']
#print(especialidad)
#5. Excluir una especialidad
#excluirEspecialidad = dataFrameUsuarios[dataFrameUsuarios['especialidad'] != 'Ingenieria de Sistemas']
#print(excluirEspecialidad)
#6. Excluir administrativos
#noAdministrativo = dataFrameUsuarios[dataFrameUsuarios['tipo_usuario'] != 'administrativos']
#print(noAdministrativo)
#7. Direcciones en medellin
#direccionesMedellin = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.contains('Medellín', case=False)]
#print(direccionesMedellin)
#8. Direcciones terminadas en sur
#direccionesSur = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.endswith('sur', case=False)]
#print(direccionesSur)
#9. Direcciones que inician con calle
#direccionesCalle = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.startswith('calle', case=False)]
#print(direccionesCalle)
#10.Especialidades que contienen la palabra datos
#especialidadesDatos = dataFrameUsuarios[dataFrameUsuarios['especialidad'].str.contains('datos', case=False)]
#print(especialidadesDatos)
#11. instructores en itagui
#instructoresItagui = dataFrameUsuarios[(dataFrameUsuarios['tipo_usuario'] == 'Instructor') & (dataFrameUsuarios['direccion'].str.contains('Itagüí', case=False))]
#print(instructoresItagui)
#12. nacidos despues de 2000
#nacidosDespuesDe2000 = dataFrameUsuarios[pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']).dt.year > 2000]
#print(nacidosDespuesDe2000)
#13. nacidos en los 90
#nacidosEnLos90 = dataFrameUsuarios[(pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']).dt.year >= 1990) & (pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']).dt.year < 2000)]
#print(nacidosEnLos90)
#14. direcciones en envigado
#direccionesEnvigado = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.contains('Envigado', case=False)]
#print(direccionesEnvigado)
#15. especialdiades que empizan por I
#especialidadesI = dataFrameUsuarios[dataFrameUsuarios['especialidad'].str.startswith('I')]
#print(especialidadesI)
#16. usuarios sin direccion
#sinDireccion = dataFrameUsuarios[dataFrameUsuarios['direccion'].isna()]
#print(sinDireccion)
#17. usuarios sin especialidad
#sinEspecialidad = dataFrameUsuarios[dataFrameUsuarios['especialidad'].isna()]
#print(sinEspecialidad)
#18. profesores que viven en sabaneta
#profesoresSabaneta = dataFrameUsuarios[(dataFrameUsuarios['tipo_usuario'] == 'Profesor') & (dataFrameUsuarios['direccion'].str.contains('Sabaneta', case=False))]
#print(profesoresSabaneta)
#19. aprendices que viven en bello
#aprendicesBello = dataFrameUsuarios[(dataFrameUsuarios['tipo_usuario'] == 'Aprendiz') & (dataFrameUsuarios['direccion'].str.contains('Bello', case=False))]
#print(aprendicesBello)
#20. nacidos en el nuevo milenio
#nacidosNuevoMilenio = dataFrameUsuarios[pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']).dt.year >= 2000]
#print(nacidosNuevoMilenio)


#1. total por tipo
totalPorTipo = dataFrameUsuarios['tipo_usuario'].value_counts()
print(totalPorTipo)

#2. total por especialidad
totalPorEspecialidad = dataFrameUsuarios['especialidad'].value_counts()
totalPorEspecialidad = dataFrameUsuarios['especialidad'].value_counts()
print()

#3. cantidad de especialidades distintas
cantidadEspecialidades = dataFrameUsuarios['especialidad'].nunique()
print(cantidadEspecialidades)

#4. tipos de usuario por especialidad
tiposPorEspecialidad = dataFrameUsuarios.groupby('especialidad')['tipo_usuario'].value_counts()
print(tiposPorEspecialidad)

#5. usuario mas antiguo por tipo
usuarioMasAntiguo = dataFrameUsuarios.loc[dataFrameUsuarios.groupby('tipo_usuario')['fecha_nacimiento'].idxmin()]
print(usuarioMasAntiguo)

#6. usuario mas joven por tipo
usuarioMasJoven = dataFrameUsuarios.loc[dataFrameUsuarios.groupby('tipo_usuario')['fecha_nacimiento'].idxmax()]
print(usuarioMasJoven)

#7. primer registro por tipo
primerRegistro = dataFrameUsuarios.groupby('tipo_usuario').first()
print(primerRegistro)

#8. ultimo registro por tipo
combinacionTipoEspecialidad = dataFrameUsuarios.groupby(['tipo_usuario', 'especialidad']).size().reset_index(name='count')
print(combinacionTipoEspecialidad)

#9. combinacion tipo por especialidad
combinacionTipoEspecialidad = dataFrameUsuarios.groupby(['tipo_usuario', 'especialidad']).size().reset_index(name='count')
combinacionTipoEspecialidad = dataFrameUsuarios.groupby(['tipo_usuario', 'especialidad']).size().reset_index(name='count')
print()

#10. el mas viejo por especialidad
masViejoPorEspecialidad = dataFrameUsuarios.loc[dataFrameUsuarios.groupby('especialidad')['fecha_nacimiento'].idxmin()]
print(masViejoPorEspecialidad)

#11. cuantos de cada especialidad por tipo
cantidadPorEspecialidadTipo = dataFrameUsuarios.groupby(['especialidad', 'tipo_usuario']).size()
print(cantidadPorEspecialidadTipo)

#12. edad promedio por tipo
dataFrameUsuarios['edad'] = pd.to_datetime('today').year - pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']).dt.year
edadPromedioPorTipo = dataFrameUsuarios.groupby('tipo_usuario')['edad'].mean()
print(edadPromedioPorTipo)

#13. años de nacimeinto mas frecuente por especialidad
dataFrameUsuarios['anio_nacimiento'] = pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']).dt.year
aniosFrecuentesPorEspecialidad = dataFrameUsuarios.groupby('especialidad')['anio_nacimiento'].agg(lambda x: x.mode()[0])
dataFrameUsuarios['anio_nacimiento'] = pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']).dt.year
print()

#14. mes de nacimiento ams frecuente por tipo
dataFrameUsuarios['mes_nacimiento'] = pd.to_datetime(dataFrameUsuarios['fecha_nacimiento']).dt.month
mesFrecuentePorTipo = dataFrameUsuarios.groupby('tipo_usuario')['mes_nacimiento'].agg(lambda x: x.mode()[0])
print(dataFrameUsuarios)

#15. UNA CONSULTA O FILTRO QUE UD PROPONGA
filtroPropuesto = dataFrameUsuarios[dataFrameUsuarios['tipo_usuario'] != 'Estudiante']
print(filtroPropuesto)