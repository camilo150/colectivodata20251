import pandas as pd

df=pd.read_csv("./data/asistencia_estudiantes_completo.csv")


#ANTES DE FILTRAR COMO ANALISTAS DE DATOS DEBES CONOCER (EXPLORAR LA FUENTE PRIMARIA)
#print(df['estado'].unique())
#print(df['estrato'].unique())
#print(df['medio_transporte'].unique())

#FILTROS Y CONDICIONES PARA TRANSOFRMAR DATOS
#1. Reportar todos los estudiantes que asistieron
#estudiantesQueAsistieron=df.query('estado=="asistio"')
#2. Reportar todos los estudiantes que faltaron
#estudiantesQueFaltaron=df.query('estado=="inasistencia"')
#3. Reportar todos los estudiantes que llegaron tarde(Justificado)
#estudiantesjustificados=df.query('estado=="justificado"')
#4. Reportar todos los estudiantes de estrato 1
#estudiantesEstratoUno=df.query('estrato==1')
#5. Reportar todos los estudiantes de estratos altos
#estudiantesEstratoAlto=df.query('estrato>3')
#6. Reportar todos los estudaintes que llegan en metro
#estudiantesQueUsanMetro=df.query('medio_transporte=="metro"')
#7. Reportar todos los estudaintes que llegan en bicicleta
#estudiantesQueUsanCicla=df.query('medio_transporte=="bicicleta"')
#8. Reportar todos los estudiantes que no caminan para llegar a la u
#estudiantesQueNoCaminan=df.query('medio_transporte!="a pie"')
#9. Reportar todos los registros de asistencia del mes de junio
#estudiantes=df.query('fecha >= "2025-06-01" and fecha <= "2025-06-30"')
#10. Reportar los estudaintes que faltaron y usan bus para llegar a la u
#estudiantesQueFaltanUsanBus=df.query('medio_transporte=="bus" and estado=="inasistencia"')
#11. Reportar estudiantes que usan bus y son de estratos altos
#estudiantesQueUsanBusySonPupi=df.query('medio_transporte=="bus" and estrato > 3')
#12. Reportar estudiantes que usan bus y son de estratos bajos
#estudiantesQueUsanBusySonPobres=df.query('medio_transporte=="bus" and estrato <= 3')
#13. Reportar estudiantes que llegan tarde y son de estrato 3,4,5 o 6
#estudiantesTardesYpupis=df.query('estado=="inasistencia" and estrato >= 3')
#14. Reportar estudiantes que usan transportes ecologicos 
#estudiantesEco=df.query('medio_transporte=="a pie" or medio_transporte == "bicicleta"')
#print(estudiantesTardesYpupis)
#15. Reportar estudiantes que faltan y usan carro para transportarse
#estudiantesQueTienencarroYnoVan=df.query('medio_transporte=="carro" and estado "inasistencia"')
#16. Reportar estudiantes que asisten son estratos altos y caminan
#estudiantesPupisYeco=df.query('medio_transporte =="a pie" and estrato >= 3')
#17. Reportar estudiantes que son estratos bajos y justifican su iniasistencia
#pobresquejustifican=df.query('estrato <= 3 and estado=="justificado"')
#18. Reportar estudiantes que son estratos altos y justifican su iniasistencia
#pupisquejustifican=df.query('estrato >= 3 and estado=="justificado"')
#19. Reportar estudiantes que usan carro y justifican su inasistencia
#estudiantesQueTienencarroYVan=df.query('medio_transporte=="carro" and estado "justificado"')
#20. Reportar estudiantes que faltan y usan metro y son estratos medios
#METROymedios=df.query('estrato == 4 and estado "inasistencia" and medio_transporte == "metro"')


#AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
#1. Contar cada registro de asistencia por cada estado
#print(df['estado'].value_counts())

#2. Numero de registros por estrato
#print(df['estrato'].value_counts())

#3. Cantidad de estudiantes por medio de transporte
#print(df['medio_transporte'].value_counts())

#4. Cantidad de registros por grupo
#print(df['id_grupo'].value_counts())

#5. Cruce entre estado y medio de transporte
#dfEstado=df['estado']
#dfMedio=df['medio_transporte']
#dfUnificado = pd.concat([dfEstado,dfMedio])
#print(dfUnificado)
#6. Promedio de estrato por estado de asistencia
#promedioEstratoPorEstado=df.groupby('estado')['estrato'].mean()
#print(promedioEstratoPorEstado)
#7. Estrato promedio por medio de transporte
#promedioTransporte=df['medio_transporte'].mean()
#print(promedioEstratoPorEstado)
#8. Maximo estrato por estado de asistencia
#max_estrato_por_estado = df.groupby('estado')['estrato'].max()
#print(max_estrato_por_estado)
#9. Minimo estrato por estado de asistencia
#min_estrato_por_estado = df.groupby('estado')['estrato'].min()
#print(min_estrato_por_estado)
#10.Conteo de asistencias por grupo y por estado
#conteo = df.groupby(['id_grupo', 'estado']).size().reset_index(name='cantidad')
#11. Transporte usado por cada grupo
#transoportesPorGrupo =df.groupby(['id_grupo', 'medio_transporte']).size().reset_index(name='transportes')
#12. cuantos grupos distintos registraron asistencia por fecha
#grupos_por_fecha = df.groupby('fecha')['id:grupo'].nunique().reset_index(name='grupos_distintos')
#print(grupos_por_fecha)
#13. Promedio de estrato por fecha
#promedio_estrato = df.groupby('fecha')['estrato'].mean().reset_index(name='promedio_estrato')
#print(promedio_estrato)
#14. Numero de tipos de estado por transporte
#estados_por_transporte = df.groupby('medio_transporte')['estado'].nunique().reset_index(name='tipos_estado')
#print(estados_por_transporte)
#15. Primer Registro de cada grupo
#primer_registro = df.sort_values('fecha').groupby('id_grupo').first().reset_index()
#print(primer_registro)

