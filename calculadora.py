import tkinter as tk
from tkinter import messagebox


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("310x320")
        self.resizable(0, 0)
        self.iconbitmap("calculadora.ico")
        self.expresion = ""
        self.entrada = None
        self.entrada_texto = tk.StringVar()
        self._creacion_componentes()

    def _creacion_componentes(self):
        entrada_frame = tk.Frame(self, width=310, height=50, bg="grey")
        entrada_frame.pack(side=tk.TOP)
        entrada = tk.Entry(entrada_frame, font=("arial", 18, "bold"),
                           textvariable=self.entrada_texto, width=23, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)

        botones_frame = tk.Frame(self, width=400, height=450, bg="grey")
        botones_frame.pack()

        boton_limpiar = tk.Button(botones_frame, text="C", width="32", height="3",
                                  bd=0, bg="#eee", cursor="pirate", command=self._evento_limpiar)
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        boton_division = tk.Button(botones_frame, text="/", width="10", height="3", bd=0, bg="#eee", cursor="pirate",
                                   command=lambda: self._evento_click("/"))
        boton_division.grid(row=0, column=3, padx=1, pady=1)

        boton_siete = tk.Button(botones_frame, text="7", width=10, height=3, bd=0, bg="#fff",
                                cursor="pirate", command=lambda: self._evento_click("7"))
        boton_siete.grid(row=1, column=0, padx=1, pady=1)
        boton_ocho = tk.Button(botones_frame, text="8", width=10, height=3, bd=0, bg="#fff",
                               cursor="pirate", command=lambda: self._evento_click("8"))
        boton_ocho.grid(row=1, column=1, padx=1, pady=1)
        boton_nueve = tk.Button(botones_frame, text="9", width=10, height=3, bd=0, bg="#fff",
                                cursor="pirate", command=lambda: self._evento_click("9"))
        boton_nueve.grid(row=1, column=2, padx=1, pady=1)
        boton_multiplicar = tk.Button(botones_frame, text="*", width=10, height=3, bd=0, bg="#fff",
                                      cursor="pirate", command=lambda: self._evento_click("*"))
        boton_multiplicar.grid(row=1, column=3, padx=1, pady=1)
        boton_cuatro = tk.Button(botones_frame, text="4", width=10, height=3, bd=0, bg="#fff",
                                 cursor="pirate", command=lambda: self._evento_click("4"))
        boton_cuatro.grid(row=2, column=0, padx=1, pady=1)
        boton_cinco = tk.Button(botones_frame, text="5", width=10, height=3, bd=0, bg="#fff",
                                cursor="pirate", command=lambda: self._evento_click("5"))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)
        boton_seis = tk.Button(botones_frame, text="6", width=10, height=3, bd=0, bg="#fff",
                               cursor="pirate", command=lambda: self._evento_click("6"))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)
        boton_suma = tk.Button(botones_frame, text="+", width=10, height=3, bd=0, bg="#fff",
                               cursor="pirate", command=lambda: self._evento_click("+"))
        boton_suma.grid(row=2, column=3, padx=1, pady=1)
        boton_uno = tk.Button(botones_frame, text="1", width=10, height=3, bd=0, bg="#fff",
                              cursor="pirate", command=lambda: self._evento_click("1"))
        boton_uno.grid(row=3, column=0, padx=1, pady=1)
        boton_dos = tk.Button(botones_frame, text="2", width=10, height=3, bd=0, bg="#fff",
                              cursor="pirate", command=lambda: self._evento_click("2"))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)
        boton_tres = tk.Button(botones_frame, text="3", width=10, height=3, bd=0, bg="#fff",
                               cursor="pirate", command=lambda: self._evento_click("3"))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)
        boton_resta = tk.Button(botones_frame, text="-", width=10, height=3, bd=0, bg="#fff",
                                cursor="pirate", command=lambda: self._evento_click("-"))
        boton_resta.grid(row=3, column=3, padx=1, pady=1)
        boton_cero = tk.Button(botones_frame, text="0", width=21, height=3, bd=0, bg="#fff",
                               cursor="pirate", command=lambda: self._evento_click("0"))
        boton_cero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        boton_punto = tk.Button(botones_frame, text=".", width=10, height=3, bd=0, bg="#fff",
                                cursor="pirate", command=lambda: self._evento_click("."))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)
        boton_igual = tk.Button(botones_frame, text="=", width=10, height=3, bd=0, bg="#fff",
                                cursor="pirate", command=self._evento_evaluar)
        boton_igual.grid(row=4, column=3, padx=1, pady=1)

    def _evento_evaluar(self):
        try:
            resultado = str(eval(self.expresion))
            self.entrada_texto.set(resultado)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
            self.entrada_texto.set("")
        finally:
            self.expresion = ""

    def _evento_limpiar(self):
        self.expresion = ""
        self.entrada_texto.set(self.expresion)

    def _evento_click(self, elemento):
        self.expresion = f"{self.expresion}{elemento}"
        self.entrada_texto.set(self.expresion)


if __name__ == "__main__":
    calcauladora = Calculadora()
    calcauladora.mainloop()
