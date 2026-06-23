# Project - Agent Improv

Most important: Keep the application simple, don't over-complicate it, be creative, and have fun!
The point is to get a working, demo-able agent up and running as fast as possible. It doesn't have to be perfect or handle every edge case.

## Constraints

- Build a Google Agent Development Kit (ADK) Agent in Python
  -  Use https://adk.dev/llms.txt for finding information about ADK
- Don't create a venv
- Don't make a UI, just build the agent.
- Give the agent useful tools.
- Use the Gemini API on Agent Platform (formerly Vertex AI) with model `gemini-3.1-flash-lite`
  - IMPORTANT: This model only works with the `global` endpoint.
  - Copy the `.env` file into the agent directory. Use this file to set project/location. 
- Don't test anything.
- Commit and push the code to the GitHub Repository before deploying.

- Deploy the agent to Agent Runtime (formerly called Vertex AI Agent Engine)

Example command for how to deploy an ADK Agent to Agent Runtime. This should be run from the parent directory of where the agent code is.

```sh
adk deploy agent_engine --region="us-east1" --display_name="Agent Display Name" directory_of_agent
```
