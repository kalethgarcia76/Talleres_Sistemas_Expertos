
import os, sys, subprocess

MODULOS = {
    "1": ("Módulo 2 - Motor de Inferencia", "MODULO_2_MOTOR_INFERENCIA/sesion2_motor_inferencia/sesion2_motor_inferencia/main.py"),
    "2": ("Módulo 3 - Lógica Difusa", "MODULO_3_LOGICA_DIFUSA/sesion3_logica_difusa/sesion3_logica_difusa/main.py"),
    "3": ("Módulo 5 - Defuzzificación", "MODULO_5_DEFUZZIFICACION/sesion5_defuzzificacion/sesion5_defuzzificacion/main.py"),
    "4": ("Módulo 6 - Árbol de Decisión", "MODULO_6_ARBOL_DECISION/sesion6_arbol_decision/main.py"),
    "5": ("Sistema Experto IT", "MODULO_SISTEMA_EXPERTO_IT/sistema_experto_it/sistema_experto_it/main.py"),
    "6": ("Módulo 9 - KNN", "MODULO_9_KNN/sesion9_knn/main.py"),
    "7": ("Módulo 10 - SVM", "MODULO_10_SVM/sesion10_svm/main.py"),
    "8": ("Módulo 11 - Perceptrón", "MODULO_11_PERCEPTRON/sesion11_perceptron/main.py"),
    "9": ("Módulo 12 - Redes MLP", "MODULO_12_REDES_MLP/sesion12_redes_mlp/main.py"),
}

def menu():
    while True:
        print("\n" + "="*72)
        print("TRABAJO INTEGRADO - MÓDULOS CASE")
        print("="*72)
        for k,(nombre,_) in MODULOS.items(): print(f"{k}. {nombre}")
        print("0. Salir")
        op=input("Seleccione un módulo: ").strip()
        match op:
            case "0":
                print("Trabajo finalizado."); break
            case _ if op in MODULOS:
                ruta=MODULOS[op][1]
                subprocess.run([sys.executable, ruta], cwd=os.path.dirname(os.path.abspath(__file__)))
            case _:
                print("Opción no válida.")

if __name__=="__main__": menu()
