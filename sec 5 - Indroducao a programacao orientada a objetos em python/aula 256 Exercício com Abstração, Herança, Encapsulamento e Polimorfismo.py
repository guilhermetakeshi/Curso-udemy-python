from abc import ABC, abstractmethod

# Classe abstrata Pessoa
class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'

# Classe abstrata Conta
class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')

# Classe ContaCorrente
class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite_extra):
        super().__init__(agencia, numero_conta, saldo)
        self.limite_extra = limite_extra

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite_extra
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite_extra:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r}, {self.limite_extra!r})'
        return f'{class_name}{attrs}'

# Classe ContaPoupanca
class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'

# Classe Cliente
class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

# Classe Banco
class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[Pessoa] | None = None,
        contas: list[Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(self, cliente: Pessoa, conta: Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'

    def realizar_saque(self, agencia, cliente, conta, valor):
        if self.autenticar(cliente, conta):
            if conta.sacar(valor):
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente ou limite extra excedido.")
        else:
            print("Autenticação falhou. Operação não permitida.")

if __name__ == '__main__':
    # Criação de clientes e contas
    c1 = Cliente('Luiz', 30, 111)
    cc1 = ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1

    c2 = Cliente('Maria', 18, 112)
    cp1 = ContaPoupanca(112, 223, 100)
    c2.conta = cp1

    # Criação do banco
    banco = Banco()

    # Adiciona clientes, contas e agências ao banco
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 112])  # Adicionei 112 para incluir a agência da conta poupança

    # Autentica o cliente e a conta
    if banco.autenticar(c1, cc1):
        cc1.depositar(10)  # Realiza um depósito na conta corrente
        c1.conta.depositar(100)  # Realiza um depósito através do cliente
        print(c1.conta)  # Exibe informações da conta corrente de Luiz

'''
class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, agencia, cliente, conta):
        if conta.agencia == agencia and cliente in self.clientes and conta in self.contas:
            return True
        else:
            return False
'''