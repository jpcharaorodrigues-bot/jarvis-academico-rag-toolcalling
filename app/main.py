from app.llm_client import LLMClient


def main():
    print("JARVIS Acadêmico iniciado.")
    print("Digite 'sair' para encerrar.\n")

    llm = LLMClient()

    while True:
        pergunta = input("Você: ")

        if pergunta.lower().strip() in ["sair", "exit", "quit"]:
            print("Encerrando o JARVIS Acadêmico.")
            break

        messages = [
            {
                "role": "system",
                "content": (
                    "Você é o JARVIS Acadêmico, um assistente para estudantes. "
                    "Responda de forma clara, técnica e objetiva."
                )
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
