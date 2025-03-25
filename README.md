This project combines a game built with pygame and sprites with 
LLM-powered NPC interactions using langchain and Ollama.

1. PREREQUISITES
Make sure you have the following installed on your system:
	Python (>= 3.8)
	pip (Python package manager)

2. CREATE AND ACTIVATE A VIRTUAL ENVIRONMENT (OPTIONAL BUT RECOMMENDED)
	Windows:
		python -m venv venv
		venv\Scripts\activate
	MacOS/Linux:
		python3 -m venv venv
		source venv/bin/activate

3. INSTALL REQUIRED LIBRARIES
	pip install pygame langchain_ollama langchain_core

4. INSTALL OLLAMA
	MacOS:
		brew install ollama
	Linux:
		curl -fsSL https://ollama.com/install.sh | bash
	On Windows:
		Download and Install from Ollam Website

5. RUN game.py
