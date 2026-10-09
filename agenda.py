contatos = []

def adicionar_contato(nome, telefone):
    contatos.append({"nome": nome, "telefone": telefone})
adicionar_contato("Ricardo", "123456789")
adicionar_contato("Maria", "987654321")
adicionar_contato("Joao", "456789123")
adicionar_contato("Ana", "789123456")
for contato in contatos:
    print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")