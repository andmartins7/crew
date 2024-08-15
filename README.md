# AI Marketing Agency with CrewAI

Welcome to the **AI Marketing Agency** project, a robust solution powered by CrewAI that enables automated content creation, scheduling, and publishing for marketing agencies. This project leverages the power of multiple AI agents, orchestrated to work together in delivering high-quality marketing content.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Setup](#environment-setup)
  - [Running the Application](#running-the-application)
- [Agent Roles and Tasks](#agent-roles-and-tasks)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project is designed to automate the marketing content creation process using a team (crew) of intelligent AI agents. These agents are responsible for tasks such as planning, researching, writing, and publishing content across social media platforms, particularly Instagram. The goal is to streamline the marketing process, reduce manual workload, and enhance the efficiency of content delivery.

## Features

- **Multi-Agent Collaboration**: A team of specialized AI agents working together to create and publish marketing content.
- **Automated Content Creation**: Agents automatically generate content based on the latest trends and customer inputs.
- **Scheduled Publishing**: Content is strategically planned and published at optimal times for maximum engagement.
- **Customizable Workflow**: Easily modify agents and tasks to suit specific marketing needs and goals.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher installed on your machine
- An OpenAI API key and a Groq API key for the language models
- A working knowledge of Python and AI/ML concepts

### Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/ai-marketing-agency.git
cd ai-marketing-agency
```

### Environment Setup

1. **Install the necessary Python libraries:**

   ```bash
   pip install crewai crewai-tools langchain_openai langchain_groq python-dotenv textwrap3
   ```
   
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your environment variables:**

   Create a `.env` file in the root directory and add your API keys:

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

### Running the Application

To run the AI Marketing Agency crew, execute the following command:

```bash
python main.py
```

This will initiate the crew of AI agents who will start generating and publishing marketing content based on the provided inputs.

## Agent Roles and Tasks

This project involves a sophisticated setup of various AI agents, each with a specific role:

- **Content Strategist Agent**: Develops a detailed posting schedule and optimizes it for maximum engagement.
- **Activity Initiator Agent**: Ensures that all planned activities are executed according to the schedule.
- **Content Planner Agent**: Organizes and prepares the content for posting, aligning with audience interests.
- **Content Researcher Agent**: Gathers the latest trends and relevant information to inform content creation.
- **Post Writer Agent**: Crafts engaging and well-structured posts for Instagram.
- **Prompt Writer Agent**: Creates detailed prompts for image generation using DALL-E.
- **Media Generator Agent**: Generates visual content using DALL-E based on provided prompts.
- **Post Formatter Agent**: Ensures the final content is formatted to meet Instagram's best practices.
- **Final Reviewer Agent**: Reviews the content to ensure it meets the required quality standards.
- **Media Publisher Agent**: Publishes the content on Instagram using the Instagram API.

## Customization

This setup is fully customizable to meet your specific needs. You can modify:

- **Agent Goals**: Change the goals of each agent to suit different marketing strategies.
- **Tasks**: Add or remove tasks, or modify existing ones to better fit your workflow.
- **Tools**: Integrate additional tools as required by your agents.

To customize the agents and tasks, simply edit the corresponding Python scripts or the configuration files.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
