def determinar_mejor_promedio(estudiantes):
 """ Determina el estudiante con el mejor promedio dada una lista
 (Diccionario) con los datos de 4 estudiantes

 -En caso de que dos o mas alumnos tengan el mismo promedio, el
 mejor promedio sera el del primer alumno evaluado dentro del empate
 Parámetros:
 -----------
 estudiantes (dictionary):
 Lista de estudiantes con nombre y promedio.

 Retorna:
 --------
 str: Cadena de caracteres de la forma
 “Con {promedio}, el mejor estudiante es {nombre}”
 """
 best_student_prom = ''
 best_student_score = 0
 cont = 0
 for key, val in estudiantes.items():
     if(type(val) is float or type(val) is int):
         if (cont==0):
             best_student_prom = key
             best_student_score = val
         else:
             if (val > best_student_score):
                 best_student_prom = key
                 best_student_score = val
     cont+=1
 return f"Con {best_student_score}, el mejor estudiante es {estudiantes[f'est{best_student_prom[-1]}']}"


if __name__ == '__main__':
    students_dict = {'est1': 'Ana', 'prom1': 4.1, 'est2': 'Juan', 'prom2':4.5, 'est3': 'Pedro', 'prom3': 4.4, 'est4': 'Carla','prom4': 4.3}



    print(determinar_mejor_promedio(students_dict))