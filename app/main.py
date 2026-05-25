from app.orchestrator import Orchestrator


def main():
    print("JARVIS Acadêmico iniciado.")
    print("Digite 'sair' para encerrar.\n")

    orchestrator = Orchestrator()

    while True:
        pergunta = input("Você: ").strip()

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o JARVIS Acadêmico.")
            break

        resposta = orchestrator.handle(pergunta)

        print("\nJARVIS:")
        print(resposta)
        print()


if __name__ == "__main__":
    main()
