from app.orchestrator import Orchestrator


def main():
    print("JARVIS Academico iniciado.")
    print("Digite 'sair' para encerrar.\n")

    orchestrator = Orchestrator()

    while True:
        pergunta = input("Voce: ").strip()

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o JARVIS Academico.")
            break

        resposta = orchestrator.handle(pergunta)

        print("\nJARVIS:")
        print(resposta)
        print()


if __name__ == "__main__":
    main()