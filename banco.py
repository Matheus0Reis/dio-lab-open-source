# sistema_bancario_gui.py

import tkinter as tk
from tkinter import messagebox

class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append({"operacao": "Depósito", "valor": valor})
            return f"Depósito de {self.formatar_valor(valor)} realizado com sucesso!"
        else:
            return "Valor de depósito inválido!"

    def sacar(self, valor):
        if valor > 0 and valor <= 500:
            if self.saques_diarios < 3:
                if valor <= self.saldo:
                    self.saldo -= valor
                    self.extrato.append({"operacao": "Saque", "valor": valor})
                    self.saques_diarios += 1
                    return f"Saque de {self.formatar_valor(valor)} realizado com sucesso!"
                else:
                    return "Saldo insuficiente!"
            else:
                return "Limite de saques diários atingido!"
        else:
            return "Valor de saque inválido!"

    def gerar_extrato(self):
        if not self.extrato:
            return "Não foram realizadas movimentações."
        else:
            texto = "Extrato da conta:\n"
            for item in self.extrato:
                texto += f"{item['operacao']} de {self.formatar_valor(item['valor'])}\n"
            texto += f"Saldo atual: {self.formatar_valor(self.saldo)}"
            return texto

    def formatar_valor(self, valor):
        return f"R$ {valor:.2f}"

class SistemaBancarioGUI:
    def __init__(self, master):
        self.master = master
        self.conta = ContaBancaria()

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label_titulo = tk.Label(self.frame, text="Banco Digital", font=("Arial", 24))
        self.label_titulo.pack()

        self.label_saldo = tk.Label(self.frame, text="Saldo: R$ 0.00", font=("Arial", 18))
        self.label_saldo.pack()

        self.entry_valor = tk.Entry(self.frame, width=20)
        self.entry_valor.pack()

        self.button_depositar = tk.Button(self.frame, text="Depósito", command=self.depositar)
        self.button_depositar.pack()

        self.button_sacar = tk.Button(self.frame, text="Saque", command=self.sacar)
        self.button_sacar.pack()

        self.button_extrato = tk.Button(self.frame, text="Extrato", command=self.extrato)
        self.button_extrato.pack()

        self.button_sair = tk.Button(self.frame, text="Sair", command=self.master.destroy)
        self.button_sair.pack()

    def depositar(self):
        valor = float(self.entry_valor.get())
        resultado = self.conta.depositar(valor)
        messagebox.showinfo("Resultado", resultado)
        self.label_saldo.config(text=f"Saldo: {self.conta.formatar_valor(self.conta.saldo)}")

    def sacar(self):
        valor = float(self.entry_valor.get())
        resultado = self.conta.sacar(valor)
        messagebox.showinfo("Resultado", resultado)
        self.label_saldo.config(text=f"Saldo: {self.conta.formatar_valor(self.conta.saldo)}")

    def extrato(self):
        texto = self.conta.gerar_extrato()
        messagebox.showinfo("Extrato", texto)

root = tk.Tk()
root.title("Banco Digital")
root.geometry("300x250")

gui = SistemaBancarioGUI(root)
root.mainloop()