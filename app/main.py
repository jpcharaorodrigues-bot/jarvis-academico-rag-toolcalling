from app.llm_client import LLMClient


def main():
    print("JARVIS Acadêmico iniciado.")
    print("Digite 'sair' para encerrar.\n")

    llm = LLMClient()

    while True:
        pergunta = input("Você: ").strip()

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o JARVIS Acadêmico.")
            break

        messages = [
            {
                "role": "system",
                "content": "Você é um assistente acadêmico para apoio ao estudo."
            },
            {
                "role": "user",
                "content": pergunta
            }
        ]

        resposta = llm.generate(messages)

        print("\nJARVIS:")
        print(resposta)
        print()


if __name__ == "__main__":
    main()
