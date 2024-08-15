import os
from crewai_tools.tools.scrape_website_tool.scrape_website_tool import ScrapeWebsiteTool
from dotenv import load_dotenv
from datetime import datetime
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from textwrap import dedent

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração das chaves de API (substitua com suas chaves reais)
openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Inicialização dos modelos LLM
gpt3_llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
gpt4o_llm = ChatOpenAI(model="gpt-4o", api_key=openai_api_key)
llama3_70b = ChatGroq(model="llama3-70b-8192", api_key=groq_api_key)
gpt4o_mini_llm = ChatOpenAI(model="gpt-4o_mini", api_key=openai_api_key)

# Configuração das ferramentas
Customer_Input = ScrapeWebsiteTool(website_url="https://reginaldoaabh.wixsite.com/altivus-ai-alfa/")
Customer_Trends = ScrapeWebsiteTool(website_url="https://techcrunch.com/")

# Definição dos Agentes
planejador = Agent(
    role="Planejador de Conteúdo para Postagens",
    goal="""
        Planejar e estruturar conteúdo envolvente para o Instagram sobre {topic},
        garantindo que as postagens sejam estrategicamente alinhadas com os interesses do público.
    """,
    backstory="""
        Como Planejador de Conteúdo, você desempenha um papel fundamental 
        na criação de campanhas publicitárias impactantes no Instagram sobre {topic}.
    """,
    verbose=True,
    llm=gpt3_llm,
    allow_delegation=False
)

pesquisador = Agent(
    role='Pesquisador de Conteúdo Publicitário',
    goal="""
        Realizar pesquisas aprofundadas sobre as últimas tendências e informações relevantes sobre {topic},
        com o objetivo de criar uma base sólida para postagens publicitárias no Instagram.
    """,
    verbose=True,
    backstory="""
        Você é um pesquisador experiente e altamente qualificado, dedicado a encontrar as tendências mais recentes 
        e informações pertinentes sobre {topic}.
    """,
    llm=gpt3_llm,
    tools=[Customer_Input, Customer_Trends],
    allow_delegation=False
)

escritor_post = Agent(
    role='Escritor de Conteúdo para Postagens',
    goal="""
        Redigir {n} postagens cativantes em português do Brasil para o Instagram sobre {topic},
        com um mínimo de 250 palavras e máximo de 350 palavras.
    """,
    backstory="""
        Você é um escritor criativo e talentoso, especializado em transformar informações e pesquisas 
        em conteúdos atraentes e envolventes para redes sociais.
    """,
    llm=gpt4o_llm,
    verbose=True,
    allow_delegation=False
)

gerador_de_midia = Agent(
    role='Gerador de Imagens Publicitárias',
    goal="""
        Criar uma imagem visualmente atraente utilizando o DALL-E, baseada em um prompt específico sobre {topic}.
    """,
    backstory=dedent("""
        Você é um designer digital experiente, dedicado a transformar ideias em arte visual impactante.
    """),
    verbose=True,
    llm=llama3_70b,
    max_rpm=1,
    allow_delegation=False
)

formatador = Agent(
    role='Gerente de Formatação de Postagens',
    goal=dedent("""
        Receber o texto do Agente Escritor de Post e a imagem do Agente Gerador de Mídia,
        e formatar ambos para se adequarem aos melhores padrões de publicidade no Instagram.
    """),
    verbose=True,
    backstory=dedent("""
        Você é um especialista em formatação e design digital, com uma vasta experiência 
        em adaptar conteúdos para se adequarem aos padrões visuais e textuais das redes sociais.
    """),
    llm=gpt3_llm
)

# Definição das Tarefas
plano_task = Task(
    description=dedent("1. Priorize as últimas tendências, principais 'players', "
                       "e notícias relevantes sobre {topic}.\n"
                       "2. Identifique o público-alvo, considerando "
                       "seus interesses e pontos de dor.\n"
                       "3. Desenvolva um plano de conteúdo detalhado, incluindo "
                       "uma introdução, pontos principais e um chamado à ação.\n"
                       "4. Inclua palavras-chave de SEO e dados ou fontes relevantes."),
    expected_output=dedent("Um documento de plano de conteúdo para {n} posts sobre {topic} "
                           "com um esboço, análise do público, "
                           "palavras-chave de SEO e recursos."),
    agent=planejador,
    verbose=True
)

pesquisa_task = Task(
    description="Pesquise as últimas tendências sobre {topic}.",
    expected_output="Um relatório detalhado sobre as tendências mais recentes sobre {topic} na área de tecnologia.",
    agent=pesquisador,
    verbose=True
)

escrita_task = Task(
    description=dedent("Escreva {n} postagens envolventes em português do Brasil "
                       "com base nas tendências pesquisadas sobre {topic} com no mínimo 250 palavras e no máximo 350 palavras cada. "
                       "Cada post deve ser formatado como:\n\n"
                       "POST:\ntexto do post em português do brasil\n\n"
                       "PROMPT:\nPrompt da imagem desse post\n\n"),
    expected_output=dedent("{n} postagens de Instagram bem escritas, atraentes e em português do Brasil, "
                           "formatadas conforme especificado para o tópico {topic}."),
    agent=escritor_post,
    verbose=True
)

criacao_imagem_task = Task(
    description="Crie {n} prompts para criar uma imagem atraente para acompanhar a postagem no Instagram sobre {topic}.",
    expected_output=dedent("{n} prompts de alta qualidade adequados para o Instagram baseados em {topic}."),
    agent=gerador_de_midia,
    verbose=True
)

revisao_task = Task(
    description=dedent("Revise as {n} escritas e prompts de imagens "
                       "para as {n} postagens do cliente e garanta "
                       "que as informações de cada postagem estejam organizadas, sem erros e cativantes "
                       "em português do Brasil sobre {topic}. "
                       "Certifique-se de que cada post está formatado como:\n\n"
                       "POST:\ntexto do post em português do brasil\n\n"
                       "PROMPT:\nPrompt da imagem desse post\n\n"),
    expected_output=dedent("{n} textos e prompts de imagens organizados por post, revisados e prontos para serem publicados "
                           "em português do Brasil, formatados conforme especificado."),
    agent=formatador,
    verbose=True
)

# Criação da Tripulação
crew = Crew(
    agents=[planejador, pesquisador, escritor_post, gerador_de_midia, formatador],
    tasks=[plano_task, pesquisa_task, escrita_task, criacao_imagem_task, revisao_task],
    process=Process.sequential,
    verbose=True,
    memory=True
)

# Execução da Tripulação
result = crew.kickoff(inputs={
    'topic': 'Monitoramento Ambiental',
    'n': 1,
    'mídia social': 'instagram',
    'estratégia de venda': 'Destaque insights em tempo real para otimizar sustentabilidade e desempenho.',
    'publico-alvo': 'Empresas e instituições brasileiras focadas em sustentabilidade e eficiência operacional.'
})

# Tenta converter o resultado para string diretamente
content_to_write = str(result)

# Salvar resultado em arquivo
current_date = datetime.now().strftime("%Y-%m-%d")
filename = f"posts-{current_date}.txt"

with open(filename, 'w', encoding='utf-8') as file:
    file.write(content_to_write)  # Escreve o conteúdo convertido

print(f"Resultado salvo em {filename}")
